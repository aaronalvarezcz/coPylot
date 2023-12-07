from typing import Tuple

class MockLaser:
    def __init__(self, name, power=0, **kwargs):
        # Initialize the mock laser
        self.name = name
        self.laser_on = False

        self.toggle_emission = 0
        self.laser_power = power

    @property
    def toggle_emission(self):
        """
        Toggles Laser Emission On and Off
        (1 = On, 0 = Off)
        """
        print(f'Toggling laser {self.name} emission')
        return self._toggle_emission

    @toggle_emission.setter
    def toggle_emission(self, value):
        """
        Toggles Laser Emission On and Off
        (1 = On, 0 = Off)
        """
        print(f'Laser {self.name} emission set to {value}')
        self._toggle_emission = value

    @property
    def laser_power(self):
        print(f'Laser {self.name} power: {self.power}')
        return self.power

    @laser_power.setter
    def laser_power(self, power):
        self.power = power
        print(f'Laser {self.name} power set to {power}')

class MockMirror:
    def __init__(self, name, pos_x=0, pos_y=0, **kwargs):
        # Initialize the mock mirror with the given x and y positions
        self.name = name

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.position = (self.pos_x, self.pos_y)

    @property
    def position(self):
        print(f'Getting mirror position ({self.pos_x}, {self.pos_y})')
        return self.position_x, self.position_y

    @position.setter
    def position(self, value: Tuple[float, float]):
        self.position_x = value[0]
        self.position_y = value[1]
        print(f'Mirror {self.name} position set to {value}')

    @property
    def position_x(self) -> float:
        """Get the current mirror position X"""
        print(f'Mirror {self.name} Position_X {self.pos_x}')
        return self.pos_x

    @position_x.setter
    def position_x(self, value: float):
        """Set the mirror position X"""
        self.pos_x = value
        print(f'Mirror {self.name} Position_X {self.pos_x}')

    @property
    def position_y(self) -> float:
        """Get the current mirror position Y"""
        return self.pos_y

    @position_y.setter
    def position_y(self, value: float):
        """Set the mirror position Y"""
        self.pos_y = value
        print(f'Mirror {self.name} Position_Y {self.pos_y}')

