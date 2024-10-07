#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

prev_deptno = None
enames = []

for line in sys.stdin:
    line = line.strip()
    deptno, table_value = line.split("\t")
    table, value = table_value.split(",", maxsplit=1)

    if prev_deptno == deptno:
        if table == 'emp':
            enames.append(value)
    else:
        # 이전 부서에 대한 결과를 출력
        if prev_deptno and enames:
            for ename in enames:
                print(ename)

        # 새 부서 데이터 초기화
        if table == 'emp':
            enames = [value]
        else:
            enames = []
        prev_deptno = deptno

# 마지막 부서에 대한 출력
if prev_deptno and enames:
    for ename in enames:
        print(ename)
