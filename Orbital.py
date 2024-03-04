from WaveFunction import FIRST_BOHR_RADIUS, oneS, twoS, twoPz, twoPx, twoPy, threeS, threePx, threePy, threePz, threeDz2, threeDxz, threeDyz, threeDxy, threeDx2y2\
    , fourS, fourPx, fourPy, fourPz, fourDz2, fourDxz, fourDyz, fourDxy, fourDx2y2, fourFz3, fourFy3x2y2, fourFxyz, fourFxz2, fourFyz2, fourFzx2y2, fourFxx23y2

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
        elif n == 3:
            if shape == 's' and direction == 'none':
                return threeS
            elif shape == 'p' and direction == 'x':
                return threePx
            elif shape == 'p' and direction == 'y':
                return threePy
            elif shape == 'p' and direction == 'z':
                return threePz
            elif shape == 'd' and direction == 'z^2':
                return threeDz2
            elif shape == 'd' and direction == 'xz':
                return threeDxz
            elif shape == 'd' and direction == 'yz':
                return threeDyz
            elif shape == 'd' and direction == 'xy':
                return threeDxy
            elif shape == 'd' and direction == 'x^2-y^2':
                return threeDx2y2
        elif n == 4:
            if shape == 's' and direction == 'none':
                return fourS
            elif shape == 'p' and direction == 'x':
                return fourPx
            elif shape == 'p' and direction == 'y':
                return fourPy
            elif shape == 'p' and direction == 'z':
                return fourPz
            elif shape == 'd' and direction == 'z^2':
                return fourDz2
            elif shape == 'd' and direction == 'xz':
                return fourDxz
            elif shape == 'd' and direction == 'yz':
                return fourDyz
            elif shape == 'd' and direction == 'xy':
                return fourDxy
            elif shape == 'd' and direction == 'x^2-y^2':
                return fourDx2y2
            elif shape == 'f' and direction == 'z^3':
                return fourFz3
            elif shape == 'f' and direction == 'xz^2':
                return fourFxz2
            elif shape == 'f' and direction == 'yz^2':
                return fourFyz2
            elif shape == 'f' and direction == 'xyz':
                return fourFxyz
            elif shape == 'f' and direction == 'z(x^2-y^2)':
                return fourFzx2y2
            elif shape == 'f' and direction == 'x(x^2-3y^2)':
                return fourFxx23y2
            elif shape == 'f' and direction == 'y(3x^2-y^2)':
                return fourFy3x2y2
        raise ValueError(f"No wave function for n={n}, shape={shape}, direction={direction}")