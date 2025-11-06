import sys

def parse_args():
    args = sys.argv[1:]
    sort_flag = False
    if '--sort' in args:
        sort_flag = True
        args.remove('--sort')

    parsed = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed[key] = value

    items = parsed.items()
    if sort_flag:
        items = sorted(items, key=lambda x: x[0])

    for key, value in items:
        print(f"Key: {key} Value: {value}")

if __name__ == "__main__":
    parse_args()