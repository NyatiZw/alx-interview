#!/usr/bin/python3
import sys

def main():
    total_size = 0
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_number = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if is_valid_line(line):
                line_number += 1
                _, _, _, status_code, file_size = parse_line(line)
                total_size += file_size
                if status_code in status_code_count:
                    status_code_count[status_code] += 1

            if line_number % 10 == 0:
                print_statistics(total_size, status_code_count)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code_count)

def is_valid_line(line):
    # Check if a line matches the expected format
    return line.count('"') >= 2 and line.count('[') >= 1

def parse_line(line):
    # Parse the line and extract status code and file size
    parts = line.split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size

def print_statistics(total_size, status_code_count):
    print(f"Total file size: File size: {total_size}")
    for status_code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{status_code}: {count}")

if __name__ == "__main__":
    main()
