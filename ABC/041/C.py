# -*- coding: utf-8 -*-

_ = input()

students = {}
i = 1
input = [int(e) for e in input().split()]

for s in input:
    students[s] = i
    i += 1

for s in sorted(students.keys(), reverse=True):
    print(students[s])
