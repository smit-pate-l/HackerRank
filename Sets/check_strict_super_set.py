# You are given a set A and n other sets. 

# Your job is to find whether set A is a strict superset of each of the n sets.

# Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))


