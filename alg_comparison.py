"""This file serves to compare the algorithms created"""

#statistical tests
#visualizations

import random

start_range = 2000
end_range = 5000
gens = 10


alternatives_test=["test1", "test2", "test3"]
for alternative in alternatives_test:
    algorithm_fit=[]
    for i in range(30):
        random_numbers=[random.randint(2000,5000)]
        for _ in range(gens):
            decrease = random.randint(1, 100)  # Random amount to decrease
            next_number = numbers[-1] - decrease
            random_numbers.append(next_number)
        algorithm_fit.append(random_numbers)
    
    with open(f"{alternative}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(algorithm_fit)
