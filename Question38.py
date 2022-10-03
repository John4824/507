import unittest
import numpy

def evaluateLagrangeBasis1D(variate,degree,basis_idx):
    node = numpy.linspace(-1,1,degree+1)
    val = 1
    for j in range(0,degree+1):
        if j != basis_idx:
            val = val * ((variate - node[j])/(node[basis_idx]-node[j]))
    return val

class Test_evaluateLagrangeBasis1D( unittest.TestCase ):
    def test_linearLagrange( self ):
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = -1, degree = 1, basis_idx = 0 ), second = 1.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = -1, degree = 1, basis_idx = 1 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = +1, degree = 1, basis_idx = 0 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = +1, degree = 1, basis_idx = 1 ), second = 1.0, delta = 1e-12 )

    def test_quadraticLagrange( self ):
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = -1, degree = 2, basis_idx = 0 ), second = 1.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = -1, degree = 2, basis_idx = 1 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = -1, degree = 2, basis_idx = 2 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate =  0, degree = 2, basis_idx = 0 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate =  0, degree = 2, basis_idx = 1 ), second = 1.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate =  0, degree = 2, basis_idx = 2 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = +1, degree = 2, basis_idx = 0 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = +1, degree = 2, basis_idx = 1 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateLagrangeBasis1D( variate = +1, degree = 2, basis_idx = 2 ), second = 1.0, delta = 1e-12 )
