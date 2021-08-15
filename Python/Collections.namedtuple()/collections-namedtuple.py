# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

s, Student = int(input()), namedtuple('Student', input())

total = 0

for i in range(s):
    student = Student(*input().split())
    total += int(student.MARKS)
    
print(format(total / s, '.2f'))

# more pythonic

#scores = [Student(*input().split()).MARKS for i in range(s)]
#print("%.2f"% (sum(map(int,scores))/s))
