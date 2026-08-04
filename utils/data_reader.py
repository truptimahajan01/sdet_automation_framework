import csv
from pathlib import Path


def read_csv(filename: str) -> list[dict]:
    """Read a CSV file from the test_data/ directory.

    Args:
        filename: Name of the CSV file (e.g., 'data.csv')

    Returns:
        List of dicts, one per row, with column headers as keys.
    """
    path = Path(__file__).parent.parent / "test_data" / filename

    if not path.exists():
        raise FileNotFoundError(f"Test data file not found: {path}")

    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
