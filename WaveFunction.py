import math

FIRST_BOHR_RADIUS = 5.29177210903e-11


def R_100(r: float) -> float:
    """
    Radial part of the wave function for n=1, l=0, m=0
    :param r: radius
    :return: value
    """
    return 2 * (FIRST_BOHR_RADIUS ** -1.5) * math.exp(-r / FIRST_BOHR_RADIUS)

def R_200(r: float) -> float:
    """
    Radial part of the wave function for n=2, l=0, m=0
    :param r: radius
    :return: value
    """
    return 1 / math.sqrt(8 * FIRST_BOHR_RADIUS ** 3) * (2 - r / FIRST_BOHR_RADIUS) * math.exp(-r / (2 * FIRST_BOHR_RADIUS))

def R_21(r: float) -> float:
    """
    Radial part of the wave function for n=2, l=1, m=1,-1
    :param r: radius
    :return: value
    """
    return 1 / math.sqrt(24 * FIRST_BOHR_RADIUS ** 3) * r / FIRST_BOHR_RADIUS * math.exp(-r / (2 * FIRST_BOHR_RADIUS))

def oneS(r: float, theta: float, phi: float) -> float:
    """
    Wave function for n=1, l=0, m=0
    :param r:
    :param theta:
    :param phi:
    :return:
    """
    return R_100(r) * math.sqrt(4 * math.pi)

def twoS(r: float, theta: float, phi: float) -> float:
    """
    Wave function for n=2, l=0, m=0
    :param r:
    :param theta:
    :param phi:
    :return:
    """
    return R_200(r) * math.sqrt(4 * math.pi)

def twoPz(r: float, theta: float, phi: float) -> float:
    """
    Wave function for n=2, l=1, m=0
    :param r:
    :param theta:
    :param phi:
    :return:
    """
    return R_21(r) * math.sqrt(2 * math.pi) * math.sqrt(6) / 2 * math.cos(theta)

def twoPx(r: float, theta: float, phi: float) -> float:
    """
    Wave function for n=2, l=1 and orientation x
    :param r:
    :param theta:
    :param phi:
    :return:
    """
    return R_21(r) * math.sqrt(2 * math.pi) * math.sqrt(6) / 2 * math.sin(theta) * math.cos(phi)

def twoPy(r: float, theta: float, phi: float) -> float:
    """
    Wave function for n=2, l=1 and orientation y
    :param r:
    :param theta:
    :param phi:
    :return:
    """
    return R_21(r) * math.sqrt(2 * math.pi) * math.sqrt(6) / 2 * math.sin(theta) * math.sin(phi)