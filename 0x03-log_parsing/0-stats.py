#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics:

    -   Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size> (if the format is not this one, the line
        must be skipped)

    -   After every 10 lines and/or a keyboard interruption (CTRL + C),
        print these statistics from the beginning:

        *   Total file size: File size: <total size>
        *   where <total size> is the sum of all previous <file size>
            (see input format above)
        *   Number of lines by status code:
            =   possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            =   if a status code doesn’t appear or is not an integer,
                don’t print anything for this status code
            =   format: <status code>: <number>
            =   status codes should be printed in ascending order
"""

if __name__ == '__main__':
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
