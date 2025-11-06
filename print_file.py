import argparse

def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return str(e)

    lines = content.splitlines()
    formatted_lines = []

    for line in lines:
        if len(line) == 0:
            formatted_lines.append("")
            continue

        start = 0
        while start < len(line):
            end = start + frame_width
            chunk = line[start:end]
            formatted_lines.append(chunk)
            start = end

    result_lines = formatted_lines[:frame_height]
    return "\n".join(result_lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int, required=True)
    parser.add_argument('--frame-width', type=int, required=True)
    parser.add_argument('file_name', type=str)

    args = parser.parse_args()

    result = format_text_block(args.frame_height, args.frame_width, args.file_name)
    print(result)

if __name__ == "__main__":
    main()
