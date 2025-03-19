X = int(input())

roman_map = [
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

result = ""

for value, symbol in roman_map:
    while X >= value:
        result += symbol
        X -= value

print(result)
