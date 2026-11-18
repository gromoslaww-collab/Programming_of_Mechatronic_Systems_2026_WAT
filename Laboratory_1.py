from enum import Enum, auto

from matplotlib.pyplot import plot, show, pause, xlim, ylim, cla
from numpy import linspace, sin, cos, tan, size, polyfit, polyval
from numpy.random import randn

class ThreatValues(Enum):
    UNIDENTIFIED = auto()
    UNKNOWN = auto()
    HOSTILE = auto()
    FRIENDLY = auto()
    NEUTRAL = auto()

class BasicVessel:
    def __init__(self, id: str, position: tuple = (0.0, 0.0), threat: ThreatValues=ThreatValues.UNIDENTIFIED):
        self.id = id
        self.position = position
        self.threat = threat

class MobileVessel(BasicVessel):
    def __init__(self, id: str, position: tuple, threat: ThreatValues=ThreatValues.UNIDENTIFIED, speed: float = 0.0, SIGMA: float = 0.8):
        super().__init__(id, position, threat)
        self.speed = speed
        self.SIGMA = SIGMA #standard deviation

    def move(self):
        self.position = (self.position[0] + self.speed + randn()*self.SIGMA**2, self.position[1] + self.speed + randn()*self.SIGMA**2)

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

        plot(self.position[0], self.position[1], color)
        pause(0.01)


if __name__ == '__main__':
    Vessel_1 = MobileVessel('Vessel_1', (0.0, 0.0), speed=0.6, SIGMA=0.5)
    Vessel_1.threat = ThreatValues.FRIENDLY
    Vessel_2 = MobileVessel('Vessel_2', (20.0, 23.0), speed=-2, SIGMA=1, threat = ThreatValues.HOSTILE)
    Vessel_3 = MobileVessel('Vessel_3', (2.0, 7.0), speed=0.3, SIGMA=0.3, threat = ThreatValues.NEUTRAL)


    for i in range(10):
        Vessel_1.move()
        Vessel_2.move()
        Vessel_3.move()
        Vessel_1.visualisation_onfly()
        Vessel_2.visualisation_onfly()
        Vessel_3.visualisation_onfly()

    show()
