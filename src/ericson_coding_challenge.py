# Write a program that reads 24-hour time (HH:MM) and an integer from
# standard input. The program should print the time in same format
# after the integer number of minutes has been added to it.

# Example input:
# 13:20 17

# Expected output:
# 13:37

# Example input:
# 02:00 65

# Expected output:
# 03:05

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

