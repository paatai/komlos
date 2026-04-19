# Vector Signing ℓ_∞ Minimizer Demo

Interactive demonstration of signing unit vectors to keep the ℓ_∞ norm of their sum bounded.

**Try it live:**
https://colab.research.google.com/drive/15tdA5kr1BDuECJ7t9g1z6scqL81sgiqJ?usp=sharing

- Toggle blue/red buttons to flip vector signs
- Use Random, Greedy, Monte Carlo buttons
- Change n (number of vectors) with the slider

Shows that even for large n, you can usually keep ||sum||_∞ ≤ ~2–3.

---

## Manim scene: 2D Brownian motion in a disk

This repository now also includes a Manim scene, `brownian_motion_2d.py`, that shows a 2D Brownian walk:

- starts at the origin `0`
- uses a small step size
- stops exactly at the boundary of the disk of radius `2`
- highlights the moving particle in **red**

Render it with:

```bash
manim -pqh brownian_motion_2d.py BrownianMotion2D
```
