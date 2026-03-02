import math


def main():
    ## initial parameters
    pressure = 101325  ## Pascal/Pa
    temperature = 288.15  ## Kelvin -> 15 Celcius
    base_altitude = 0
    air_constant = 287.05  ## J/(kg*K)
    gravity = 9.80665  ## m/s**2

    ## get user input for altitude
    altitude = int(input("Altitude(in meters): "))

    while altitude < 0 or altitude > 85000:
        print("Enter a number that is between 0 and 85000")
        altitude = int(input("Altitude(in meters): "))

    # height in meters, lapse rate in Kelvin/meters
    layers = [
        (11000, -0.0065),
        (20000, 0.0),
        (32000, 0.0010),
        (47000, 0.0028),
        (51000, 0.0),
        (71000, -0.0028),
        (84852, -0.0020),
    ]

    for h_ceiling, L in layers:
        h_end = min(altitude, h_ceiling)
        delta_h = h_end - base_altitude

        if L != 0:
            t_end = temperature + L * delta_h
            p_end = pressure * (t_end / temperature) ** (-gravity / (L * air_constant))
        else:
            t_end = temperature
            p_end = pressure * math.exp(
                -gravity * delta_h / (air_constant * temperature)
            )

        # update variables
        base_altitude, temperature, pressure = h_end, t_end, p_end

        # if we reached the altitude break the loop
        if altitude <= h_ceiling:
            break

    ## density = P/(R*T)
    density = pressure / (air_constant * temperature)

    speed_of_sound = (1.4 * air_constant * temperature) ** (0.5)

    print(f"Temperature: {temperature}")
    print(f"Pressure: {pressure}")
    print(f"Density: {density}")
    print(f"Speed of Sound: {speed_of_sound}")


if __name__ == "__main__":
    main()
