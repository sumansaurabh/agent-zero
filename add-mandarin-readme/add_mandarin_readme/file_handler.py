import os
from pathlib import Path

def read_readme(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Source README file not found at: {file_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_readme(file_path: str, content: str) -> None:
    path = Path(file_path)
    # Ensure the directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
