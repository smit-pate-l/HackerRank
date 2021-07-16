#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .

#print: Print the list.

#remove e: Delete the first occurrence of integer .

#append e: Insert integer  at the end of the list.

#sort: Sort the list.

#pop: Pop the last element from the list.

#reverse: Reverse the list.

#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

n = int(input())
lst = []


for _ in range(n):
    s_lst = input().split()
    
    for i in range(1,len(s_lst)):
        s_lst[i] = int(s_lst[i])
    
    if s_lst[0] == "append":
        lst.append(s_lst[1])
    elif s_lst[0] == "insert":
        lst.insert(s_lst[1],s_lst[2])
    elif s_lst[0] == "remove":
        lst.remove(s_lst[1])
    elif s_lst[0] == "pop":
        lst.pop()
    elif s_lst[0] == "sort":
        lst.sort(s_lst)
    elif s_lst[0] == "reverse":
        lst.reverse(s_lst)
    elif s_lst[0] == "print":
        print(lst)
  
