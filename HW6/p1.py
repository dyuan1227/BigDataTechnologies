import threading
import time
import math
import matplotlib.pyplot as plt



lock=threading.Lock() #lock


def worker(k):
	global result
	result.append(4*((-1)**k)/(2*k+1))

def sum_worker(p):
	global temp_result
	lock.acquire()
	temp_result.append(sum(result[p:p+2]))
	lock.release()

def compute_pi(N,concurrent):
	start=time.time()
	result_seq=0
	if concurrent==False:
		for k in range(N):
			result_seq+=4*((-1)**k)/(2*k+1)
		end=time.time()
		running_time=end-start
		return result_seq, running_time
	else:
		global temp_result, result

		result=[]
		threads=[]

		for k in range(N):
			w=threading.Thread(target=worker, args=(k,))
			w.start()
			threads.append(w)

		for w in threads:
			w.join()

		while len(result) > 1:
			temp_result=[]
			sum_threads = []
			num_thread =math.ceil(len(result)/2)
			
			for i in range(num_thread):
				w=threading.Thread(target=sum_worker, args=(2*i,))
				w.start()
				sum_threads.append(w)
			
			for w in sum_threads:
				w.join()

			result=temp_result.copy()
			
			del temp_result
			del sum_threads

		end2=time.time()
		elapse = end2-start
		result_para=result[0]

	return result_para, elapse



#Plot
ns=[2**i for i in range(4,11)]
concurrent_running_times=[]
sequential_running_times=[]
for i in range(0,len(ns)):
	concurrent_running_times.append(compute_pi(ns[i],True)[1])

for i in range(0,len(ns)):
	sequential_running_times.append(compute_pi(ns[i],False)[1])

plt.plot(ns,sequential_running_times, label ="Sequential")
plt.plot(ns,concurrent_running_times, label ="Concurrent")

plt.xlabel('N')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()