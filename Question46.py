import numpy
import math
import unittest
import sympy

def computeNewtonCotesQuadrature(fun,num_points):
    
    x, w = getNewtonCotesQuadrature([-1,1],num_points)
    area = 0
    for j in range(num_points):
        area += w[j] * fun(x[j])
    return area

def getNewtonCotesQuadrature(domain,num_points):
    qp = numpy.zeros(num_points)
    integral = numpy.zeros(num_points)
    if num_points == 1:
        qp = [0]
        integral = [2]
    if num_points == 2:
        qp = [-1,1]
        integral = [1,1]
    if num_points == 3:
        qp = [-1,0,1]
        integral = [1/3,4/3,1/3]
    if num_points == 4:
        qp = [-1,-1/3,1/3,1]
        integral = [1/4,3/4,3/4,1/4]
    if num_points == 5:
        qp = [-1,-1/2,0,1/2,1]
        integral = [7/45,32/45,4/15,32/45,7/45]
    if num_points == 6:
        qp = [-1,-3/5,-1/5,1/5,3/5,1]
        integral = [19/144,25/48,25/72,25/72,25/48,19/144]
    if num_points == 7:
        qp = [-1,-2/3,-1/3,0,1/3,2/3,1]
        integral = [41/420,18/35,9/140,68/105,9/140,18/35,41/420]
    if num_points == 8:
        qp = [-1,-5/7,-3/7,-1/7,1/7,3/7,5/7,1]
        integral = [751/8640,.41400462963,49/320,.345949074074,.345949074074,49/320,.41400462963,751/8640]
    #print(num_points)
    #print(deltax)
    #print(qp)
    return qp, integral

# testing template
#class Test_computeNewtonCotesQuadrature( unittest.TestCase ):
#    def test_biunit_4point( self ):
#        qp,w = computeNewtonCotesQuadrature([-1,1],4) # write test and print 
#        qp_gold = [-.75,-.25,.25,.75]
#        w_gold = .5
#        self.assertAlmostEqual( first = w, second = w_gold, delta = 1e-12 )
#        self.assertTrue(numpy.allclose(qp,qp_gold))

class Test_computeNewtonCotesQuadrature( unittest.TestCase ):
    def test_integrate_constant_one( self ):
        constant_one = lambda x : 1 * x**0
        for degree in range( 1, 6 ):
            num_points = degree + 1
            self.assertAlmostEqual( first = computeNewtonCotesQuadrature( fun = constant_one, num_points = num_points ), second = 2.0, delta = 1e-12 )

    def test_exact_poly_int( self ):
        for degree in range( 1, 6 ):
            num_points = degree + 1
            poly_fun = lambda x : ( x + 1.0 ) ** degree
            indef_int = lambda x : ( ( x + 1 ) ** ( degree + 1) ) / ( degree + 1 )
            def_int = indef_int(1.0) - indef_int(-1.0)
            self.assertAlmostEqual( first = computeNewtonCotesQuadrature( fun = poly_fun, num_points = num_points ), second = def_int, delta = 1e-12 )

    def test_integrate_sin( self ):
        sin = lambda x : math.sin(x)
        for num_points in range( 1, 7 ):
            self.assertAlmostEqual( first = computeNewtonCotesQuadrature( fun = sin, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_cos( self ):
        cos = lambda x : math.cos(x)
        self.assertAlmostEqual( first = computeNewtonCotesQuadrature( fun = cos, num_points = 6 ), second = 2*math.sin(1), delta = 1e-4 )
