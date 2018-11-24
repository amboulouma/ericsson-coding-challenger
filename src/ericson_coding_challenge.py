
# Write a program that reads standard input. The input can
# contain multiple lines with words separated by whitespace.
# Treat words as case-insensitive.

# Print out the most frequent word (in lowercase) and its
# frequency in separate lines.

# Example input:
# foo
# bar bar
# foobar foo foo

# Expected output:
# foo
# 3

# Example input:
# horse power car
# cat powder milk
# pure Power muscle
# Anyway power is power

# Expected output:
# power
# 4
    
n = sorted(list(map(int, input().split())))
print(n)
if len(n)%2 == 0:
    print((n[len(n)//2 - 1] + n[len(n)//2])/2)
else:
    print(n[len(n)//2])