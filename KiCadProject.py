from pathlib import Path
from typing import List, Optional


class KiCadProject:
    # bad pracice ot use an __init__ file do more than one thing
    def __init__(self, directory) -> Optional[None]:
        self.directory = Path(dir)
        if not self.directory.is_dir():
            raise "Invalid directory path"
        return None

    def output_files(self) -> List[str]:
        return [p for p in self.directory.iterdir() if p.is_file()]
