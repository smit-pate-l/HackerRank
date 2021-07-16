# You are given a set A and N number of other sets. 
# These N number of sets have to perform some specific mutation operations on set .
# Your task is to execute those operations and print the sum of elements from set .

_ = int(input())
A = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, var = input().split()
    N = set(map(int, input().split()))
    getattr(A,cmd)(N)
print(sum(A))
    
