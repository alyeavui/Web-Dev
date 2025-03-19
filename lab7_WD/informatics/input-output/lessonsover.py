n = int(input())

lesson_duration = 45 
short_break = (n // 2) * 5 
long_break = ((n - 1) // 2) * 15  

total_minutes = 9 * 60 + n * lesson_duration + short_break + long_break 

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours, minutes)
