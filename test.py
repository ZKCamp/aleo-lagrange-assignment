# Do not change the code in this file

import hashlib

correct_solution_hash = "8348bd5d18664c75471ba49438edfc82"
solution_hash = hashlib.md5(open("solution.csv", "r").read().encode()).hexdigest()

assert(solution_hash == correct_solution_hash)
