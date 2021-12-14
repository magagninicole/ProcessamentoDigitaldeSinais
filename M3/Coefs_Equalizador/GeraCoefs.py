import numpy 

with open('Coef_PB.dat', 'r') as f:
    coefs_PB = [line.strip().replace(',', '') for line in f]

coefs_short_PB = numpy.zeros(len(coefs_PB))
for i in range(len(coefs_PB)):
    coefs_short_PB[i] = int(float(coefs_PB[i]) * 32768)

with open("coefs_short_PB.dat", "w") as f:
    for s in coefs_short_PB:
        f.write(str(s) +",\n")

with open('Coef_PF.dat', 'r') as f:
    coefs_PF = [line.strip().replace(',', '') for line in f]

coefs_short_PF = numpy.zeros(len(coefs_PF))
for i in range(len(coefs_PF)):
    coefs_short_PF[i] = int(float(coefs_PF[i]) * 32768)

with open("coefs_short_PF.dat", "w") as f:
    for s in coefs_short_PF:
        f.write(str(s) +",\n")
        
with open('Coef_PA.dat', 'r') as f:
    coefs_PA = [line.strip().replace(',', '') for line in f]

coefs_short_PA = numpy.zeros(len(coefs_PA))
for i in range(len(coefs_PA)):
    coefs_short_PA[i] = int(float(coefs_PA[i]) * 32768)

with open("coefs_short_PA.dat", "w") as f:
    for s in coefs_short_PA:
        f.write(str(s) +",\n")