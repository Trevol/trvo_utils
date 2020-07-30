import os
from glob import glob


def ensureRelativeToDir(directory: str, path: str):
    assert path is not None and directory is not None
    directory = str(directory)
    path = str(path)
    # absolute path (/....) or explicitly relative (../ or ./)
    if path.startswith(os.sep) or path.startswith('.'):
        return path
    return os.path.join(directory, path)


def list_files(dirs, extensions):
    for d in dirs:
        files = []
        for e in extensions:
            files.extend(glob(os.path.join(d, '*.' + e)))
        for f in sorted(set(files)):
            yield f