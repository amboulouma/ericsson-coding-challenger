# Exercise 1

print("Hello Ericsson!")


# Exercise 3

n = input()
for i in range(int(n)):
    print((i+1)*"*")

# Exercise 4

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("HasselHoff")
    elif i%3 == 0:
        print("Hassel")
    elif i%5 == 0:
        print("Hoff")
    else:
        print(i)

# Exercise 5

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
        
# Exercise 6

s = input()
r = list(s)
for i in range(len(s)):
    print("".join(r))
    r[i] = " "