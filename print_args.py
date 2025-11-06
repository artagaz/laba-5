import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='*')
    args = parser.parse_args()

    if not args.params:
        print("no args")
    else:
        for param in args.params:
            print(param)

if __name__ == "__main__":
    main()