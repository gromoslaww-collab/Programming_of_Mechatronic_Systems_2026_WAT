from matplotlib.pyplot import plot, show, xlim, ylim, pause
from numpy import linspace, sin, cos, tan, size, polyfit, polyval
from numpy.random import randn

def function_definition(start:int=0, stop:int=10, Num_of_Points:int=100, noise:float=0.2, function:str='sin'):
    x = linspace(start, stop, Num_of_Points)
    function = get_functions(function)
    match function:
        case 0:
            y = sin(x) + randn(size(x)) * noise
        case 1:
            y = cos(x) + randn(size(x)) * noise
        case 2:
            y = tan(x) + randn(size(x)) * noise
        case 3:
            y = x**2 + randn(size(x)) * noise
        case 4:
            y = x + randn(size(x)) * noise
    return x, y

def get_functions(function):
    FUNCTION = {'sin': 0, 'cos': 1, 'tan': 2, 'quadratic': 3, 'linear': 4}
    return FUNCTION.get(function, 0)

def get_approximation_degree(description):
    DESCRIPTION = {'coarse': 2, 'medium-rare': 4, 'fine': 6, 'critical_importance': 8}
    return DESCRIPTION.get(description, 2)

def data_processing(x, y, descritption:str='medium-rare'):
    degree = get_approximation_degree(descritption)
    p = polyfit(x, y, degree)
    y_approx = polyval(p, x)
    return y_approx

def visualization(x, y, y_approx):
    y_min = y[0]
    y_max = y[0]
    for i in range(y.size):
        if y_max > y[i]:
            y_max = y[i]
        if y_min < y[i]:
            y_min = y[i]
    for i in range(x.size):
        xlim(x[0], x[x.size-1])
        ylim((y_min - 0.5), (y_max + 0.5))
        plot(x[:i+1], y[:i+1], 'b.')
        plot(x[:i+1], y_approx[:i+1], 'r-')
        pause(0.01)
        show()


if __name__ == '__main__':
    # User Notice: DO NOT USE MORE THAN 300 POINTS
    x, y = function_definition(0, 13, 70, 0.5, function='tan')
    y_approx = data_processing(x, y, descritption='th')
    visualization(x, y, y_approx)
