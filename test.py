# Do not change the code in this file

import hashlib

correct_solution_hash = "98e5f20e7d1af4396a5861f1941a145a"
solution_hash = hashlib.md5(open("solution.csv", "r").read().encode()).hexdigest()

assert(solution_hash == correct_solution_hash)