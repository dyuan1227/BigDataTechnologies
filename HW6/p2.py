import math
import numpy as np
from mrjob.job import MRJob
from mrjob.step import MRStep


class pi_estimate(MRJob):

	def steps(self):

	    return [ MRStep(mapper = self.rdm_pt_gen, reducer = self.inside_circle),
	             MRStep(reducer = self.pi_value)]

	# Mapper to produce N samples
	def rdm_pt_gen(self, _ , N):  

	    N = int(N)
	    
	    #Produce N/2 samples each in x-axis and y-axis
	    #Generate uniform random samples 
	    x = np.random.uniform(-1,1,int(N/2))   
	    y = np.random.uniform(-1,1,int(N/2))
	    
	    points = list(zip(x,y))
	    for j in range(len(points)):
	        yield "Point" + str(j+1), points[j]    
	    
	# Classify whether the point lies inside or outside the circle
	def inside_circle(self, key, values):

	    point = next(values)
	    x = point[0]
	    y = point[1]
	    z = (np.sqrt(x**2 + y**2) <= 1)
	    indicator = int(z)
	    yield None, indicator

	# Estimate the value of pi
	def pi_value(self, _ , indicator):

	    indicator = list(indicator)
	    
	    #Sum the points in the circle
	    sum_indicator = 0
	    
	    for element in indicator:
	        sum_indicator = sum_indicator + int(element)
	        
	    pi = 4*sum_indicator/len(indicator)
	    yield None, pi


if __name__ == '__main__':
    pi_estimate.run()