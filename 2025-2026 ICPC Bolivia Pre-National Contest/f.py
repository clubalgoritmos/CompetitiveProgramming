import sys
import bisect

data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
la = [int(next(it)) for _ in range(n)]

prefix = []
suffix = sorted(la)

output = []

for i in range(n - 1):
    x = la[i]
    bisect.insort(prefix, x)
    pos = bisect.bisect_left(suffix, x)
    suffix.pop(pos)

    l = int(next(it))
    r = int(next(it))

    if l > len(prefix):
        sum_prefix = sum(prefix)
    else:
        sum_prefix = sum(prefix[-l:])

    if r > len(suffix):
        sum_suffix = sum(suffix)
    else:
        sum_suffix = sum(suffix[:r])

    output.append(str(sum_prefix - sum_suffix))

sys.stdout.write("\n".join(output))
