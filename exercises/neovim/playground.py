"""
NeoVim practice file. Navigate this with Telescope and oil.nvim.
Good motions to practice here:
  - gg / G        jump to top / bottom
  - { / }         jump between blank lines (paragraph motion)
  - gd            go to definition (once LSP is set up)
  - *             search for the word under cursor
  - %             jump between matching brackets
  - zc / zo       fold / unfold a block
"""

import math
import random
from dataclasses import dataclass
from typing import Optional


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self) -> str:
        return f"Point({self.x:.2f}, {self.y:.2f})"


@dataclass
class Rectangle:
    origin: Point
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def contains(self, point: Point) -> bool:
        return (
            self.origin.x <= point.x <= self.origin.x + self.width
            and self.origin.y <= point.y <= self.origin.y + self.height
        )


# ── Pure functions ─────────────────────────────────────────────────────────────

def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation between a and b by factor t (0.0 – 1.0)."""
    return a + clamp(t, 0.0, 1.0) * (b - a)


def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


# ── Text utilities ─────────────────────────────────────────────────────────────

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:\"'")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(counts: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix


# ── Simple simulation ──────────────────────────────────────────────────────────

def random_walk(steps: int, seed: Optional[int] = None) -> list[Point]:
    """2D random walk. Each step moves ±1 on x or y axis."""
    rng = random.Random(seed)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = 0.0, 0.0
    path = [Point(x, y)]
    for _ in range(steps):
        dx, dy = rng.choice(directions)
        x += dx
        y += dy
        path.append(Point(x, y))
    return path


def bounding_box(points: list[Point]) -> Rectangle:
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    origin = Point(min(xs), min(ys))
    return Rectangle(origin, max(xs) - min(xs), max(ys) - min(ys))


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    # Geometry
    a = Point(0, 0)
    b = Point(3, 4)
    print(f"Distance from {a} to {b}: {a.distance_to(b)}")

    rect = Rectangle(Point(1, 1), 10, 5)
    print(f"Rectangle area: {rect.area}, perimeter: {rect.perimeter}")
    print(f"Contains {b}: {rect.contains(b)}")

    # Math
    print(f"\nFirst 10 fibonacci: {fibonacci(10)}")
    print(f"Primes up to 50: {primes_up_to(50)}")
    print(f"lerp(0, 100, 0.25) = {lerp(0, 100, 0.25)}")

    # Text
    sample = "the quick brown fox jumps over the lazy dog the fox"
    counts = word_count(sample)
    print(f"\nTop words: {most_common(counts, 3)}")
    print(truncate("a very long string that needs to be shortened", 30))

    # Simulation
    path = random_walk(200, seed=42)
    box = bounding_box(path)
    print(f"\nRandom walk bounding box: {box.width:.0f}w x {box.height:.0f}h")
    print(f"Final position: {path[-1]}")


if __name__ == "__main__":
    main()
