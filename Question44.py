import numpy
import math
import unittest
import sympy

# use the quadrature points to evaluate the quadrature 
def riemannQuadrature(fun,num_points):
    x,w = getRiemannQuadrature([-1,1],num_points) # calling the defined function for use in this function
    # this tells me where the locations of the x points are on the interval [-1,1]
    area = 0
    for j in range(num_points):
       area += w*fun(x[j]) #not correct python syntax but the idea is good
    return area

# get quadrature points on the domain
def getRiemannQuadrature(domain,num_points):
    qp = numpy.zeros(num_points)
    deltax = (domain[1]-domain[0])/num_points
    for i in range(num_points):
        if i != 0:
            qp[i] = qp[i-1] + deltax
        else:
            qp[i] = domain[0] + deltax/2
    w = deltax
    return qp,w

# testing template
class Test_getRiemannQuadrature( unittest.TestCase ):
    def test_biunit_4point( self ):
        qp,w = getRiemannQuadrature([-1,1],4) # write test and print 
        qp_gold = [-.75,-.25,.25,.75]
        w_gold = .5
        self.assertAlmostEqual( first = w, second = w_gold, delta = 1e-12 )
        self.assertTrue(numpy.allclose(qp,qp_gold))

class Test_computeRiemannQuadrature( unittest.TestCase ):
    def test_integrate_constant_one( self ):
        constant_one = lambda x : 1
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = constant_one, num_points = num_points ), second = 2.0, delta = 1e-12 )

    def test_integrate_linear( self ):
        linear = lambda x : x
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = linear, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_quadratic( self ):
        linear = lambda x : x**2
        error = []
        for num_points in range( 1, 100 ):
            error.append( abs( (2.0 / 3.0) - riemannQuadrature( fun = linear, num_points = num_points ) ) )
        self.assertTrue( numpy.all( numpy.diff( error ) <= 0.0 ) )

    def test_integrate_sin( self ):
        sin = lambda x : math.sin(x)
        error = []
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = sin, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_cos( self ):
        cos = lambda x : math.cos(x)
        error = []
        for num_points in range( 1, 100 ):
            error.append( abs( (2.0 / 3.0) - riemannQuadrature( fun = cos, num_points = num_points ) ) )
        self.assertTrue( numpy.all( numpy.diff( error ) <= 0.0 ) )
