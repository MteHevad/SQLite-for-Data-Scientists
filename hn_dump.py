#! /usr/bin/env python

import sys
from os import getenv
from sqlite3 import connect
import fileinput
import json


def main():
    items = []
    with connect(getenv('DB_URI', './sqlite-olt.db')) as db:
        for hits, in db.execute("select json_extract(data, '$.hits') from search_results where json_valid(data) = 1 limit 50000"):
            items += json.loads(hits)
    print(json.dumps(items))


if __name__ == '__main__':
    main()