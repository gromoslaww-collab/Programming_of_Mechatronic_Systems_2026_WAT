import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
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

        self.root = tk.Tk()
        self.root.title('Dynamic Graph')
        self.root.geometry('850x700')

        self.start_button =tk.Button(self.root, text='Start', command=self.start_simulation)
        self.start_button.pack(side=tk.BOTTOM, pady=10)

        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlim(0, 8)
        self.axes.set_ylim(-1.5, 1.5)

        self.data_line, = self.axes.plot([], [], 'b.', label='Data')
        #     What does the "," do here? It serves the same functionality as the following:
        #     self.data_line, = self.axes.plot([], [], 'b.', label='Data')
        #     creates a list containing graphical element "plot([], [], 'b.', label='Data')", to be specific:
        #     self.data_line = [plot_element]
        #     to retrieve the plot element we would normally:
        #     self.data_line = self.data_line[0]
        #     or we can just use ",":  self.data_line, = self.axes.plot([], [], 'b.', label='Data')
        self.approx_line, = self.axes.plot([], [], 'r-', label='Approximation')

        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def start_simulation(self):
        self.function_definition()
        self.data_processing()
        self._update_plot()

    def _update_plot(self, n: int):
        self.data_line.set_data(self.x[:n], self.y[:n])

        approximation = self.y_approx[n-1]
        if approximation is not None:
            self.approx_line.set_data(self.x[:n], approximation)
        else:
            self.approx_line.set_data([], [])
        self.canvas.draw_idle()
        if n < self.x.size:
            self.root.after(100, self._update_plot, n+1)
        else:
            self.start_button.config(state=tk.NORMAL)


    def function_definition(self):

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

    #
    # def visualization(self):
    #     x_min = self.x[0]
    #     x_max = self.x[self.x.size - 1]
    #     y_min = self.y[0]
    #     y_max = self.y[0]
    #     for i in range(self.y.size):
    #         if y_max > self.y[i]:
    #             y_max = self.y[i]
    #         if y_min < self.y[i]:
    #             y_min = self.y[i]
    #
    #     for i in range(self.x.size):
    #         xlim(x_min - 1, x_max + 1)
    #         ylim(y_min - 1, y_max + 1)
    #         plot(self.x[:i + 1], self.y[:i + 1], 'b.')
    #         if self.y_approx[i] is not None:
    #             plot(self.x[:i + 1], self.y_approx[i], 'r-')
    #         pause(0.01)
    #         show()



if __name__ == '__main__':
    graph = DynamicGraph()
    graph.root.mainloop()