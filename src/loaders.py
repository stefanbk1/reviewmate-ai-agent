import json
from pathlib import Path
from typing import Any, Dict


def load_json(path: str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"JSON fajl ne postoji: {path}")
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Tekstualni fajl ne postoji: {path}")
    return file_path.read_text(encoding="utf-8")
