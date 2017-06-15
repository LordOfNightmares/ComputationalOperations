from simplex import Simplex

print('First condition')
objective = ('maximize', '8000x_1 + 16000x_2 + 24000x_3')
constraints = ['1200x_2 + 5800x_3 <= 1500', '5x_1 + 5x_2 + 5x_3 <= 6', '4x_1 >= 2']
Lp_system = Simplex(num_vars=3, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print('max profit = ', Lp_system.optimize_val,   '\n')

print('second year, with the new investment')
constraints = ['1200x_2 + 5800x_3 <= 16347', '5x_1 + 5x_2 + 5x_3 <= 6', '4x_1 >= 2']
Lp_system = Simplex(num_vars=3, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print('max profit = ', Lp_system.optimize_val, '\n')

print('Second condition, no need new grape seeds')
constraints = ['1200x_2 + 5000x_3 <= 1500', '5x_1 + 5x_2 + 5x_3 <= 6', '4x_1 >= 2']
Lp_system = Simplex(num_vars=3, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print('max profit = ', Lp_system.optimize_val, '\n')

print('Third condition, less paid collectors, minus 100 liters of wine')
objective = ('maximize', '8000x_1 + 16000x_2 + 24000x_3 - 600')
#600 is the 100 litres given to the collectors
constraints = ['1200x_2 + 3300x_3 <= 1500', '5x_1 + 5x_2 + 5x_3 <= 6', '4x_1 >= 2']
Lp_system = Simplex(num_vars=3, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print('max profit = ', Lp_system.optimize_val)
