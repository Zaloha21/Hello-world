import cmath, math
import matplotlib.pyplot as mp
import numpy as np

while True:
    def oplossingen(a,b,c):
        D = b**2 -4*a*c
        if D >0:
            print('This formula has 2 real solutions')                              #Calculating D for D>0
            solution1 = (-1*b + (math.sqrt(D)))/(2*a)
            solution2 = (-1*b - (math.sqrt(D)))/(2*a)
            print('These are '+ str(solution1) +' and '+ str(solution2) +'.')
            x = np.linspace(-10+int(solution1),10+int(solution2))                   #Domain Plot
            y = a*x**2 + b*x +c
            mp.plot(x,y)
            mp.axhline(0, color ='black')                                           #Axes
            mp.axvline(0, color ='black')
            mp.grid(color='grey', linestyle='-', linewidth=0.1)                     #Grid
            mp.show()
        if D == 0:
            print('This formula has 1 real solution')
            x1= (-1*b)/(2*a)                                                        #Maximum Solution
            print('This is ' + str(x1) + '.')
            x = np.linspace(-10+int(x1),10+int(x1))                                 #Domain root
            y = a*x**2 + b*x +c
            mp.plot(x,y)
            mp.axhline(0, color ='black')
            mp.axvline(0, color ='black')
            mp.grid(color='grey', linestyle='-', linewidth=0.1)
            mp.show()
        if D <0:
            print('This formula has 2 complex solutions')
            xc1 = (-1*b + cmath.sqrt(D))/(2*a)
            xc2 = (-1*b - cmath.sqrt(D))/(2*a)                                      #Complex solution
            print('These are ' + str(xc1)+ 'and '+ str(xc2) +'.')
            x = np.linspace(-10+int((xc1).real),10+int((xc2).real))                 #Domain real part of complex solution
            y = a*x**2 + b*x +c
            mp.plot(x,y)
            mp.axhline(0, color ='black')
            mp.axvline(0, color ='black')
            mp.grid(color='grey', linestyle='-', linewidth=0.1)
            mp.show()


    a,b,c = input('Voer hier ax^2 + bx + c in als a,b,c: ').split(",")
    oplossingen(int(a),int(b),int(c))
    print('\n')
    continue

