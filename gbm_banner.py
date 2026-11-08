#!/usr/bin/env python3
"""
Daily "simulated market" banner for the profile README.

Pure standard library. Seeded by the UTC date, so every day draws a different
picture but any given day is exactly reproducible.

What it does each run:
  1. Simulates Geometric Brownian Motion paths under the risk-neutral measure.
  2. Prices a European call by Monte Carlo with antithetic variates.
  3. Compares against the closed-form Black-Scholes price.
  4. Writes assets/gbm.svg with the paths and the live pricing error.
"""
import datetime
import math
import pathlib
import random

S0, K, R, SIGMA, T = 100.0, 100.0, 0.05, 0.25, 1.0
STEPS, PATHS_DRAWN, N_PRICE = 120, 40, 60_000
W, H, PAD = 960, 320, 28


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_call(s, k, r, sigma, t):
    d1 = (math.log(s / k) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return s * norm_cdf(d1) - k * math.exp(-r * t) * norm_cdf(d2)


def mc_call_antithetic(rng, n):
    drift = (R - 0.5 * SIGMA**2) * T
    vol = SIGMA * math.sqrt(T)
    disc = math.exp(-R * T)
    m = n // 2
    acc = acc2 = 0.0
    for _ in range(m):
        z = rng.gauss(0.0, 1.0)
        pay = 0.5 * (
            max(S0 * math.exp(drift + vol * z) - K, 0.0)
            + max(S0 * math.exp(drift - vol * z) - K, 0.0)
        )
        acc += pay
        acc2 += pay * pay
    mean = acc / m
    se = math.sqrt(max(acc2 / m - mean**2, 0.0) / m)
    return disc * mean, disc * se


def simulate_paths(rng):
    dt = T / STEPS
    drift = (R - 0.5 * SIGMA**2) * dt
    vol = SIGMA * math.sqrt(dt)
    paths = []
    for _ in range(PATHS_DRAWN):
        p, s = [S0], S0
        for _ in range(STEPS):
            s *= math.exp(drift + vol * rng.gauss(0.0, 1.0))
            p.append(s)
        paths.append(p)
    return paths


def render(paths, mc, se, bs, seed_label):
    lo = min(min(p) for p in paths)
    hi = max(max(p) for p in paths)
    top, bottom = 64, H - 58

    def X(i):
        return PAD + (W - 2 * PAD) * i / STEPS

    def Y(v):
        return bottom - (bottom - top) * (v - lo) / (hi - lo)

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" '
               f'aria-label="Simulated GBM paths with Monte Carlo versus Black-Scholes pricing">')
    out.append('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
               '<stop offset="0" stop-color="#14123A"/><stop offset="1" stop-color="#241B5E"/></linearGradient></defs>')
    out.append(f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)" stroke="#6C4CF1" stroke-opacity="0.6"/>')
    for g in range(1, 5):
        gy = top + (bottom - top) * g / 5
        out.append(f'<line x1="{PAD}" x2="{W-PAD}" y1="{gy:.1f}" y2="{gy:.1f}" stroke="#ffffff" stroke-opacity="0.06"/>')
    for p in paths:
        color = "#3DDBB0" if p[-1] > K else "#FF6B5E"
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(p))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-opacity="0.45" stroke-width="1.2"/>')
    mean_path = [sum(p[i] for p in paths) / len(paths) for i in range(STEPS + 1)]
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(mean_path))
    out.append(f'<polyline points="{pts}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    ky = Y(K)
    out.append(f'<line x1="{PAD}" x2="{W-PAD}" y1="{ky:.1f}" y2="{ky:.1f}" stroke="#EEEAFE" stroke-opacity="0.7" stroke-dasharray="6 6"/>')
    out.append(f'<text x="{W-PAD}" y="{ky-6:.1f}" text-anchor="end" font-family="monospace" font-size="12" fill="#EEEAFE">K = {K:.0f}</text>')
    mono = 'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"'
    out.append(f'<text x="{PAD}" y="30" {mono} font-size="15" font-weight="700" fill="#3DDBB0">'
               f'TODAY\'S MARKET, SIMULATED BY MY OWN ENGINE</text>')
    out.append(f'<text x="{PAD}" y="50" {mono} font-size="12" fill="#EEEAFE" fill-opacity="0.8">'
               f'GBM  S0={S0:.0f}  r={R:.0%}  sigma={SIGMA:.0%}  T={T:.0f}y  seed={seed_label}  drawn={PATHS_DRAWN} of {N_PRICE:,} priced</text>')
    err = mc - bs
    out.append(f'<text x="{PAD}" y="{H-34}" {mono} font-size="13" fill="#FFFFFF">'
               f'European call  MC(antithetic) = {mc:.4f} +/- {1.96*se:.4f}   |   Black-Scholes = {bs:.4f}   |   error = {err:+.4f}</text>')
    inside = abs(err) <= 1.96 * se
    verdict = "BS price sits inside the 95% interval" if inside else "BS price outside the 95% interval (it happens 1 day in 20)"
    out.append(f'<text x="{PAD}" y="{H-14}" {mono} font-size="12" fill="#3DDBB0">{verdict}</text>')
    out.append('</svg>')
    return "\n".join(out)


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    rng = random.Random(today.toordinal())
    paths = simulate_paths(rng)
    mc, se = mc_call_antithetic(rng, N_PRICE)
    svg = render(paths, mc, se, bs_call(S0, K, R, SIGMA, T), today.isoformat())
    out = pathlib.Path(__file__).resolve().parent.parent / "gbm.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out}  MC={mc:.4f}±{1.96*se:.4f}  BS={bs_call(S0,K,R,SIGMA,T):.4f}")


if __name__ == "__main__":
    main()
