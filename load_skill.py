"""load_skill.py — reads a markdown skill file and returns its content as a string."""

from pathlib import Path


def load_skill(path: str) -> str:
    """Load a skill definition from a markdown file.

    Args:
        path: Relative or absolute path to the .md skill file.

    Returns:
        The file contents as a string.

    Raises:
        FileNotFoundError: If the skill file does not exist.
    """
    skill_path = Path(path)
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {path}")
    return skill_path.read_text(encoding="utf-8")
