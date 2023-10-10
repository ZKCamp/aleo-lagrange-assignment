from csv_writer import CSVWriter


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

    # Add your code here
    pass


csv_writer = CSVWriter()
all_polynomial_points = csv_writer.get_points()

lp_coeffs_lst = []
for polynomial_points in all_polynomial_points:
    lp_coeffs = calculate_lagrange_polynomial(polynomial_points)
    lp_coeffs_lst.append(lp_coeffs)

csv_writer.write(lp_coeffs_lst)
