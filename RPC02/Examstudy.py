def max_passed_exams(exams):
    exams.sort(key=lambda x: x[3]*abs(x[2]-x[1]))  # Sort exams by start time
    current_time = 0
    passed_exams = 0

    for si, pi, ei, ai in exams:
        if current_time + ai <= si:
            current_time = si + ai
        else:
            current_time = ei
            passed_exams += 1

    return passed_exams

# Read input
n = int(input())
exams = []
for _ in range(n):
    si, pi, ei, ai = map(int, input().split())
    exams.append((si, pi, ei, ai))

# Calculate and output the maximum number of exams you can pass
result = max_passed_exams(exams)
print(result)
