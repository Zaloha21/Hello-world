import cmath, math
import matplotlib.pyplot as mp
import numpy as np
from matplotlib.patches import Polygon
from scipy.integrate import quad


def average(std_dev,average_number,l,r):


    x = np.linspace(average_number - std_dev, average_number + std_dev )
    y = 1/(math.sqrt(2*math.pi*std_dev **2))*math.e**(-1*(x - average_number)**2)/(2*(std_dev**2)) #normCD function


    mp.axhline(0, color="k" , linewidth = 0.1)
    mp.plot(x,y)                                                        #normCD dev V-window



    fig, ax = mp.subplots()                                             #Integral AREA PLOT
    mp.plot(x, y, 'r', linewidth=2)
    mp.ylim(bottom=0)


    ix = np.linspace(l, r)
    iy = 1/(math.sqrt(2*math.pi*std_dev **2))*math.e**(-1*(ix - average_number)**2)/(2*(std_dev**2))    #INTEGRAL AREA PLOT (credits to:https: //matplotlib.org/gallery/showcase/integral.html)
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

std_dev,average_number = input("Enter standard deviation and mean as a,b: ").split(',')    #list filter
l,r = input('Linkergrens, Rechtergrens: ').split(',')
average(int(std_dev),int(average_number),int(l),int(r))
