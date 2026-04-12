import sys

def better(x, y):
    if x[1] > y[1]:
        return True
    elif x[1] < y[1]:
        return False
    else:
        return x[0] < y[0]

data = sys.stdin.read().split()
N = int(data[0])
candidates = []
index = 1
for i in range(N):
    s = data[index]
    a = int(data[index+1])
    index += 2
    candidates.append((s, a))

champ = candidates[0]
champ_losers = []

for candidate in candidates[1:]:
    if better(champ, candidate):
        champ_losers.append(candidate)
    else:
        champ_losers.append(champ)
        champ = candidate

runner_up = champ_losers[0]
for candidate in champ_losers[1:]:
    if better(candidate, runner_up):
        runner_up = candidate

sys.stdout.write(champ[0] + "\n")
sys.stdout.write(runner_up[0])
