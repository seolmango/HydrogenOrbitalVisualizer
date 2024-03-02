from math import sqrt, exp, pi, cos, sin

FIRST_BOHR_RADIUS = 5.29177210903e-11


def R_1s(r):
    return 2 / sqrt(FIRST_BOHR_RADIUS ** 3) * exp(-r / FIRST_BOHR_RADIUS)

def R_2s(r):
    return 1 / sqrt(8 * FIRST_BOHR_RADIUS ** 3) * (2 - r / FIRST_BOHR_RADIUS) * exp(-r / (2 * FIRST_BOHR_RADIUS))

def R_3s(r):
    return 2 / (81 * sqrt(3 * FIRST_BOHR_RADIUS ** 3)) * (27 - 18 * r / FIRST_BOHR_RADIUS + 2 * (r / FIRST_BOHR_RADIUS) ** 2) * exp(-r / (3 * FIRST_BOHR_RADIUS))

def R_2p(r):
    return 1 / sqrt(24 * FIRST_BOHR_RADIUS ** 3) * r / FIRST_BOHR_RADIUS * exp(-r / (2 * FIRST_BOHR_RADIUS))

def R_3p(r):
    return 4 / (81 * sqrt(6 * FIRST_BOHR_RADIUS ** 3)) * r / FIRST_BOHR_RADIUS * (6 - r / FIRST_BOHR_RADIUS) * exp(-r / (3 * FIRST_BOHR_RADIUS))

def R_3d(r):
    return 4 / (81 * sqrt(30 * FIRST_BOHR_RADIUS ** 3)) * (r / FIRST_BOHR_RADIUS) ** 2 * exp(-r / (3 * FIRST_BOHR_RADIUS))

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