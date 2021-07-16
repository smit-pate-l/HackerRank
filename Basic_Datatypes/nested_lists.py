n = int(input())
a = [[input(),float(input())]  for i in range(n)]
second_lowest = sorted(list(set([marks for name, marks in a])))[1]

print('\n'.join([names for names,marks in sorted(a) if marks == second_lowest]))
