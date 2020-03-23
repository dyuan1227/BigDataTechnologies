#For problem 1, I have a Sorter.py file that contains a class called Sorter. It constructs two functions including a setup function and a mergesort function that will reverse the input list when self.reverse=True.

In the TestSorter.py file, I am testing 6 cases.
1. test_reverse_false  				(testing when positive values when reverse=false)
2. test_reverse_true   				(testing when postitive value when reverse=true)
3. test_all_negative_reverse_false  (testing when negative values when reverse=false)
4. test_all_negative_reverse_true   (testing when negative value when reverse=true)
5. test_reverse_false_empty 		(testing when empty list when reverse=false)
6. test_reverse_true_empty  		(testing when empty list when reverse=true)


Run the tests for problem1, using the following command:
python3 -m nose TestSorter.py



#For problem 2,
The TestGetBinaryRepresentation.py have five test to test
1. when the input is 0
2. when the input is 2     (when the input is a positive integer)
3. when the input is 1.1   (when the input is a positive demical)
4. when the input is -1	   (when the input is a negative integer)
5. when the input is -1.1  (when the input is a negative decimal)

Run the tests for problem2, using the following command:
python3 -m nose TestGetBinaryRepresentation.py


#For problem 3,


Run the tests for problem 3, using the following command:
python3 -m unittest TestQesolution.py

It includes 8 tests:
- 4 for qesolution
 * when b and c are relative close; testing for 2b
 * when b and c are relative close; testing for -c
 * when b is relatively large and c is; testing for 2b (rootsum)   * Test Fail 
 * when b is relatively large and c is; testing for -c (rootproduct)
- 4 for qesolutionRevise.
 * when b and c are relative close; testing for 2b
 * when b and c are relative close; testing for -c 
 * when b is relatively large and c is; testing for 2b (rootsum)   * Will not fail any more
 * when b is relatively large and c is; testing for -c (rootproduct) 


Problem 3.2
When b is large in magnitude compare to c, the calculation -b+sqrt(b^2+c) will suffer from catastrophic cancellation because this is the sum of two large positive numbers. The same is true for two negative values. The relative error will increase due to this. In the fourth test, when b=2147483647, c=0.00000001, we can see that the relative error is higher than 10^(-12).


For Problem 3.3, qesolutionRevise.py is here to solve the catastrophic cancellation. We could add two large numbers with the same sign, and then compute the other solution using x1\*x2 = -c. In the code, we can see that if b>=0, r1 = (2\*b + np.sqrt(y))/2   and  r2 = -2\*c/(2\*b+np.sqrt(y))
and  if b<0 , r1 = (2\*b - np.sqrt(y))/2   and  r2 = -2\*c/(2\*b-np.sqrt(y))
As we can see from the last for tests, the relative error is now below 10^(-12).
