"""Fortune Cookies for Machines — print one fortune line.

Reads the fortune from entry.txt (kept next to this script) and prints
it exactly once, with no extra output.
"""

from pathlib import Path


def load_fortune(path: Path) -> str:
    """Return the fortune line from *path*, stripped of trailing newlines."""
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError(f"fortune file is empty: {path}")
    if len(line) > 200:
        raise ValueError(f"fortune exceeds 200 chars ({len(line)}): {path}")
    return line


def main() -> None:
    fortune = load_fortune(Path(__file__).with_name("entry.txt"))
    print(fortune)


if __name__ == "__main__":
    main()
