# Problem 1

Like professor mentioned in class. Concurrent is not working properly in Python. Therefore, the concurrent graph increases in time when N takes larger values. Creating threads are taking time. In this case, the sequential case is running faster than the concurrent way.

There are three main functions:
- worker: append the sum to the result list
- sum_worker: sum every two elements and append to the list
- compute_pi: divide the cases into concurrent and sequential.

To run the file, simply run: python3 p1.py

# Problem 2

We have functions as described below
- steps: mapper and reducer
- rdm_pt_gen: random point generator for 1/4 of a circle
- inside_circle: decide whether the generated point is in the circle
- pi_value: calculate the value of the pi by counting how many points are in the circle divided by all points

To check the result, simply run: echo 1000 | python3 p2.py





