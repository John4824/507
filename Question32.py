
import sympy
import numpy
import math
import matplotlib.pyplot as plt


# define function here
def taylorExpansion( fun, a, order ): 
    x = list( fun.atoms( sympy.Symbol ) )[0] 
    t = 0
    for i in range( 0, order + 1 ):
       df = sympy.diff( fun, x, i )
       term = ( df.subs( x, a ) / sympy.factorial( i ) ) * ( x - a )**i
       t += term # t = t + term
    return t

# test predefined function here
order = 10
x = sympy.Symbol("x") # defining the symbol letter variable
f = sympy.erfc(x) # defining a function of the predefined letter variable
t = taylorExpansion(f,0,order) # use the predefined function to get a taylorExpansion of this function at this point to this order
print(f) # display function
print(t) # display taylor series

#int = sympy.integrate(f - t , (x,-1,1))
#print(int)

# Define variables for graphing here
x = sympy.symbols('x')
fun = sympy.sin(math.pi*x)
t = taylorExpansion(fun,0,order)
# define and create arrays for graphing here
N = 1000
px = numpy.linspace(-1,1,N) # array of 1000 points from -1 to 1
py = numpy.zeros(N) # empty or zeros array length N
fy = numpy.zeros(N) # empty or zeros array length N
for i in range(0,N):
    fy[i] = fun.subs(x,px[i])
    py[i] = t.subs(x,px[i])
# plotting details here
#fig, ax = plt.subplots()
#ax.plot(px,fy,linewidth = 2.0)
#ax.plot(px,py,linewidth=2.0)
#plt.title('Order 1')
#plt.show()
