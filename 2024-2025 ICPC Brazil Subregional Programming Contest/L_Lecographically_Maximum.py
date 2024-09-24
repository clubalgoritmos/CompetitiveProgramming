def count_bits(numbers):
    max_num = max(numbers)
    max_len = max_num.bit_length()
    bit_positions = [0] * max_len
    for num in numbers:
        for i in range(max_len):
            if num & (1 << i):
                bit_positions[i] += 1
    return bit_positions

def form_numbers(bit_positions):
    numbers = []
    total_bits = sum(bit_positions)
    while total_bits > 0:
        num = 0
        for i in range(len(bit_positions)):
            if bit_positions[i] > 0:
                num |= (1 << i)
                bit_positions[i] -= 1
                total_bits -= 1
        numbers.append(num)
    return numbers

N = int(input())
numbers = list(map(int, input().split()))
bit_positions = count_bits(numbers)
result_numbers = form_numbers(bit_positions)

print(*result_numbers+[0]*(N-len(result_numbers)))