from pathlib import Path


class KiCadProject:
    def __init__(self, dir: str) -> None:
        self.dir = Path(dir)
        if not self.dir.is_dir():
            raise "Invalid directory path"
        return

    def output_files(self) -> list[str]:
        return [p for p in self.dir.iterdir() if p.is_file()]
