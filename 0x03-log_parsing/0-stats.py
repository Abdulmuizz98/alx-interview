#!/usr/bin/python3

if __name__ == '__main__':
    """ This module has been duly documented. this is not too much """
    import sys
    import re

    file_size = 0
    count = {
        "200": 0, "301": 0, "400": 0, "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0
    try:
        for line in sys.stdin:
            line = line[0:-1]
            if line_count != 0 and line_count % 10 == 0:
                # print what you need print
                print("File size:", file_size)
                [print('{}: {}'.format(k, v)) for k, v in count.items() if v]

            first = r'\d+\.\d+\.\d+\.\d+ - \[.*\]'
            second = r'"GET \/projects\/260 HTTP\/1\.1" \d+ \d+'
            reg_fmt: str = '{} {}'.format(first, second)

            reg_stcode: str = r'(?<=" ).*?(?= \d)'
            reg_filesz: str = r'\d+$'
            match_fmt = re.findall(reg_fmt, line)
            print('match_fmt:', match_fmt)
            if match_fmt:  # use the main regex to check format
                match_stcode = re.findall(reg_stcode, line)  # get size
                print("match_stcode:", match_stcode)
                if match_stcode and match_stcode[0] in count:
                    count[match_stcode[0]] += 1
                    file_size += int(re.findall(reg_filesz, line)[0])
            line_count += 1
    except KeyboardInterrupt:
        # print before you time out
        print("File size:", file_size)
        [print('{}: {}'.format(k, v)) for k, v in count.items() if v]
        raise
