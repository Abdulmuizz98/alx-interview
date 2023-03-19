import sys
import re

lines = sys.stdin.readlines()
file_size = 0
count = {"200": 0, "301":0, "400": 0, "403": 0, "404": 0, "405": 0, "500": 0}

for i in range(len(lines)):
    line = lines[i][0:-1]
    try:
        if i % 10:
            # print what you need print
            print("File size:", file_size)
            [print('{}: {}'.format(k, v)) for k, v in count.items() if v]
            
        reg_fmt: str = '\d+\.\d+\.\d+\.\d+ - \[.*\] "GET \/projects\/260 HTTP\/1\.1" \d+ \d+'
        reg_stcode: str = '(?<=" ).*?(?= \d)'
        reg_filesz: str = '\d+$'
        match_fmt = re.findall(reg_fmt, line)
        if match_fmt: #use the main regex to check format
            match_stcode = re.findall(reg_stcode, line) # use the backtracking to get only size
            if match_stcode and count.get(match_stcode[0]):
                count[match_stcode[0]] += 1
                file_size += re.findall(reg_filesz, line)[0]
    except KeyboardInterrupt:
        # print before you time out
        print("File size:", file_size)
        [print('{}: {}'.format(k, v)) for k, v in count.items() if v]