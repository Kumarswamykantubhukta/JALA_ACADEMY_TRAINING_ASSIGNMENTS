##install all packages
import numpy as np
import numpy.linalg as la


### Basic Array Operations:

# 1. Create a 3x3 array filled with random integers between 0 and 10. Calculate the sum, mean, and standard deviation of the array.
print("Questions 1 \n")
matrix1 = np.random.randint(0, 11, (3, 3))
print("Matrix 1:\n", matrix1)
print("Sum:", np.sum(matrix1))
print("Mean:", np.mean(matrix1))
print("Standard Deviation:", np.std(matrix1))

# 2. Create a 1D array of 10 elements and compute the cumulative sum of the elements.
print("Questions 2 \n")
array1 = np.arange(1, 11)
print("Array 1:", array1)
print("Cumulative Sum:", np.cumsum(array1))

# 3. Generate two 2x3 arrays with random integers and perform element-wise addition, subtraction, multiplication, and division.
print("Questions 3\n")
matrix2 = np.random.randint(1, 10, (2, 3))
matrix3 = np.random.randint(1, 10, (2, 3))
print("Matrix 2:\n", matrix2)
print("Matrix 3:\n", matrix3)
print("Addition:\n", matrix2 + matrix3)
print("Subtraction:\n", matrix2 - matrix3)
print("Multiplication:\n", matrix2 * matrix3)
print("Division:\n", matrix2 / matrix3)

# 4. Create a 4x4 identity matrix.
print("Questions 4 \n")
identity_matrix = np.eye(4)
print("Identity Matrix:\n", identity_matrix)

# 5. Given an array b = np.array([6, 12, 18, 24, 30]), divide each element by 6 using broadcasting.
print("Questions 5 \n")
array2 = np.array([6, 12, 18, 24, 30])
print("Array 2:", array2)
print("Array 2 / 6:", array2 / 6)

# Array Manipulation:

# 6. Reshape a 1D array of 12 elements into a 3x4 matrix.
print("Questions 6 \n")
array3 = np.arange(12)
print("Array 3:", array3)
print("Reshaped Array:\n", array3.reshape(3, 4))

# 7. Flatten a 3x3 matrix into a 1D array.
print("Questions 7 \n")
matrix4 = np.arange(9).reshape(3, 3)
print("Matrix 4:\n", matrix4)
print("Flattened Array:", matrix4.flatten())

# 8. Stack two 3x3 matrices horizontally and vertically.
print("Questions 8\n")
matrix5 = np.arange(9).reshape(3, 3)
matrix6 = np.arange(9, 18).reshape(3, 3)
print("Matrix 5:\n", matrix5)
print("Matrix 6:\n", matrix6)
print("Horizontal Stack:\n", np.hstack((matrix5, matrix6)))
print("Vertical Stack:\n", np.vstack((matrix5, matrix6)))

# 9. Concatenate two arrays of different sizes along a new axis.
print("Questions 9 \n")
matrix7 = np.arange(6).reshape(2, 3)
matrix8 = np.arange(8).reshape(2, 4)
print("Matrix 7:\n", matrix7)
print("Matrix 8:\n", matrix8)
try:
    print("Concatenate with new axis:\n", np.stack((matrix7, matrix8), axis=1))
except ValueError:
    print("Arrays must have the same shape to stack")

# 10. Transpose a 3x2 matrix and then reshape it to have 3 rows and 2 columns.
print("Questions 10 \n")
matrix9 = np.arange(6).reshape(3, 2)
print("Matrix 9:\n", matrix9)
print("Transposed and Reshaped:\n", matrix9.T.reshape(3, 2))

# Indexing and Slicing:

# 11. Given a 1D array of 15 elements, extract elements at positions 2 to 10 with a step of 2.
print("Questions 11 \n")
array4 = np.arange(15)
print("Array 4:", array4)
print("Sliced Array:", array4[2:11:2])

# 12. Create a 5x5 matrix and extract the sub-matrix containing elements from rows 1 to 3 and columns 2 to 4.
print("Questions 12 \n")
matrix10 = np.arange(25).reshape(5, 5)
print("Matrix 10:\n", matrix10)
print("Sub-matrix:\n", matrix10[1:4, 2:5])

# 13. Replace all elements in a 1D array greater than 10 with the value 10.
print("Questions 13 \n")
array5 = np.arange(15)
print("Array 5:", array5)
array5[array5 > 10] = 10
print("Modified Array:", array5)

# 14. Use fancy indexing to select elements from a 1D array at positions [0, 2, 4, 6].
print("Questions 14 \n")
array6 = np.arange(10)
print("Array 6:", array6)
print("Fancy Indexing:", array6[[0, 2, 4, 6]])

# 15. Create a 1D array of 10 elements and reverse it using slicing.
print("Questions 15 \n")
array7 = np.arange(10)
print("Array 7:", array7)
print("Reversed Array:", array7[::-1])

# Broadcasting:

# 16. Create a 3x3 matrix and add a 1x3 array to each row using broadcasting.
print("Questions 16 \n")
matrix11 = np.arange(9).reshape(3, 3)
array8 = np.array([1, 2, 3])
print("Matrix 11:\n", matrix11)
print("Array 8:", array8)
print("Broadcasted Addition:\n", matrix11 + array8)

# 17. Multiply a 1D array of 5 elements by a scalar value using broadcasting.
print("Questions 17 \n")
array9 = np.arange(5)
print("Array 9:", array9)
print("Broadcasted Multiplication:", array9 * 2)

# 18. Subtract a 3x1 column vector from a 3x3 matrix using broadcasting.
print("Questions 18 \n")
matrix12 = np.arange(9).reshape(3, 3)
array10 = np.array([1, 2, 3]).reshape(3, 1)
print("Matrix 12:\n", matrix12)
print("Array 10:\n", array10)
print("Broadcasted Subtraction:\n", matrix12 - array10)

# 19. Add a scalar to a 3D array and demonstrate how broadcasting works across all dimensions.
print("Questions 19 \n")
matrix13 = np.arange(8).reshape(2, 2, 2)
print("Matrix 13:\n", matrix13)
print("Broadcasted Scalar Addition:\n", matrix13 + 5)

# 20. Create two arrays of shapes (4, 1) and (1, 5) and add them using broadcasting.
print("Questions 20 \n")
matrix14 = np.arange(4).reshape(4, 1)
matrix15 = np.arange(5).reshape(1, 5)
print("Matrix 14:\n", matrix14)
print("Matrix 15:\n", matrix15)
print("Broadcasted Addition:\n", matrix14 + matrix15)

# Vectorized Operations:

# 21. Compute the square root of each element in a 2D array using vectorized operations.
print("Questions 21 \n")
matrix16 = np.arange(9).reshape(3, 3)
print("Matrix 16:\n", matrix16)
print("Square Root:\n", np.sqrt(matrix16))

# 22. Calculate the dot product of two 1D arrays of size 5.
print("Questions 22 \n")
array11 = np.arange(5)
array12 = np.arange(5, 10)
print("Array 11:", array11)
print("Array 12:", array12)
print("Dot Product:", np.dot(array11, array12))

# 23. Perform element-wise comparison of two 1D arrays and return an array of boolean values indicating where the first array has larger elements.
print("Questions 23 \n")
array13 = np.array([1, 5, 3, 7, 9])
array14 = np.array([2, 4, 4, 6, 8])
print("Array 13:", array13)
print("Array 14:", array14)
print("Element-wise Comparison (array13 > array14):", array13 > array14)

# 24. Create a 2D array and apply a vectorized operation to double the value of each element.
print("Questions 24 \n")
matrix17 = np.arange(9).reshape(3, 3)
print("Matrix 17:\n", matrix17)
print("Doubled Array:\n", matrix17 * 2)

# 25. Create a 1D array of 100 random integers and compute the sum of all even numbers using vectorized operations.
print("Questions 25 \n")
array15 = np.random.randint(0, 100, 100)
print("Array 15:", array15)
even_numbers = array15[array15 % 2 == 0]
print("Sum of Even Numbers:", np.sum(even_numbers))

# Linear Algebra:

# 26. Create a 3x3 matrix and find its determinant.
print("Questions 26 \n")
matrix18 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix 18:\n", matrix18)
print("Determinant:", la.det(matrix18))

# 27. Given a 2x2 matrix, compute its inverse and verify by multiplying with the original matrix to obtain the identity matrix.
print("Questions 27 \n")
matrix19 = np.array([[1, 2], [3, 4]])
print("Matrix 19:\n", matrix19)
inverse_matrix19 = la.inv(matrix19)
print("Inverse:\n", inverse_matrix19)
print("Verification (matrix19 * inverse_matrix19):\n", np.dot(matrix19, inverse_matrix19))

# 28. Calculate the eigenvalues and eigenvectors of a 2x2 matrix.
print("Questions 28 \n")
matrix20 = np.array([[1, 2], [2, 1]])
print("Matrix 20:\n", matrix20)
eigenvalues, eigenvectors = la.eig(matrix20)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# 29. Solve the system of linear equations 2x + 3y = 5 and 4x + 6y = 10 using NumPy.
print("Questions 29 \n")
matrix21 = np.array([[2, 3], [4, 6]])
array16 = np.array([5, 10])
try:
    solution = la.solve(matrix21, array16)
    print("Solution:", solution)
except la.LinAlgError:
    print("The system of linear equations is singular or ill-conditioned.")

# 30. Perform Singular Value Decomposition (SVD) on a 3x3 matrix and reconstruct the original matrix using the SVD components.
print("Questions 30 \n")
matrix22 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix 22:\n", matrix22)
U, S, V = la.svd(matrix22)
print("U:\n", U)
print("S:", S)
print("V:\n", V)
S_matrix = np.zeros(matrix22.shape)
S_matrix[:len(S), :len(S)] = np.diag(S)
reconstructed_matrix22 = U @ S_matrix @ V
print("Reconstructed Matrix:\n", reconstructed_matrix22)