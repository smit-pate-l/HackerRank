# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
print(sum(s))
    
