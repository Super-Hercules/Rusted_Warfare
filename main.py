import os

def extract_unit_name(input_dir):
    lines = []
    for file_name in os.listdir(input_dir):
        if file_name:
            lines.append(file_name.replace(".ini", "") + "\n")

    with open('extracted.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)


if __name__ == "__main__":
    extract_unit_name(os.path.join(os.path.dirname(os.path.abspath(__file__)), "1"))