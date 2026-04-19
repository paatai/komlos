from __future__ import annotations

import numpy as np
from manim import *


class BrownianMotion2D(Scene):
    def construct(self) -> None:
        rng = np.random.default_rng(7)
        radius = 2.0
        step_size = 0.03
        max_steps = 50000

        title = Title("2D Brownian Motion in a Disk")
        subtitle = Text(
            "Starts at 0 and stops at the boundary of radius 2",
            font_size=30,
            color=GRAY_B,
        ).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), FadeIn(subtitle, shift=0.2 * DOWN))

        disk = Circle(radius=radius, color=BLUE_C, stroke_width=4)
        origin_dot = Dot(ORIGIN, radius=0.06, color=WHITE)
        origin_label = MathTex("0", font_size=34).next_to(origin_dot, DOWN + LEFT, buff=0.08)
        self.play(Create(disk), FadeIn(origin_dot), Write(origin_label))

        points = [np.array([0.0, 0.0, 0.0])]
        for _ in range(max_steps):
            direction = rng.normal(size=2)
            direction /= np.linalg.norm(direction)
            prev = points[-1].copy()
            candidate = prev.copy()
            candidate[:2] += step_size * direction

            if np.linalg.norm(candidate[:2]) >= radius:
                delta = candidate[:2] - prev[:2]
                a = np.dot(delta, delta)
                b = 2 * np.dot(prev[:2], delta)
                c = np.dot(prev[:2], prev[:2]) - radius**2
                t = (-b + np.sqrt(max(b * b - 4 * a * c, 0.0))) / (2 * a)
                hit = prev.copy()
                hit[:2] = prev[:2] + t * delta
                points.append(hit)
                break

            points.append(candidate)

        path = VMobject(color=YELLOW, stroke_width=3)
        path.set_points_as_corners([points[0], points[0]])

        moving_point = Dot(points[0], radius=0.075, color=RED)
        moving_label = Text("moving point", font_size=24, color=RED)
        moving_label.add_updater(lambda m: m.next_to(moving_point, UP + RIGHT, buff=0.1))

        self.add(path, moving_point, moving_label)

        def update_walk(mob: Dot, alpha: float) -> None:
            idx = min(int(alpha * (len(points) - 1)), len(points) - 1)
            current = points[idx]
            mob.move_to(current)
            path.set_points_as_corners(points[: idx + 1])

        run_time = min(14, 4 + 0.004 * len(points))
        self.play(UpdateFromAlphaFunc(moving_point, update_walk), run_time=run_time, rate_func=linear)

        moving_label.clear_updaters()
        boundary_text = Text("Boundary reached", font_size=32, color=GREEN_B).next_to(
            disk, DOWN, buff=0.35
        )
        self.play(Write(boundary_text))
        self.wait(2)
