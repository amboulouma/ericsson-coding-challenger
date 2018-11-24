from collections import Counter
data = ""
while True:
    try:
        s = input()
        if not s: break
        data += s + " "
    except:
        KeyboardInterrupt

user_input = data.split()
c = Counter(user_input)

print(c.most_common()[0][0])    
print(c.most_common()[0][1])    