from __future__ import annotations
from pathlib import Path
from Typing import List, Optional


class KiCadProject:
    # keep one thing in the __init__ fuction
    def __init__(self, dir: str) -> Optional[None]:
        self.dir = Path(dir)
        if not self.dir.is_dir():
            raise "Invalid directory path"
        return

    def output_files(self) -> List[str]:
        return [p for p in self.dir.iterdir() if p.is_file()]
