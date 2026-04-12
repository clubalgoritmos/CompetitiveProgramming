def range_in_parts(start, end, step, part_size):
    for i in range(start, end, step * part_size):
        yield from range(i, min(i + step * part_size, end), step)

# Example usage:
for num in range_in_parts(0, 10, 1, 2):
    print(num)