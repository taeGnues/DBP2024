#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.strip()
    deptno, table_value = line.split("\t")
    table, value = table_value.split(",", maxsplit=1)

    if table == 'emp':
        ename, salary = value.split(",", maxsplit=1)
        salary = float(salary)

        if salary >= 5000:
            print(f"{deptno}\t{table},{ename}")

    elif table == 'dept':
        print(f"{deptno}\t{table},{value}")

