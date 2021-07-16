# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

m = int(input())

M = set(map(int,input().split()))
n = int(input())

N = set(map(int,input().split()))
r = sorted(list(M.symmetric_difference(N)))

for i in r:
    print(i)
