def least_squares_regression(x_mean, y_mean, x_std_dev, y_std_dev, r):
    slope = r * (y_std_dev / x_std_dev)
    intercept = y_mean - slope * x_mean
    return slope, intercept

print('\n------- Least Squares Regression Line Equation -------')

x_mean = float(input('X Mean\t? '))
y_mean = float(input('Y Mean\t? '))
x_std_dev = float(input('X SD\t? '))
y_std_dev = float(input('Y SD\t? '))
r = float(input('R\t? '))

slope, intercept = least_squares_regression(x_mean, y_mean, x_std_dev, y_std_dev, r)
print(f'Regression Line Equation: \ny = {round(slope,2)}x + {round(intercept,2)}')

print ('-'*40+'\n')
