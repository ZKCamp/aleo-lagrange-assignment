# Do not change the code in this file

import hashlib

correct_solution_hash = "22ad632aa128cf40dc24430d21f7e4f4"
solution_hash = hashlib.md5(open("solution.csv", "r").read().encode()).hexdigest()

assert(solution_hash == correct_solution_hash)