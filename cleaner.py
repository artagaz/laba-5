import os
import sys

from size import get_readable_size

def get_dir_size(directory):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except OSError:
                    pass
    except PermissionError:
        pass
    return total_size

def get_top_dirs(path):
    dirs_with_size = []
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                size = get_dir_size(item_path)
                dirs_with_size.append((size, item))
    except PermissionError:
        pass

    dirs_with_size.sort(reverse=True, key=lambda x: x[0])
    for size, name in dirs_with_size[:10]:
        readable_size = get_readable_size(size)
        print(f"{name} - {readable_size}")

if __name__ == "__main__":
    target_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    get_top_dirs(target_path)