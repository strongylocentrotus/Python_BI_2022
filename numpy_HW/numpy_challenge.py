import numpy as np

if __name__ == "__main__":
    first = np.array([4, 7, 9])
    second = np.ones((12, 11))
    third = np.zeros(14, dtype=int)


def matrix_multiplication(matrix_a: np.ndarray, matrix_b: np.ndarray):
    return np.matmul(matrix_a, matrix_b)


def multiplication_check(matrices_list: list):
    for i in range(len(matrices_list) - 1):
        one = matrices_list[i]
        two = matrices_list[i + 1]
        if one.shape[1] != two.shape[0]:
            return False
    return True


def multiply_matrices(matrices_list: list):
    try:
        if len(matrices_list) == 1:
            return matrices_list[0]
        return np.dot(multiply_matrices(matrices_list[:-1]), matrices_list[-1])
    except ValueError:
        return None


def compute_multidimensional_distance(matrix_a, matrix_b):
    return np.sqrt(np.sum(np.square(matrix_a - matrix_b)))


def compute_2d_distance(matrix_a: np.ndarray, matrix_b: np.ndarray):
    return compute_multidimensional_distance(matrix_a, matrix_b)


def compute_pair_distances(d2_array: np.ndarray):
        its_shape = d2_array.reshape(d2_array.shape[0], 1, d2_array.shape[1])
        fin_mat = np.sqrt(np.einsum("ijk,ijk->ij", d2_array - its_shape, d2_array - its_shape))
        return fin_mat


