import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

from input_and_output import *


class Window:
    def __init__(self, width, height, zoom_percent=100):
        self.width = width
        self.height = height
        self.zoom_percent = zoom_percent
        self.is_running = False
        self.scale_factor = 1.0

        self.root = tk.Tk()
        self.root.title('Tidal Effects')
        self.root.geometry("{}x{}".format(self.width, self.height))

        self.space = tk.Canvas(self.root, width=(0.85 * self.width),
                               height=self.height, bg='black')
        self.space.pack(side=tk.LEFT)
        self.frame = tk.Frame(self.root, width=(0.15 * self.width))
        self.frame.pack(fill=tk.X, side=tk.LEFT, expand=1)

        self.celestial_bodies = []

        self._set_controllers()

        self.space.bind('<ButtonPress>', self.zoom)
        self.root.bind('<Configure>', self.resize)
        self.space.bind('<Button-1>', self.drag_start)
        self.space.bind('<B1-Motion>', self.drag)
        self.space.bind('<ButtonRelease-1>', self.drag_finish)
        self.root.mainloop()

    def _set_controllers(self):
        """
        Create controllers for changing parameters. (planets' density, velocity, ...)

        :return:
        """
        self.start_button = tk.Button(self.frame, text="Start", command=self._start_running)
        self.start_button.pack(pady=10)

        load_file = tk.Button(self.frame, text="Open file ...", command=self.upload_data)
        save_file = tk.Button(self.frame, text="Save to file ...", command=self.save_to_file)
        save_file.pack(pady=10, side=tk.BOTTOM)
        load_file.pack(pady=10, side=tk.BOTTOM)

        mass_labels = [
            tk.Label(self.frame, text='Earth Mass in 10^22', wraplength=(self.width / 5)),
            tk.Label(self.frame, text='Moon Mass in 10^22', wraplength=(self.width / 5))
        ]
        self.mass_sliders = [
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=1000,
                resolution=10,
                length=self.width * 0.15,
                command=lambda value: self.change_mass(value, 0),
            ),
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=1000,
                resolution=10,
                length=self.width * 0.15,
                command=lambda value: self.change_mass(value, 1),
            )
        ]
        for label, slider in zip(self.mass_sliders, mass_labels):
            label.pack(pady=10)
            slider.pack()

        vel_labels = [
            tk.Label(self.frame, text='Earth Velocity in km/s', wraplength=(self.width / 5)),
            tk.Label(self.frame, text='Moon Velocity in km/s', wraplength=(self.width / 5)),
        ]
        self.velocity_sliders = [
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=30,
                length=self.width * 0.15,
                command=lambda value: self.change_velocity(value, 0),
            ),
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=30,
                length=self.width * 0.15,
                command=lambda value: self.change_velocity(value, 1),
            )
        ]

        for label, slider in zip(self.velocity_sliders, vel_labels):
            label.pack(pady=10)
            slider.pack()

    def _start_running(self):
        """
        Changing Start Button text and command, running program.

        :return:
        """
        self.is_running = True
        self.start_button['text'] = 'Pause'
        self.start_button['command'] = self._stop_running

        self.run()

    def drag_start(self, event):
        """
        Grabs an object via clicking on it by mouse
        """
        for body in self.celestial_bodies:
            x, y, R = self.scale_coordinates(body)
            dist_event_obj = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
            if dist_event_obj <= R:
                body.drag_readiness = True

    def drag_finish(self, event):
        """
        Releases an object after dragging it by mouse
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
                body.drag_readiness = False
                x = (event.x - self.space.winfo_width() / 2) * 100 / (self.scale_factor * self.zoom_percent)  # coords rescaling
                y = (event.y - self.space.winfo_height() / 2) * 100 / (self.scale_factor * self.zoom_percent)
                body.x = x
                body.y = y
                x, y, R = self.scale_coordinates(body)
                self.space.coords(body.image, x - R, y - R, x + R, y + R)

    def drag(self, event):
        """
        moves an object via to dragging it by mouse
        :return: None
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
                x = (event.x - self.space.winfo_width() / 2) * 100 / (self.scale_factor * self.zoom_percent)  # coords rescaling
                y = (event.y - self.space.winfo_height() / 2) * 100 / (self.scale_factor * self.zoom_percent)
                body.x = x
                body.y = y
                x, y, R = self.scale_coordinates(body)
                self.space.coords(body.image, x - R, y - R, x + R, y + R)

    def run(self):
        """
        Moves objects, changes coordinates.

        :return: None
        """
        if self.is_running:
            self.change_position()
            self.root.after(1, self.run)

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
            elif event.num == 4 and self.zoom_percent < 200:  # Scroll up
                self.zoom_percent += 10

    def scale_coordinates(self, cel_obj):
        """
        Scales cel_obj's x, y, when user zooms in or out.

        :param cel_obj: celestial object
        :return: (new_x, new_y)
        """
        new_x = cel_obj.x * self.scale_factor * self.zoom_percent / 100 + self.space.winfo_width() / 2
        new_y = cel_obj.y * self.scale_factor * self.zoom_percent / 100 + self.space.winfo_height() / 2
        new_R = cel_obj.R * self.scale_factor * self.zoom_percent / 100
        return new_x, new_y, new_R

    def change_position(self):
        """
        Move objects x, y.

        :return: None
        """
        dt = 800
        for body in self.celestial_bodies:
            body.move(self.celestial_bodies, dt)
            x, y, R = self.scale_coordinates(body)
            self.space.coords(body.image, x - R, y - R, x + R, y + R)

    def resize(self, event):
        """
        Resizes all elements when window size is changed.

        :return:
        """
        init_width, init_height = self.width, self.height
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        width_scale, height_scale = self.width / init_width, self.height / init_height

        self.space.config(width=(0.85 * self.width), height=self.height)
        self.space.scale("all", 0, 0, width_scale, height_scale)
        self.scale_factor *= width_scale

        self.frame.config(width=(0.15 * self.width), height=self.height)

    def upload_data(self):
        """
        Reads planets' data. Creates planets and water molecules.

        :return:None
        """
        self._stop_running()
        self.celestial_bodies.clear()
        self.space.delete("all")

        try:
            file_name = askopenfile(filetypes=(("Text file", ".txt"),)).name
        except AttributeError:
            raise ValueError("Please upload a file")

        self.celestial_bodies.extend(read_space_objects_data_from_file(file_name))
        self.celestial_bodies.sort(key=lambda obj: obj.m, reverse=True)

        # adding water molecules
        self.celestial_bodies.extend(create_water(self.celestial_bodies[0]))

        for i, body in enumerate(self.celestial_bodies):
            body.create_image(self.space)
            if body.type != 'water':
                self.mass_sliders[i].set(body.m / 1E22)
                V = (body.Vx ** 2 + body.Vy ** 2) ** 0.5
                self.velocity_sliders[i].set(V / 1000)

        max_x_or_y = max(
            max([(body.x, body.y) for body in self.celestial_bodies],
                key=lambda c: (c[0] ** 2 + c[1] ** 2))
        )
        self.scale_factor = 0.4 * (self.width * 0.8) / max_x_or_y  # 0.4 canvas width / max coordinate

        self._start_running()

    def save_to_file(self):
        """
        Saves planets' data after simulation.
        <type> <R> <color> <mass> <x> <y> <Vx> <Vy>

        :return: None
        """
        self._stop_running()

        file_name = asksaveasfile(filetypes=(("Text file", ".txt"),)).name
        write_space_objects_data_to_file(file_name, self.celestial_bodies)

    def change_mass(self, value, i):
        """
        Changes body's mass when slider is moved.

        :param value: slider's current value
        :param i: index of body
        :return: None
        """
        if len(self.celestial_bodies) > 0:
            self.celestial_bodies[i].m = float(value) * 1E22

    def change_velocity(self, value, i):
        """
        Changes body's full velocity when slider is moved.

        :param value: slider's current value
        :param i: index of body
        :return: None
        """
        if len(self.celestial_bodies) > 0:
            Vx, Vy = self.celestial_bodies[i].Vx, self.celestial_bodies[i].Vy
            V_init = (Vx ** 2 + Vy ** 2) ** 0.5
            V_new = float(value) * 1000
            self.celestial_bodies[i].Vx *= V_new / V_init
            self.celestial_bodies[i].Vy *= V_new / V_init


if __name__ == '__main__':
    window = Window(800, 700)
    window.run()
