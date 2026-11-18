import pylab as p
from matplotlib.pyplot import plot, show, xlim, ylim, pause, close
from numpy import linspace, sin, size, polyfit, polyval
from numpy.random import randn

def function_definition():
    x = linspace(-10, 10, 100)
    y = sin(x) + randn(size(x)) * 0.2
    return x, y

def get_approximation_degree(description):
    DESCRIPTION = {'coarse': 2, 'medium-fine': 4, 'fine': 6, 'critical_importance': 8}
    return DESCRIPTION.get(description, 2)

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
    for i in range(x.size):
        close("all")
        xlim(-10, 10)
        ylim(-1.5, 1.5)
        plot(x[:i+1], y[:i+1], 'b.')
        if i > 8:
            y_approx = data_processing(x[:i+1], y[:i+1], descritption='critical_importance')
            plot(x[:i+1], y_approx[:i+1], 'r-')
        pause(0.01)
    show()
