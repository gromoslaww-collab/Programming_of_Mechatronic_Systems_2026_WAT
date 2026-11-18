from matplotlib.pyplot import plot, show
from numpy import linspace, sin, size, polyfit, polyval
from numpy.random import randn

def function_definition():
    x = linspace(-10, 10, 100)
    y = sin(x) + randn(size(x)) * 0.2
    return x, y

def get_approximation_degree(description):
    if description == 'coarse':
        degree = 2
    elif description == 'medium-rare':
        degree = 4
    elif description == 'fine':
        degree = 7
    elif description == 'critical_importance':
        degree = 8
    else:
        degree = 4
    return degree



def data_processing(x, y, descritption:str='medium-rare'):
    degree = get_approximation_degree(descritption)
    p = polyfit(x, y, degree)
    y_approx = polyval(p, x)
    return y_approx

def visualization(x, y, y_approx):
    plot(x, y, 'b.')
    plot(x, y_approx, 'r-')
    show()

if __name__ == '__main__':
    x, y = function_definition()
    y_approx = data_processing(x, y, descritption='critical_importance')
    visualization(x, y, y_approx)
