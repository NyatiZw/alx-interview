#!/usr/bin/python3
import sys

def main():
    total_size = 0
    status_code_count = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            if line_number % 10 == 0:
                print_statistics(total_size, status_code_count)

            try:
                ip, date, request, status_code, file_size = parse_line(line)
                total_size += file_size
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_code_count[status_code] = status_code_count.get(status_code, 0) + 1
            except ValueError:
                continue
    except KeyboardInterrupt:
        print_statistics(total_size, status_code_count)

def parse_line(line):
    parts = line.split()
    if len(parts) == 10:
        ip, date, request, status_code, file_size = parts[0], parts[3], parts[5], int(parts[8]), int(parts[9])
        return ip, date, request, status_code, file_size
    else:
        raise ValueError("Invalid line format")

def print_statistics(total_size, status_code_count):
    print(f"Total file size: File size: {total_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

if __name__ == "__main__":
    main()
