def max_score(n, m, scores):
    max_score = float('-inf')
    
    for start in range(n):
        for end in range(start, min(start + m + 1, n)):
            score = scores[end] - scores[start]
            if score > max_score:
                max_score = score
    
    return max_score

n,m = map(int,input().split())
scores = list(map(int,input().split()))
print(max_score(n, m, scores))