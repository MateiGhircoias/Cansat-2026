def pressure_to_altitude(pressure_hpa, sea_level_pressure=1010):
    return 44330 * (1 - (pressure_hpa / sea_level_pressure) ** 0.1903)