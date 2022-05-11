def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	
	if len(matrix) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	result = 0
	for i in range(len(matrix)):
		result += matrix[0][i] * determinant(get_minor(matrix, 0, i)) * (-1) ** i

	return result
	

def get_minor(matrix, i, j):
	minor = []
	for n in range(len(matrix)):
		if n == i: continue
		minor.append(matrix[n][:j] + matrix[n][j + 1:])
	return minor
