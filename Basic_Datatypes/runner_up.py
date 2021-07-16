# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 

# You are given n scores. 

# Store them in a list and find the score of the runner-up

n = int(input())

#takes input value with space in a line, upto total values are = n
A = list(map(int,input().split()))[:n]

z = max(A)

while max(A) == z:
    A.remove(max(A))

print(max(A))    
