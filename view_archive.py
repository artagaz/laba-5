from zipfile import ZipFile
import sys

from size import get_readable_size

with ZipFile(sys.argv[1]) as myzip:
    all_paths = set()

    for name in myzip.namelist():
        all_paths.add(name)
        if not name.endswith('/'):
            parts = name.split('/')
            for i in range(len(parts) - 1):
                dir_path = '/'.join(parts[:i + 1]) + '/'
                all_paths.add(dir_path)

    for path in sorted(all_paths):
        if len(sys.argv) != 3:
            print("Usage: python view_archive.py <arc_name>")
            exit(1)

        items = path.rstrip("/").split("/")

        depth = len(items) - 1
        indent = "  " * depth

        if path.endswith('/'):
            print(f"{indent}{items[-1]}")
        else:
            size_str = get_readable_size(myzip.getinfo(path).file_size)
            print(f"{indent}{items[-1]} {size_str}")
