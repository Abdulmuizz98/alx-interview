#!/usr/bin/python3
''' A script that reads stdin line by line and computes metrics'''


if __name__ == '__main__':
    import sys
    import re

    file_size = 0
    count = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line[0:-1]
            if line_count != 0 and line_count % 10 == 0:
                print("File size:", file_size)
                [print('{}: {}'.format(
                       k, v)) for k, v in sorted(count.items()) if v]

            first = r'\d+\.\d+\.\d+\.\d+ - \[.*\]'
            second = r'"GET \/projects\/260 HTTP\/1\.1" \d+ \d+'
            reg_fmt = '{} {}'.format(first, second)
            reg_stcode = r'(?<=" ).*?(?= \d)'
            reg_filesz = r'\d+$'

            match_fmt = re.findall(reg_fmt, line)
            if match_fmt:  # use the main regex to check format
                match_stcode = re.findall(reg_stcode, line)  # get size
                if match_stcode and match_stcode[0] in count:
                    count[match_stcode[0]] += 1
                    file_size += int(re.findall(reg_filesz, line)[0])

            line_count += 1

    except KeyboardInterrupt:
        pass

    finally:
        print("File size:", file_size)
        [print('{}: {}'.format(
               k, v)) for k, v in sorted(count.items()) if v]
