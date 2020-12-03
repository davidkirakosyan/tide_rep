import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

from input_and_output import *


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
        self.root.bind('<Configure>', self.resize)
        self.space.bind('<Button-2>', drag_start (self.celestial_bodies))
        self.space.bind('<B2-Motion>', drag (self.celestial_bodies))
        self.space.bind('<ButtonRelease-2>', drag_finish (self.celestial_bodies))
        self.root.mainloop()

    def _set_controllers(self):
        """
        Create controllers for changing parameters. (planets' density, velocity, ...)

        :return:
        """
        self.start_button = tk.Button(self.frame, text="Start", command=self._start_running)
        self.start_button.pack(pady=10)

        load_file = tk.Button(self.frame, text="Open file ...", command=self.open_file)
        save_file = tk.Button(self.frame, text="Save to file ...", command=self.save_to_file)
        save_file.pack(pady=10, side=tk.BOTTOM)
        load_file.pack(pady=10, side=tk.BOTTOM)

        earth_dens, moon_dens = tk.DoubleVar(), tk.DoubleVar()
        earth_dens.set(1000)  # FIXME: set initial densities
        moon_dens.set(1000)
        e_dens_label = tk.Label(self.frame, text='Earth Density', wraplength=(self.width / 5))
        m_dens_label = tk.Label(self.frame, text='Moon Density', wraplength=(self.width / 5))
        self.earth_density = tk.Scale(
            self.frame,
            variable=earth_dens,
            orient=tk.HORIZONTAL,
            from_=1000,
            to=10000,
            resolution=100,
            length=self.width * 0.15,
        )
        self.moon_density = tk.Scale(
            self.frame,
            variable=moon_dens,
            orient=tk.HORIZONTAL,
            from_=1000,
            to=10000,
            resolution=100,
            length=self.width * 0.15,
        )
        e_dens_label.pack(pady=10)
        self.earth_density.pack()
        m_dens_label.pack(pady=10)
        self.moon_density.pack()

        earth_vel, moon_vel = tk.DoubleVar(), tk.DoubleVar()  # in km/s
        earth_vel.set(1)  # FIXME: set initial velocities.
        moon_vel.set(1)
        e_vel_label = tk.Label(self.frame, text='Earth Velocity in km/s', wraplength=(self.width / 5))
        m_vel_label = tk.Label(self.frame, text='Moon Velocity in km/s', wraplength=(self.width / 5))
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
        e_vel_label.pack(pady=10)
        self.earth_velocity.pack()
        m_vel_label.pack(pady=10)
        self.moon_velocity.pack()

    def _start_running(self):
        """
        Changing Start Button text and command, running program.

        :return:
        """
        self.is_running = True
        self.start_button['text'] = 'Pause'
        self.start_button['command'] = self._stop_running

        self.run()

    def drag_start (self, event):
        """
        Grabs an object via clicking on it by mouse
        """
        for body in self.celestial_bodies:
            dist_event_obj = ((event.x - body.x)**2 + (event.y - body.y)**2)**0.5
            if dist_event_obj <= body.R:
                body.drag_readiness = True

    def drag_finish (self, event):
        """
        Releases an object after dragging it by mouse
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
                body.drag_readiness = False
                body.x = event.x
                body.y = event.y

    def drag (self, event):
        """
        moves an object via to dragging it by mouse
        :return: None
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
               body.x = event.x
               body.y = event.y

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

    def resize(self, event):
        """
        Resizes all elements when window size is changed.

        :return:
        """
        init_width, init_height = self.width, self.height
        width_scale, height_scale = self.root.winfo_width() / init_width, self.root.winfo_height() / init_height
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.space.config(width=(0.85 * self.width), height=self.height)
        self.space.scale("all", 0 / 2, 0 / 2, width_scale, height_scale)

        self.frame.config(width=(0.15 * self.width), height=self.height)

    def open_file(self):
        """
        Opens a file and reads planets' datas.

        :return:None
        """
        file_address = askopenfile(filetypes=(("Text file", ".txt"),))
        # TODO: open file and get data

        self._start_running()

    def save_to_file(self):
        """
        Saves planets' data after simulation.
        <type> <R> <color> <mass> <x> <y> <Vx> <Vy>

        :return: None
        """
        self._stop_running()

        file_name = asksaveasfile(filetypes=(("Text file", ".txt"),))
        write_space_objects_data_to_file(file_name.name, self.celestial_bodies)


if __name__ == '__main__':
    window = Window(800, 700)
    window.run()
