import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(
        self,
        starting_position: tuple[float | int, float | int],
        velocity: tuple[float | int, float | int],
        time: tuple[float, int],
        horizontal_acceleration: float = 0,
        stop_after_hitting_ground_level: bool = False,
    ) -> None:
        self.starting_position = np.array(starting_position)
        self.velocity = np.array(velocity)
        self.time = np.arange(0, time[0] + 1, time[1])
        self.gravity: float = 9.8
        self.horizontal_acceleration = horizontal_acceleration
        self.stop_after_hitting_ground_level = stop_after_hitting_ground_level

        self.simulate()

    def simulate(self):
        # first lets find the total time it takes to finish the movement
        # Vx = Vix + a * t
        # Vy = Viy + a * t
        # x = xi + Vix * t + a * t / 2
        # y = yi + Viy * t + a * t / 2
        x_initial = self.starting_position[0]
        y_initial = self.starting_position[1]

        velocity_initial_x = self.velocity[0]
        velocity_initial_y = self.velocity[1]

        self.x_pos = (
            x_initial
            + velocity_initial_x * self.time
            + (self.horizontal_acceleration * np.pow(self.time, 2)) / 2
        )
        self.y_pos = (
            y_initial
            + velocity_initial_y * self.time
            - (self.gravity * np.pow(self.time, 2)) / 2
        )

        if self.stop_after_hitting_ground_level:
            mask = self.y_pos >= 0
            self.x_pos = self.x_pos[mask]
            self.y_pos = self.y_pos[mask]
            self.time = self.time[mask]

        self.velocity_x = velocity_initial_x + self.horizontal_acceleration * self.time
        self.velocity_y = velocity_initial_y - self.gravity * self.time

        # calculate velocity using x and y components
        self.velocity = np.sqrt(np.pow(self.velocity_x, 2) + np.pow(self.velocity_y, 2))

    def plot_velocity_time(self):
        plt.plot(self.time, self.velocity)
        plt.title("Velocity x Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Velocity")
        plt.grid()
        plt.savefig("velocity_time_graph.png")
        plt.show()
        plt.close()

    def plot_range_time(self):
        plt.plot(self.time, self.x_pos)
        plt.title("Range x Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Range")
        plt.grid()
        plt.savefig("range_time_graph.png")
        plt.show()
        plt.close()

    def plot_altitude_time(self):
        plt.plot(self.time, self.y_pos)
        plt.title("Altitude x Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Altitude")
        plt.grid()
        plt.savefig("altitude_time_graph.png")
        plt.show()
        plt.close()

    def plot_altitude_range(self):
        plt.plot(self.x_pos, self.y_pos)
        plt.title("Altitude x Range Graph")
        plt.xlabel("Range")
        plt.ylabel("Altitude")
        plt.grid()
        plt.savefig("altitude_range_graph.png")
        plt.show()
        plt.close()


def main():
    x_pos = float(input("x position: "))
    y_pos = float(input("y position: "))

    velocity_x = float(input("Initial horizontal velocity component: "))
    velocity_y = float(input("Initial vertical velocity component: "))

    try:
        horizontal_acceleration: float = float(input("Enter horizontal acceleration: "))
    except Exception:
        print("Error: setting horizontal acceleration to 0")
        horizontal_acceleration: float = 0.0

    time = float(input("Enter how long you want the simulation to run: "))
    time_step = int(input("Enter time step: "))

    if input("Stop after hitting ground level(y=0): ").lower() in [
        "y",
        "yes",
        "yeah",
        "yeah",
        "true",
        "1",
        "t",
    ]:
        stop_after_hitting_ground_level: bool = True
    else:
        stop_after_hitting_ground_level: bool = False

    sim = Simulation(
        (x_pos, y_pos),
        (velocity_x, velocity_y),
        (time, time_step),
        horizontal_acceleration,
        stop_after_hitting_ground_level,
    )

    sim.plot_velocity_time()
    sim.plot_range_time()
    sim.plot_altitude_time()
    sim.plot_altitude_range()


if __name__ == "__main__":
    main()
