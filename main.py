from csv_writer import CSVWriter
from typing import List, Tuple


def polynomial_multiplication(
    poly1: List[int], poly2: List[int], mod: int = 17
) -> List[int]:
    """Multiply two polynomials in modulo arithmetic."""
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] = (result[i + j] + poly1[i] * poly2[j]) % mod
    return result


def compute_lagrange_basis(points: List[Tuple[int, int]], j: int) -> List[int]:
    """
    Compute the j-th Lagrange basis polynomial.
    It calculates the product of terms (x - x_m)/(x_j - x_m) for all m != j.
    """
    basis_poly = [1]
    for m, point in enumerate(points):
        if m == j:
            continue
        # (x - x_m) in polynomial form.
        numerator = [-point[0], 1]  # [coefficient, x^power]
        denominator = (points[j][0] - point[0]) % 17  # x_j - x_m
        # Multiply by (x - x_m) / (x_j - x_m)
        term = [x * pow(denominator, -1, 17) for x in numerator]
        basis_poly = polynomial_multiplication(basis_poly, term)
    return basis_poly


def calculate_lagrange_polynomial(points: List[Tuple[int, int]]) -> List[int]:
    """
    Calculate lagrange polynomial.

    Consider the example below
    Given points = [[1, 3], [4, 4], [16, 5], [13, 9]], the returned value calculated on base field of 17
    should be list - [1, 13, 3, 3]

    :param points: List of elements of form [x, y]. The returned polynomial should pass through these points

    :return: List[int] - coefficients of lagrange polynomial. The coefficient of lowest power of x
    should be the first element of list
    """

    # Add your code here
    """
    Compute the polynomial that interpolates the given points using Lagrange's method.

    We will have n-1 degrees based on n points
    """
    result_polynomial = [0] * len(points)
    for point_index, (_, y) in enumerate(points):
        for basis_poly, coeff in enumerate(compute_lagrange_basis(points, point_index)):
            result_polynomial[basis_poly] = (
                result_polynomial[basis_poly] + y * coeff
            ) % 17
    return result_polynomial


csv_writer = CSVWriter()
all_polynomial_points = csv_writer.get_points()

lp_coeffs_lst = []
for polynomial_points in all_polynomial_points:
    lp_coeffs = calculate_lagrange_polynomial(polynomial_points)
    lp_coeffs_lst.append(lp_coeffs)

csv_writer.write(lp_coeffs_lst)
