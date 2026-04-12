size = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def roman_to_arabic(roman):
    total = 0
    max_right = 0
    for char in reversed(roman):
        value = size[char]
        if value < max_right:
            total -= value
        else:
            total += value
            max_right = value
    return total

n = int(input())
for _ in range(n):
    roman = input().strip()
    print(roman_to_arabic(roman))