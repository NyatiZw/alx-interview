#!/usr/bin/python3
""" Script that reads stdin and computes metrics"""


import sys
import re
from collections import defaultdict

log_format = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.+\] '
                        r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

total_size = 0
status_code_count = defaultdict(int)

line_count = 0

try:
    for line in sys.stdin:
        match = log_format.match(line)
        if match:
            ip, status_code, file_size = match.groups()
            total_size += int(file_size)
            status_code_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_code_count.keys()):
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    pass

print(f"File size: {total_size}")
for code in sorted(status_code_count.keys()):
    print(f"{code}: {status_code_count[code]}")
