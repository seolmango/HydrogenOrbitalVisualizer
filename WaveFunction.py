from math import sqrt, exp, pi, cos, sin

FIRST_BOHR_RADIUS = 5.29177210903e-11


def R_1s(r):
    return 2 / sqrt(FIRST_BOHR_RADIUS ** 3) * exp(-r / FIRST_BOHR_RADIUS)

def R_2s(r):
    return 1 / sqrt(8 * FIRST_BOHR_RADIUS ** 3) * (2 - r / FIRST_BOHR_RADIUS) * exp(-r / (2 * FIRST_BOHR_RADIUS))

def R_3s(r):
    return 2 / (81 * sqrt(3 * FIRST_BOHR_RADIUS ** 3)) * (27 - 18 * r / FIRST_BOHR_RADIUS + 2 * (r / FIRST_BOHR_RADIUS) ** 2) * exp(-r / (3 * FIRST_BOHR_RADIUS))

def R_4s(r):
    return (16 / sqrt(4096 * FIRST_BOHR_RADIUS ** 3)) * (1 - 12 * (r / (16 * FIRST_BOHR_RADIUS)) + 32 * (r / (16 * FIRST_BOHR_RADIUS)) ** 2 - (64 / 3) * (r / (16 * FIRST_BOHR_RADIUS)) ** 3) * exp(-r / (4 * FIRST_BOHR_RADIUS))

def R_2p(r):
    return 1 / sqrt(24 * FIRST_BOHR_RADIUS ** 3) * r / FIRST_BOHR_RADIUS * exp(-r / (2 * FIRST_BOHR_RADIUS))

def R_3p(r):
    return 4 / (81 * sqrt(6 * FIRST_BOHR_RADIUS ** 3)) * r / FIRST_BOHR_RADIUS * (6 - r / FIRST_BOHR_RADIUS) * exp(-r / (3 * FIRST_BOHR_RADIUS))

def R_4p(r):
    return (64 / 3) * sqrt(15 / (4096 * FIRST_BOHR_RADIUS ** 3)) * (r / (16 * FIRST_BOHR_RADIUS) - 4 * (r / (16 * FIRST_BOHR_RADIUS)) ** 2 + (16 / 5) * (r / (16 * FIRST_BOHR_RADIUS)) ** 3) * exp(-r / (4 * FIRST_BOHR_RADIUS))

def R_3d(r):
    return 4 / (81 * sqrt(30 * FIRST_BOHR_RADIUS ** 3)) * (r / FIRST_BOHR_RADIUS) ** 2 * exp(-r / (3 * FIRST_BOHR_RADIUS))

def R_4d(r):
    return (256 / 15) * sqrt(5 / (4096 * FIRST_BOHR_RADIUS ** 3)) * (3 * (r / (16 * FIRST_BOHR_RADIUS)) ** 2 - 4 * (r / (16 * FIRST_BOHR_RADIUS)) ** 3) * exp(-r / (4 * FIRST_BOHR_RADIUS))

def R_4f(r):
    return (1024 / 105) * sqrt(35 / (4096 * FIRST_BOHR_RADIUS ** 3)) * (r / (16 * FIRST_BOHR_RADIUS)) ** 3 * exp(-r / (4 * FIRST_BOHR_RADIUS))

def Y_s(theta, phi):
    return 1 / sqrt(4 * pi)

def Y_px(theta, phi):
    return sqrt(3 / (4 * pi)) * cos(phi) * sin(theta)

def Y_py(theta, phi):
    return sqrt(3 / (4 * pi)) * sin(phi) * sin(theta)

def Y_pz(theta, phi):
    return sqrt(3 / (4 * pi)) * cos(theta)

def Y_dz2(theta, phi):
    return sqrt(5 / (16 * pi)) * (3 * cos(theta) ** 2 - 1)

def Y_dxz(theta, phi):
    return sqrt(15 / (4 * pi)) * cos(phi) * cos(theta) * sin(theta)

def Y_dyz(theta, phi):
    return sqrt(15 / (4 * pi)) * sin(phi) * cos(theta) * sin(theta)

def Y_dxy(theta, phi):
    return sqrt(15 / (16 * pi)) * (sin(theta) ** 2) * sin(2 * phi)

def Y_dx2y2(theta, phi):
    return sqrt(15 / (16 * pi)) * (sin(theta) ** 2) * cos(2 * phi)

def Y_fz3(theta, phi):
    return sqrt(7 / (16 * pi)) * (5 * cos(theta) ** 3 - 3 * cos(theta))

def Y_fxz2(theta, phi):
    return (1 / 8) * sqrt(42 / pi) * (5 * cos(theta) ** 2 - 1) * cos(phi) * sin(theta)

def Y_fyz2(theta, phi):
    return (1 / 8) * sqrt(42 / pi) * (5 * cos(theta) ** 2 - 1) * sin(phi) * sin(theta)

def Y_fxyz(theta, phi):
    return (1 / 4) * sqrt(105 / pi) * sin(theta) ** 2 * cos(theta) * sin(2 * phi)

def Y_fzx2y2(theta, phi):
    return (1 / 4) * sqrt(105 / pi) * sin(theta) ** 2 * cos(2 * phi) * cos(theta)

def Y_fxx23y2(theta, phi):
    return (1 / 8) * sqrt(70 / pi) * sin(theta) ** 3 * cos(3 * phi)

def Y_fy3x2y2(theta, phi):
    return (1 / 8) * sqrt(70 / pi) * sin(theta) ** 3 * sin(3 * phi)

def oneS(r, theta, phi):
    return R_1s(r) * Y_s(theta, phi)

def twoS(r, theta, phi):
    return R_2s(r) * Y_s(theta, phi)

def twoPx(r, theta, phi):
    return R_2p(r) * Y_px(theta, phi)

def twoPy(r, theta, phi):
    return R_2p(r) * Y_py(theta, phi)

def twoPz(r, theta, phi):
    return R_2p(r) * Y_pz(theta, phi)

def threeS(r, theta, phi):
    return R_3s(r) * Y_s(theta, phi)

def threePx(r, theta, phi):
    return R_3p(r) * Y_px(theta, phi)

def threePy(r, theta, phi):
    return R_3p(r) * Y_py(theta, phi)

def threePz(r, theta, phi):
    return R_3p(r) * Y_pz(theta, phi)

def threeDz2(r, theta, phi):
    return R_3d(r) * Y_dz2(theta, phi)

def threeDxz(r, theta, phi):
    return R_3d(r) * Y_dxz(theta, phi)

def threeDyz(r, theta, phi):
    return R_3d(r) * Y_dyz(theta, phi)

def threeDxy(r, theta, phi):
    return R_3d(r) * Y_dxy(theta, phi)

def threeDx2y2(r, theta, phi):
    return R_3d(r) * Y_dx2y2(theta, phi)

def fourS(r, theta, phi):
    return R_4s(r) * Y_s(theta, phi)

def fourPx(r, theta, phi):
    return R_4p(r) * Y_px(theta, phi)

def fourPy(r, theta, phi):
    return R_4p(r) * Y_py(theta, phi)

def fourPz(r, theta, phi):
    return R_4p(r) * Y_pz(theta, phi)

def fourDz2(r, theta, phi):
    return R_4d(r) * Y_dz2(theta, phi)

def fourDxz(r, theta, phi):
    return R_4d(r) * Y_dxz(theta, phi)

def fourDyz(r, theta, phi):
    return R_4d(r) * Y_dyz(theta, phi)

def fourDxy(r, theta, phi):
    return R_4d(r) * Y_dxy(theta, phi)

def fourDx2y2(r, theta, phi):
    return R_4d(r) * Y_dx2y2(theta, phi)

def fourFz3(r, theta, phi):
    return R_4f(r) * Y_fz3(theta, phi)

def fourFxz2(r, theta, phi):
    return R_4f(r) * Y_fxz2(theta, phi)

def fourFyz2(r, theta, phi):
    return R_4f(r) * Y_fyz2(theta, phi)

def fourFxyz(r, theta, phi):
    return R_4f(r) * Y_fxyz(theta, phi)

def fourFzx2y2(r, theta, phi):
    return R_4f(r) * Y_fzx2y2(theta, phi)

def fourFxx23y2(r, theta, phi):
    return R_4f(r) * Y_fxx23y2(theta, phi)

def fourFy3x2y2(r, theta, phi):
    return R_4f(r) * Y_fy3x2y2(theta, phi)