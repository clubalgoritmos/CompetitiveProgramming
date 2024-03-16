def find_substring(S):
    start = 0
    min_length = float('inf')
    count = {str(i): 0 for i in range(1, 4)}
    distinct_count = 0

    for end in range(len(S)):
        if S[end] in count:
            count[S[end]] += 1
            if count[S[end]] == 1:
                distinct_count += 1

        while distinct_count == 3:
            min_length = min(min_length, end - start + 1)
            if S[start] in count:
                count[S[start]] -= 1
                if count[S[start]] == 0:
                    distinct_count -= 1
            start += 1

    return min_length if min_length != float('inf') else 0

for _ in range(int(input())):
    S = input()
    print(find_substring(S))    