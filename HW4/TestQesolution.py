from qesolution import qesolution
from qesolutionRevise import qesolutionRevise
import unittest


class TestQesolution(unittest.TestCase):
    
    ###########################
    ####Test for qesolution####
    ########################### 

    #Test pass for normal b and c ; 2b
    def test_case_1(self):
        b=10
        c=12
        accuracy=10**-12
        r1,r2 = qesolution(b,c)
        rootsum=r1+r2
        two_b=2*b
        relative_err_sum = (rootsum - two_b)/two_b
        self.assertTrue(abs(relative_err_sum)<accuracy)

    #Test pass for normal b and c ; -c
    def test_case_2(self):
        b=10
        c=12
        accuracy=10**-12
        r1,r2 = qesolution(b,c)
        rootproduct=r1*r2
        neg_c=(-1)*c
        relative_err_product = (rootproduct - neg_c)/neg_c
        self.assertTrue(abs(relative_err_product)<accuracy)

    #Test pass for large b and small c
    def test_case_3(self):
        b=2147483647
        c=0.00000001
        accuracy=10**-12
        r1,r2 = qesolution(b,c)
        rootsum=r1+r2
        two_b=2*b
        relative_err_sum = (rootsum - two_b)/two_b
        self.assertTrue(abs(relative_err_sum)<accuracy)

    #Test don't pass for large b and small c
    def test_case_4(self):
        b=2147483647
        c=0.00000001
        accuracy=10**-12
        r1,r2 = qesolution(b,c)
        rootproduct=r1*r2
        neg_c=(-1)*c
        relative_err_product = (rootproduct - neg_c)/neg_c
        self.assertTrue(abs(relative_err_product)<accuracy)

    
    ###########################
    #Test for qesolutionRevise#
    ###########################

    #Test pass for normal b and c ; 2b
    def test_case_5(self):
        b=10
        c=12
        accuracy=10**-12
        r1,r2 = qesolutionRevise(b,c)
        rootsum=r1+r2
        two_b=2*b
        relative_err_sum = (rootsum - two_b)/two_b
        self.assertTrue(abs(relative_err_sum)<accuracy)


    #Test pass for normal b and c ; -c
    def test_case_6(self):
        b=10
        c=12
        accuracy=10**-12
        r1,r2 = qesolutionRevise(b,c)
        rootproduct=r1*r2
        neg_c=(-1)*c
        relative_err_sum = (rootproduct - neg_c)/neg_c
        self.assertTrue(abs(relative_err_sum)<accuracy)


    #Test pass for large b and small c ; 2b
    def test_case_7(self):
        b=2147483647
        c=0.00000001
        accuracy=10**-12
        r1,r2 = qesolutionRevise(b,c)
        rootsum=r1+r2
        two_b=2*b
        relative_err_sum = (rootsum - two_b)/two_b
        self.assertTrue(abs(relative_err_sum)<accuracy)

    #Test pass for large b and small c ; -c
    def test_case_8(self):
        b=2147483647
        c=0.00000001
        accuracy=10**-12
        r1,r2 = qesolutionRevise(b,c)
        rootproduct=r1*r2
        neg_c=(-1)*c
        relative_err_sum = (rootproduct - neg_c)/neg_c
        self.assertTrue(abs(relative_err_sum)<accuracy)
        
        
   