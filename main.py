import tkinter as tk


class Window:
    def __init__(self, width, height, zoom_percent=100):
        self.width = width
        self.height = height
        self.zoom_percent = zoom_percent
        self.is_running = False
        self.scale_factor = self.width * 0.4 * 2.6e-9

        self.root = tk.Tk()
        self.root.title('Tidal Effects')
        self.root.geometry("{}x{}".format(self.width, self.height))

        self.space = tk.Canvas(self.root, width=(0.85 * self.width),
                               height=self.height, bg='black')
        self.space.pack(side=tk.LEFT)
        self.frame = tk.Frame(self.root, width=(0.15 * self.width))
        self.frame.pack(fill=tk.X, side=tk.LEFT, expand=1)

        self.celestial_bodies = []  # TODO: add all elements

        self._set_controllers()

        self.space.bind('<ButtonPress>', self.zoom)
        self.root.mainloop()

    def _set_controllers(self):
        """
        Create controllers for changing parameters. (planets' density, velocity, ...)

        :return:
        """
        self.start_button = tk.Button(self.frame, text="Start", command=self._start_running)
        self.start_button.pack(side=tk.TOP)

        earth_dens, moon_dens = tk.DoubleVar(), tk.DoubleVar()
        earth_dens.set(1000)  # FIXME: set initial densities
        moon_dens.set(1000)
        self.earth_density = tk.Scale(
            self.frame,
            variable=earth_dens,
            orient=tk.HORIZONTAL,
            from_=1000,
            to=10000,
            resolution=100,
            length=self.width * 0.15,
            label='Earth Density',
        )
        self.moon_density = tk.Scale(
            self.frame,
            variable=moon_dens,
            orient=tk.HORIZONTAL,
            from_=1000,
            to=10000,
            resolution=100,
            length=self.width * 0.15,
            label='Moon Density',
        )
        self.earth_density.pack(side=tk.TOP)
        self.moon_density.pack(side=tk.TOP)

        earth_vel, moon_vel = tk.DoubleVar(), tk.DoubleVar()  # in km/s
        earth_vel.set(1)  # FIXME: set initial velocities.
        moon_vel.set(1)
        e_vel_label = tk.Label(self.frame, text='Earth Full Velocity in km/s', wraplength=self.width / 10)
        m_vel_label = tk.Label(self.frame, text='Moon Full Velocity in km/s', wraplength=self.width / 10)
        self.earth_velocity = tk.Scale(
            self.frame,
            variable=earth_vel,
            orient=tk.HORIZONTAL,
            from_=1,
            to=30,
            length=self.width * 0.15,
        )
        self.moon_velocity = tk.Scale(
            self.frame,
            variable=moon_vel,
            orient=tk.HORIZONTAL,
            from_=1,
            to=17,
            length=self.width * 0.15,
        )
        e_vel_label.pack(side=tk.TOP)
        self.earth_velocity.pack(side=tk.TOP)
        m_vel_label.pack(side=tk.TOP)
        self.moon_velocity.pack(side=tk.TOP)

    def _start_running(self):
        """
        Changing Start Button text and command, running program.

        :return:
        """
        self.is_running = True
        self.start_button['text'] = 'Pause'
        self.start_button['command'] = self._stop_running

        self.run()

    def run(self):
        """
        Moves objects, changes coordinates.

        :return: None
        """
        pass

    def _stop_running(self):
        """
        Changing Start Button text and command, running program.

        :return:
        """
        self.is_running = False
        self.start_button['text'] = 'Start'
        self.start_button['command'] = self._start_running

    def zoom(self, event):
        if self.is_running:
            if event.num == 5 and self.zoom_percent > 50:  # Scroll down
                self.zoom_percent -= 10
            elif event.num == 4 and self.zoom_percent < 160:  # Scroll up
                self.zoom_percent += 10

    def scale_coordinates(self, cel_obj):
        """
        Scales cel_obj's x, y, when user zooms in or out.

        :param cel_obj: celestial object
        :return: (new_x, new_y)
        """
        new_x = cel_obj.x * self.scale_factor * self.zoom_percent / 100
        new_y = cel_obj.y * self.scale_factor * self.zoom_percent / 100
        new_R = cel_obj.R * self.scale_factor * self.zoom_percent / 100
        return new_x, new_y, new_R

    def change_position(self):
        """
        Move objects x, y.

        :return: None
        """
        for body in self.celestial_bodies:
            x, y, R = self.scale_coordinates(body)
            self.space.coords(body.image, x - R, y - R, x + R, y + R)


if __name__ == '__main__':
    window = Window(600, 600)
    window.run()
