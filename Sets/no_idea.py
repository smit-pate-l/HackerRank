# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
# You like all the integers in set A and dislike all the integers in set B. 
# Your initial happiness is 0. 
# For each i integer in the array, if i is present in A , you add 1 to your happiness. 
# If i is present in B, you add -1 to your happiness. 
# Otherwise, your happiness does not change. 
# Output your final happiness at the end.


n, m = map(int, input().split())
lst = list(map(int, input().split()))[:n]
M = set(map(int, input().split()))
N = set(map(int, input().split()))
counter = 0
for i in lst:
    if i in M:
        counter += 1
    elif i in N:
        counter -= 1
print(counter)
