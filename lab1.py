from matplotlib import pyplot
import math

n = 500

x = []
x.append(0.65)
for i in range(1,n):
    x.append(3.8 * x[i - 1] * (1 - x[i - 1]))

a = range(0, n)

pyplot.plot(a,x)
pyplot.show()

x = [0.14]
s = [0]
for i in range(1, 10000):
    x.append(3.8 * x[i - 1] * (1 - x[i - 1]))
    if x[i] > 0.5:
        s.append(1)
    else:
        s.append(0)

    
prob = []
for nu in range(2, 10):
    prob_nu = []
    for i in range (0, 2**nu - 1):
        prob_nu.append(0.0)
        
    for j in range (1, 10000 / nu):
        sum = 0
        for i in range (0, nu - 1):
            sum += s[(j - 1) * nu + i] * 2**i
        prob_nu[sum] += 1.0
    prob.append(prob_nu)
    
for nu in range(2, 10):
    for i in range(0, 2**nu - 1):
        prob[nu - 2][i] /= (10000 / nu)

shenon_arr = []
r2_arr = []
r3_arr = []        
for nu in range(2, 10):
    shenon = 0.0
    r2 = 0.0
    r3 = 0.0
    for i in range(0, 2**nu - 1):
        if prob[nu - 2][i] > 0:
            shenon -= prob[nu - 2][i] * math.log(prob[nu - 2][i], 2)
            r2 += prob[nu - 2][i] **2;
            r3 += prob[nu - 2][i] **3;
    shenon_arr.append(shenon)
    r2_arr.append(- math.log(r2,2))
    r3_arr.append(- math.log(r3,2))
    
    print 'nu = ' + str(nu)
    print 'shenon: ' + str(shenon)
    print 'r2: ' + str( - math.log(r2, 2))
    print 'r3: ' + str( - math.log(r3, 2) / 2)
    
nurange = range(2, 10)

#pyplot.plot(nurange, shenon_arr)
#pyplot.plot(nurange, r2_arr)
#pyplot.plot(nurange, r3_arr)
#pyplot.show()