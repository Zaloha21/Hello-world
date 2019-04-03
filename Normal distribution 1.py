import cmath, math
import matplotlib.pyplot as mp
import numpy as np
from matplotlib.patches import Polygon
from scipy.integrate import quad


def average(number,l,r):
    __list = number

    sum_number = 0

    for i in range(len(__list)):                                        #average
        sum_number += __list[i]
    average_number = sum_number / len(__list)

    dev_sum_number_squared = 0

    for i in range(len(__list)):
        dev_sum_number_squared += (__list[i] - average_number)**2       #st_dev
    std_dev = math.sqrt(dev_sum_number_squared / len(__list))
    print("The average is: " + str(average_number) + " and the standard deviation is: " + str(std_dev) + '.')

    x = np.linspace(average_number - std_dev, average_number + std_dev )
    y = 1/(math.sqrt(2*math.pi*std_dev **2))*math.e**(-1*(x - average_number)**2)/(2*(std_dev**2)) #normCD function


    mp.axhline(0, color="k" , linewidth = 0.1)
    mp.plot(x,y)                                                        #normCD dev V-window



    fig, ax = mp.subplots()                                             #Integral AREA PLOT (credits to:https: //matplotlib.org/gallery/showcase/integral.html)
    mp.plot(x, y, 'r', linewidth=2)
    mp.ylim(bottom=0)


    ix = np.linspace(l, r)
    iy = 1/(math.sqrt(2*math.pi*std_dev **2))*math.e**(-1*(ix - average_number)**2)/(2*(std_dev**2))    #INTEGRAL AREA PLOT
    verts = [(l, 0), *zip(ix, iy), (r, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    mp.text(0.5 * (l + r), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)

    mp.figtext(0.9, 0.05, '$x$')
    mp.figtext(0.1, 0.9, '$y$')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticks((l, r))
    ax.set_xticklabels((l, r))
    ax.set_yticks([])


    sigma = std_dev                                                                                     #New def of standard deviation for integrated value
    mu = average_number                                                                                 #New def of average number for integrated value
    def integrand(z,sigma,mu):
        return 1/(math.sqrt(2*math.pi*sigma **2))*math.e**(-1*(z - mu)**2/(2*(sigma**2)))

    A = quad(integrand, l, r, args= (sigma, mu))                                                        #Definite Integral
    print('The chance between ' + str(l) + ' and ' + str(r) + ' with inaccuracy ' + ' is' + str(A))

    mp.show()

number = [float(x) for x in input('Insert data with commas in between:  ').split(',')]      #list filter
l,r = input('Linkergrens, Rechtergrens: ').split(',')
average(number,int(l),int(r))
