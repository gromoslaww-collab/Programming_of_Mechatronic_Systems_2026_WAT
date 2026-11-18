from matplotlib.pyplot import plot, show, pause, xlim, ylim, figure, close
from numpy import linspace, sin, cos, tan, size, polyfit, polyval
from numpy.random import randn

class DynamicGraph:

    DESCRIPTION = {'coarse': 2, 'medium-fine': 4, 'fine': 6, 'critical_importance': 8}
    FUNCTION = {'sin': 0, 'cos': 1, 'tan': 2, 'quadratic': 3, 'linear': 4}

    def __init__(self, description: str ='fine', start:int=0, stop:int=10, Num_of_Points:int=100, noise:float=0.2, function:str='sin'):
        self.description = description
        self.min_points = self.get_approximation_degree()
        self.start = start
        self.stop = stop
        self.Num_of_Points = Num_of_Points
        self.noise = noise
        self.function = function
        self.x = None
        self.y = None
        self.y_approx = []

    def function_definition(self):
        # self.x = linspace(0, 10, 110)
        # self.y = sin(self.x) + randn(size(self.x)) * 0.2

        self.x = linspace(self.start, self.stop, self.Num_of_Points)
        function = self.get_function()
        match function:
            case 0:
                self.y = sin(self.x) + randn(size(self.x)) * self.noise
            case 1:
                self.y = cos(self.x) + randn(size(self.x)) * self.noise
            case 2:
                self.y = tan(self.x) + randn(size(self.x)) * self.noise
            case 3:
                self.y = self.x ** 2 + randn(size(self.x)) * self.noise
            case 4:
                self.y = self.x + randn(size(self.x)) * self.noise

    def get_approximation_degree(self):
        return self.DESCRIPTION.get(self.description, 6)

    def get_function(self):
        return self.FUNCTION.get(self.function, 0)

    def data_processing(self):
        degree = self.get_approximation_degree()
        for i in range(self.x.size):
            if  i >= self.min_points:
                p = polyfit(self.x[:i + 1], self.y[:i + 1], degree)
                self.y_approx.append(polyval(p, self.x[:i + 1]))
            else:
                self.y_approx.append(None)

    def visualization(self):
        x_min = self.x[0]
        x_max = self.x[self.x.size - 1]
        y_min = self.y[0]
        y_max = self.y[0]
        for i in range(self.y.size):
            if y_max > self.y[i]:
                y_max = self.y[i]
            if y_min < self.y[i]:
                y_min = self.y[i]

        for i in range(self.x.size):
            xlim(x_min - 1, x_max + 1)
            ylim(y_min - 1, y_max + 1)
            plot(self.x[:i + 1], self.y[:i + 1], 'b.')
            if self.y_approx[i] is not None:
                plot(self.x[:i + 1], self.y_approx[i], 'r-')
            pause(0.01)
            show()


if __name__ == '__main__':
    graph = DynamicGraph('critical_importance', 0, 13, 120, 0.5, 'tan')
    graph.function_definition()
    #__init__(self, description: str ='fine', start:int=0, stop:int=10, Num_of_Points:int=20, noise:float=0.2, function:str='sin'):
    graph.function_definition()
    graph.data_processing()
    graph.visualization()