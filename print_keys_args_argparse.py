import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('key_values', nargs='*', type=str)

    args = parser.parse_args()

    parsed = {}
    for arg in args.key_values:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed[key] = value

    items = parsed.items()
    if args.sort:
        items = sorted(items, key=lambda x: x[0])

    for k, v in items:
        print(f"Key: {k} Value: {v}")

if __name__ == "__main__":
    main()