#!/usr/bin/env python3

import csv
import glob

def main(argv=None):
    with open("index.csv") as inp:
        rows = csv.reader(inp)
        index = dict((row[0],row) for row in rows)
    files = set(glob.glob("*"))
    missing = files - index.keys()
    for m in missing:
        index[m] = [m,]
    with open("index.csv", 'w') as out:
        csv_out = csv.writer(out)
        for row in sorted(index.values()):
            csv_out.writerow(row)

if __name__ == '__main__':
    main()
