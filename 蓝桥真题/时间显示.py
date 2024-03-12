ms = int(input())

s = ms // 1000
minute = s // 60
s = s % 60
hour = minute // 60
minute = minute % 60
hour = hour % 24

hours = str(hour) if hour >= 10 else "0" + str(hour)
minutes = str(minute) if minute >= 10 else "0" + str(minute)
ss = str(s) if s >= 10 else "0" + str(s)
print(f"{hours}:{minutes}:{ss}")
