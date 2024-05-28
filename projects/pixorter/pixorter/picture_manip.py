"""Contains top-level methods for manipulating Picture objects"""

from pathlib import Path
from typing import Generator, Iterable, Set

from .date_extract import get_snap_date
from .file_manip import walk_dir
from .picture import Picture


def collect_pictures(root_path: Path) -> Generator[Picture, None, None]:
    for file in walk_dir(root_path):
        yield Picture(source_path=file, snap_date=get_snap_date(file))


def get_output_paths(pictures: Iterable[Picture]) -> Generator[Path, None, None]:
    """
    Get all the output paths for the pictures passed as input.
    The function makes sure no duplicate Paths are returned (even if the snap datetimes are equal)
    """
    used_paths: Set[Path] = set()

    for picture in pictures:
        duplicate_count = 1
        while (output_path := picture.get_output_path(duplicate_count)) in used_paths:
            duplicate_count += 1

        yield output_path
