from __future__ import annotations
from pathlib import Path
from Excellon import Excellon
from Gerber import Gerber


class KiCadProject:
    def __init__(self, project_dir: Path, output_dir: Path, gerber_files: list[Gerber], drill_files: list[Excellon]) -> None:
        self.project_dir = project_dir
        self.output_dir = output_dir
        self.gerber_files = gerber_files
        self.drill_files = drill_files

    @classmethod
    def load(dir: str) -> KiCadProject:
        dir_path = Path(dir)
        if not dir_path.is_dir():
            raise 'Invalid directory path'

        output_path = dir_path / 'out'
        if not output_path.is_dir():
            raise "Project output directory not found. Ensure the project contains a directory named 'out'."

        gerber_files = [Gerber(f) for f in output_path.glob('**/*.gbr')]
        drill_files = [Excellon(f) for f in output_path.glob('**/*.drl')]
        if gerber_files.count() == 0:
            raise 'No gerber files found in output directory. Did you forget to plot the board?'

        return KiCadProject(dir_path, output_path, gerber_files, drill_files)
