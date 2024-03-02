from WaveFunction import FIRST_BOHR_RADIUS, oneS, twoS, twoPz, twoPx, twoPy

class Orbital:
    def __init__(self, n: int, shape: str, direction: str):
        self.n = n
        self.shape = shape
        self.direction = direction
        self.wave = self.orbital_wave(n, shape, direction)

    def change_wave(self, n: int, shape: str, direction: str):
        self.n = n
        self.shape = shape
        self.direction = direction
        self.wave = self.orbital_wave(n, shape, direction)

    def orbital_wave(self, n: int, shape: str, direction: str):
        if n == 1:
            if shape == 's' and direction == 'none':
                return oneS
        elif n == 2:
            if shape == 's' and direction == 'none':
                return twoS
            elif shape == 'p' and direction == 'z':
                return twoPz
            elif shape == 'p' and direction == 'x':
                return twoPx
            elif shape == 'p' and direction == 'y':
                return twoPy
        raise ValueError(f"No wave function for n={n}, shape={shape}, direction={direction}")