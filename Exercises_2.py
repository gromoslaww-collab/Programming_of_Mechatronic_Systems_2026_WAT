from abc import ABC, abstractclassmethod
from enum import Enum, auto

from matplotlib.pyplot import plot, show, pause, xlim, ylim, cla, figure, close
from numpy import linspace, sin, cos, tan, size, polyfit, polyval
from numpy.random import randn

fig = figure()
great_sea = fig.add_subplot(projection='3d')
great_sea.set_xlabel('X Axis')
great_sea.set_ylabel('Y Axis')
great_sea.set_zlabel('Z Axis')
great_sea.set_xlim(-25, 25)
great_sea.set_ylim(-25, 25)
great_sea.set_zlim(0, 25)


class ThreatValues(Enum):
    UNIDENTIFIED = auto()
    UNKNOWN = auto()
    HOSTILE = auto()
    FRIENDLY = auto()
    NEUTRAL = auto()

class BasicVessel:
    def __init__(self, id: str, position: tuple = (0.0, 0.0, 0.0), threat: ThreatValues=ThreatValues.UNIDENTIFIED):
        self.id = id
        self.position = position
        self.threat = threat

class MobileVessel(ABC, BasicVessel):
    def __init__(self, id: str, position: tuple, threat: ThreatValues = ThreatValues.UNIDENTIFIED):
        super().__init__(id, position, threat)
    @abstractclassmethod
    def move(self):
        ...
    def visualisation_onfly(self):
        match self.threat:
            case ThreatValues.HOSTILE:
                color = 'ro'
            case ThreatValues.NEUTRAL:
                color = 'go'
            case ThreatValues.FRIENDLY:
                color = 'bo'
            case _:
                color = 'yo'

        great_sea.plot(self.position[0], self.position[1], self.position[2], color)
        pause(0.01)

class MobileSeaVessel(MobileVessel, BasicVessel):
    def __init__(self, id: str, position: tuple, threat: ThreatValues=ThreatValues.UNIDENTIFIED, speed: float = 0.0, sigma: float = 0.8):
        super().__init__(id, position, threat)
        self.speed = speed
        self.sigma = sigma #standard deviation

    def move(self):
        self.position = (self.position[0] + self.speed + randn()*self.sigma**2, self.position[1] + self.speed + randn()*self.sigma**2, 0.0)
   
   
        
class MobileAerialVessel(MobileVessel, BasicVessel):
    def __init__(self, id: str, position: tuple, threat: ThreatValues=ThreatValues.UNIDENTIFIED, speed: float = 0.0, sigma: float = 0.8, max_altitude: float = 15.0, min_altitude: float = 0.0):
        super().__init__(id, position, threat)
        self.speed = speed
        self.sigma = sigma #standard deviation
        self.max_altitude = max_altitude
        self.min_altitude = min_altitude

    def move(self):
        self.position = (self.position[0] + self.speed + randn()*self.sigma**2, self.position[1] + self.speed + randn()*self.sigma**2, self.position[2] + 0.3*self.speed + randn()*self.sigma**2)
        if self.position[2] > self.max_altitude:
            self.position = (self.position[0], self.position[1], self.max_altitude)
        elif self.position[2] < self.min_altitude:
            self.position = (self.position[0], self.position[1], self.min_altitude)


if __name__ == '__main__':
    Vessel_1 = MobileSeaVessel('Vessel_1', (0.0, 0.0), speed=0.6, sigma=0.5)
    Vessel_1.threat = ThreatValues.FRIENDLY
    Vessel_2 = MobileSeaVessel('Vessel_2', (20.0, 23.0), speed=-2, sigma=1, threat = ThreatValues.HOSTILE)
    Vessel_3 = MobileSeaVessel('Vessel_3', (2.0, 7.0), speed=0.3, sigma=0.3, threat = ThreatValues.NEUTRAL)
    Aerial_Vessel_1 = MobileAerialVessel('Aerial_Vessel_1', (10, 10, 10), speed=3, sigma=0.5, threat = ThreatValues.FRIENDLY, max_altitude=13, min_altitude=8)
    Aerial_Vessel_2 = MobileAerialVessel('Aerial_Vessel_2', (-10, 10, 10), speed=4, sigma=0.7, threat=ThreatValues.HOSTILE, max_altitude=16, min_altitude=3)

    for i in range(10):
        Vessel_1.move()
        Vessel_2.move()
        Vessel_3.move()
        Aerial_Vessel_1.move()
        Aerial_Vessel_2.move()
        Vessel_1.visualisation_onfly()
        Vessel_2.visualisation_onfly()
        Vessel_3.visualisation_onfly()
        Aerial_Vessel_1.visualisation_onfly()
        Aerial_Vessel_2.visualisation_onfly()

    show()
