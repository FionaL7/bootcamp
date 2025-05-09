import sys

for line in sys.stdin:
    sys_line = line.strip()
    uppercase_response = sys_line.upper()
    print(uppercase_response)
