from csv_writer import CSVWriter
from helpers.polynomial_helper import Polynomial
from fields.field import FQ


def calculate_lagrange_polynomial(points):
    """
    Calculate lagrange polynomial.

    Consider the example below
    Given points = [[1, 3], [4, 4], [16, 5], [13, 9]], the returned value calculated on base field of 17
    should be list - [1, 13, 3, 3]

    :param points: List of elements of form [x, y]. The returned polynomial should pass through these points

    :return: List[int] - coefficients of lagrange polynomial. The coefficient of lowest power of x
    should be the first element of list
    """

    poly = Polynomial.from_points([
        [FQ(point[0]), FQ(point[1])]
        for point in points
    ])
    return [_.val for _ in poly.coeffs]


csv_writer = CSVWriter()
all_polynomial_points = csv_writer.get_points()

lp_coeffs_lst = []
for polynomial_points in all_polynomial_points:
    lp_coeffs = calculate_lagrange_polynomial(polynomial_points)
    lp_coeffs_lst.append(lp_coeffs)

csv_writer.write(lp_coeffs_lst)