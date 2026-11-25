"""One Star, Five Stars for the Food.

Writes one sentence to /output/entry.txt: a one-star review of Earth
written by an alien tourist that still slips in a sincere compliment
about the food.
"""

import os

# One sentence, one star, one sincere compliment about the food.
REVIEW = (
    "One star: the locals worship glowing rectangles, queueing is a "
    "religion, and the Wi-Fi is a myth — but the noodles alone are "
    "worth invading this planet for."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        # No trailing newline: the sentence is the whole entry.
        os.write(fd, REVIEW.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
