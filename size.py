import os

def get_readable_size(size):
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    unit_index = 0
    while size > 1023 and unit_index < len(units) - 1:
        size //= 1024
        unit_index += 1
    return f"{size}{units[unit_index]}"

def get_filesizes():
    filesizes = []
    for f in os.listdir('.'):
        if os.path.isfile(f):
            size = os.path.getsize(f)
            readable_size = get_readable_size(size)
            filesizes.append(f"{f} {readable_size}\n")
    return ''.join(filesizes)

if __name__ == "__main__":
    print(get_filesizes())