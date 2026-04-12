import math, random

with open("C.in", "w") as f:
    A = random.randint(1, 5)
    C = random.randint(1, 5)
    S = random.randint(1, 5)
    
    f.write( str(A) + " " + str(C) + " " + str(S) + "\n" )
    f.write( str( math.factorial( (A + C) * S ) + 100 ) + "\n" )

R = math.factorial( (A + C) * S ) + 100

with open("C.out", "w") as f:
    f.write( str(R) + "\n" )
