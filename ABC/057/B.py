# -*- coding: utf-8 -*-
 
 
def solve(s_pp, p_pp):
    p_nums = []
    for x, y in s_pp:
        distance = []
        for xx, yy in p_pp:
            n = abs(x - xx) + abs(y - yy)
            distance.append(n)
        min_distance_idx = distance.index(min(distance))
        p_nums.append(min_distance_idx + 1)
    return p_nums
 
 
def main():
    students, points = [int(e) for e in input().split()]
    students_ps = []
    points_ps = []
 
    for _ in range(students):
        x, y = [int(e) for e in input().split()]
        students_ps.append([x, y])
    for _ in range(points):
        x, y = [int(e) for e in input().split()]
        points_ps.append([x, y])
    
    for answer in solve(students_ps, points_ps):
        print(answer)
 
 
main()
