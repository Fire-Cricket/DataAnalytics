import numpy as np
'''
arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([[1,2,3,4,5], [6, 7, 8, 9, 10]]) #Will crash if uneven

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"Checking the shape {arr1.shape} and dimension {arr1.ndim}")
print()

print(f"Checking the shape {arr2.shape} and dimension {arr2.ndim}")
print()

print(f"Checking the shape {arr3.shape} and dimension {arr3.ndim}")
'''

arrA = np.array([[11, 12, 13], [14, 15, 16]])

print(arrA)
print()

for row1 in arrA: 
    loop_result = row1 * 2 
    print(loop_result)       
 #   for row2 in row1:        
  #      loop_result = row2 * 2
   #     print(loop_result)