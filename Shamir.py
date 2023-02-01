import random

# варіант 20
fopen = open('INPUTSHAMIR.txt','r')
p = int(fopen.readline())
qa = int(fopen.readline())
qb = int(fopen.readline())
fopen.close

M = int(input('Enter message: '))

ka = random.randint(1, 100)
while ((ka * qa) % (p - 1) != 1):
    ka = random.randint(1, 100)
kb = random.randint(1, 100)
while ((kb * qb) % (p - 1)!=1):
    kb = random.randint(1, 100)

Ya = (M ** ka) % p
Yb = (Ya ** kb) % p
C = (Yb ** qa) % p
M = (C ** qb) % p

wf = open('output_Shamir.txt','w', encoding='utf-8')
wf.write("ka: " + str(ka))
wf.write("\nkb: " + str(kb))
wf.write("\nYa: " + str(Ya))
wf.write("\nYb: " + str(Yb))
wf.write("\nC: " + str(C))
wf.write("\nM: " + str(M))
wf.close