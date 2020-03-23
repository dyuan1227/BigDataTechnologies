class Sorter:
	def __init__(self, reverse=False):
		self.reverse=reverse

	def mergeSort(self,arr):
	 	sub_size=1
	 	while sub_size < len(arr):
	 		#Initilizing the left postition,right_size and left_size
	 		left=0
	 		right_size=0
	 		left_size=0

	 		while left < len(arr):

	 			#Checking if it is out of range
	 			if left + sub_size*2 -1 > len(arr)-1:


	 				if len(arr)-left < sub_size:
	 					left_size=len(arr)-left
	 					right = 0
	 					right_size = 0
	 				else:
	 					left_size = sub_size
	 					right = left + sub_size
	 					right_size = len(arr)-right
	 			#If not, updating the right, right_size, left_size
	 			else:
	 				right = left + sub_size
	 				right_size = sub_size
	 				left_size = sub_size
	 			
	 			#Initilizing the two arrays
	 			R_arr=[0]*right_size
	 			L_arr=[0]*left_size

	 			#filling left and right arrays
	 			for i in range(left_size):
	 				L_arr[i]=arr[left+i]
	 			for j in range(right_size):
	 				R_arr[j]=arr[right+j]

	 			i, j, k = 0, 0, left

	 			#Checking whether reverse is true
	 			if self.reverse==False:
	 				while i < left_size and j < right_size:
	 					if L_arr[i] < R_arr[j]:
	 						arr[k]=L_arr[i]
	 						i+=1
	 					else:
	 						arr[k]=R_arr[j]
	 						j+=1
	 					k+=1
	 			else:
	 				while i < left_size and j < right_size:
	 					if L_arr[i] > R_arr[j]:
	 						arr[k]=L_arr[i]
	 						i+=1
	 					else:
	 						arr[k]=R_arr[j]
	 						j+=1
	 					k+=1
	 			#Dealing with the array with more elements
	 			while i < left_size:
	 				arr[k]=L_arr[i]
	 				i+=1
	 				k+=1
	 			while j < right_size:
	 				arr[k]=R_arr[j]
	 				j+=1
	 				k+=1

	 			#Increasing left to the position that double the sub_size
	 			left = left + 2 * sub_size
	 		
	 		#Increading the sub_size by 2
	 		sub_size = sub_size * 2

            