# physics.py
# A collection of 5 fundamental physics formulas

def wave_speed(frequency, wavelength):
    """Calculates wave speed: v = f * lambda"""
    return frequency * wavelength

def centripetal_force(mass, velocity, radius):
    """Calculates centripetal force: Fc = (m * v^2) / r"""
    return (mass * (velocity ** 2)) / radius

def gravitational_force(mass1, mass2, radius):
    """Calculates Newton's law of universal gravitation: F = (G * m1 * m2) / r^2"""
    G = 6.67430e-11 # Gravitational constant in m^3 kg^-1 s^-2
    return (G * mass1 * mass2) / (radius ** 2)

def electrical_power(voltage, current):
    """Calculates electrical power: P = V * I"""
    return voltage * current

def hydrostatic_pressure(density, gravity, depth):
    """Calculates fluid pressure at a depth: P = rho * g * h"""
    return density * gravity * depth
