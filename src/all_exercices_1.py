# Exercise 1

print("Hello Ericsson!")


# Exercise 2

n = input()
for i in range(int(n)):
    print((i+1)*"*")

# Exercise 3

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("HasselHoff")
    elif i%3 == 0:
        print("Hassel")
    elif i%5 == 0:
        print("Hoff")
    else:
        print(i)

# Exercise 4

s = input()
f = ""
stack = []
parenthese = {
    "(":")"
}
for parenthese_ in s:
    if parenthese_ in parenthese:
        stack.append(parenthese_)
    elif len(stack) == 0 or parenthese[stack.pop()] != parenthese_:
        f = "false"
    else:
       f = str(len(stack) == 0).lower()
        
# Exercise 5

s = input()
r = list(s)
for i in range(len(s)):
    print("".join(r))
    r[i] = " "

# Exercise 6

n = int(input())

for i in range(1, n+1):
    print("/", end="")
    if i%3 == 0:
        print("", end=" ")
 
# Exercise 7

n = sorted(list(map(int, input().split())))
print(n)
if len(n)%2 == 0:
    print((n[len(n)//2 - 1] + n[len(n)//2])/2)
else:
    print(n[len(n)//2])

# Exercise 8

from collections import Counter
data = ""
while True:
    s = input()
    if not s: break
    data += s + " "

user_input = data.split()
c = Counter(user_input)

print(c.most_common()[0][0])

# Exercise 9

time = input().split(":")
hours = int(time[0])
minutes_op = time[1].split()
minutes = int(minutes_op[0])
minutes_to_add = int(minutes_op[1])
minutes += minutes_to_add
hours += minutes//60
minutes = minutes%60

hours_to_str = str(hours)
minutes_to_str = str(minutes)

if len(hours_to_str) < 2: hours_to_str = "0" + hours_to_str
if len(minutes_to_str) < 2: minutes_to_str = "0" + minutes_to_str
print("{}:{}".format(hours_to_str,minutes_to_str))

# Exercise 10

n = list(map(int, input().split()))
print(n[len(n)//2])

