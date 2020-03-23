import unittest
from Sorter import Sorter

class TestSorter(unittest.TestCase):
	def setUp(self):
		self.test_reverse_false=Sorter(reverse=False)
		self.test_reverse_true=Sorter(reverse=True)

	#Test if reverse works
	def test_reverse_false(self):
		x=[5,4,3,2,1]
		self.test_reverse_false.mergeSort(x)
		self.assertEqual(x,[1,2,3,4,5])

	#Test if non-reverse works
	def test_reverse_true(self):
		x=[1,2,3,4,5]
		self.test_reverse_true.mergeSort(x)
		self.assertEqual(x,[5,4,3,2,1])

	# Test negative values for reverse
	def test_all_negative_reverse_false(self):
		x=[-1,-2,-3,-4,-5]
		self.test_reverse_false.mergeSort(x)
		self.assertEqual(x,[-5,-4,-3,-2,-1])

	#Test negative values for non-reverse works
	def test_all_negative_reverse_true(self):
		x=[-5,-4,-3,-2,-1]
		self.test_reverse_true.mergeSort(x)
		self.assertEqual(x,[-1,-2,-3,-4,-5])

	#Test if empty set works with reverse 
	def test_reverse_false_empty(self):
		x=[]
		self.test_reverse_false.mergeSort(x)
		self.assertEqual(x,[])
	
	#Test if empty set works with non-reverse 
	def test_reverse_true_empty(self):
		x=[]
		self.test_reverse_true.mergeSort(x)
		self.assertEqual(x,[])

