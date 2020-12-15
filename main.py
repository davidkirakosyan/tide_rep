import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

from input_and_output import *
from objects import *


class Window:
    def __init__(self, width, height, zoom_percent=100):
        self.width = width
        self.height = height
        self.zoom_percent = zoom_percent
        self.x0, self.y0 = [0] * 2
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
        self.ocean = []
        self.showing_ocean = tk.BooleanVar()
        self.showing_ocean.set(False)

        self.fps = tk.DoubleVar()
        self.fps.set(100)

        self._set_controllers()

        self.space.bind('<ButtonPress>', self.zoom)  # For Linux
        self.space.bind('<MouseWheel>', self.zoom)  # For Windows and MacOS
        self.root.bind('<Configure>', self.resize)
        self.space.bind('<Button-1>', self.drag_start)
        self.space.bind('<B1-Motion>', self.drag)
        self.space.bind('<ButtonRelease-1>', self.drag_finish)
        self.job = None
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self._stop_running()
        if self.job:
            self.root.after_cancel(self.job)
        self.root.destroy()

    def _set_controllers(self):
        """
        Create controllers for changing parameters. (planets' density, velocity, ...)
        :return:
        """
        self.start_button = tk.Button(self.frame, text="Start", command=self._start_running)
        self.start_button.pack(pady=6)

        load_file = tk.Button(self.frame, text="Open file ...", command=self.upload_data)
        save_file = tk.Button(self.frame, text="Save to file ...", command=self.save_to_file)
        save_file.pack(pady=6, side=tk.BOTTOM)
        load_file.pack(pady=6, side=tk.BOTTOM)

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
                length=(self.width * 0.15),
                command=lambda value: self.change_mass(value, 0),
            ),
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=1000,
                resolution=10,
                length=(self.width * 0.15),
                command=lambda value: self.change_mass(value, 1),
            )
        ]
        for label, slider in zip(self.mass_sliders, mass_labels):
            label.pack(pady=6)
            slider.pack()

        vel_labels = [
            tk.Label(self.frame, text='Earth Velocity in m/s', wraplength=(self.width / 5)),
            tk.Label(self.frame, text='Moon Velocity in m/s', wraplength=(self.width / 5)),
        ]
        self.velocity_sliders = [
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=2300,
                length=(self.width * 0.15),
                command=lambda value: self.change_velocity(value, 0),
            ),
            tk.Scale(
                self.frame,
                variable=tk.DoubleVar(),
                orient=tk.HORIZONTAL,
                from_=1,
                to=2300,
                length=(self.width * 0.15),
                command=lambda value: self.change_velocity(value, 1),
            )
        ]

        for label, slider in zip(self.velocity_sliders, vel_labels):
            label.pack(pady=6)
            slider.pack()

        fps_label = tk.Label(self.frame, text="FPS", wraplength=(self.width / 5))
        fps_label.pack(pady=6)
        fps_scale = tk.Scale(
            self.frame,
            variable=self.fps,
            orient=tk.HORIZONTAL,
            from_=10,
            to=500,
            resolution=10,
            length=self.width * 0.15,
        )
        fps_scale.pack()

        ocean_check = tk.Checkbutton(self.frame, text="Ocean On/Off", variable=self.showing_ocean,
                                     onvalue=True, offvalue=False, command=self.show_ocean)
        ocean_check.pack(pady=6)

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
<<<<<<< HEAD
=======

>>>>>>> 0d8e3aba32f6cc88979e50965fc4539cef37b7e0
        :return: None
        """
        if self.is_running:
            self.change_position()
            self.job = self.root.after(int(1000 / self.fps.get()), self.run)

    def _stop_running(self):
        """
        Changing Start Button text and command, running program.
<<<<<<< HEAD
=======

>>>>>>> 0d8e3aba32f6cc88979e50965fc4539cef37b7e0
        :return:
        """
        self.is_running = False
        self.start_button['text'] = 'Start'
        self.start_button['command'] = self._start_running

    def update_screen(self):
        """
        Updates Canvas, when program is paused.
<<<<<<< HEAD
=======

>>>>>>> 0d8e3aba32f6cc88979e50965fc4539cef37b7e0
        :return: None
        """
        if not self.is_running:
            for body in self.celestial_bodies + self.ocean:
                x, y, R = self.scale_coordinates(body)
                self.space.coords(body.image, x - R, y - R, x + R, y + R)

    def drag_start(self, event):
        """
        Grabs an object via clicking on it by mouse
        """
        for body in self.celestial_bodies:
            x, y, R = self.scale_coordinates(body)
            dist_event_obj = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
            if dist_event_obj <= R:
                body.drag_readiness = True
                break  # grab only one object

        dragging_planet = any([body.drag_readiness for body in self.celestial_bodies])
        if not dragging_planet:
            self.start_x0 = event.x - self.x0
            self.start_y0 = event.y - self.y0

        dragging_planet = any([body.drag_readiness for body in self.celestial_bodies])
        if not dragging_planet:
            self.start_x0 = event.x - self.x0
            self.start_y0 = event.y - self.y0

    def drag_finish(self, event):
        """
        Releases an object after dragging it by mouse
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
                body.drag_readiness = False

    def drag(self, event):
        """
        moves an object via to dragging it by mouse
        :return: None
        """
        for body in self.celestial_bodies:
            if body.drag_readiness:
                # coords rescaling
                x = (event.x - self.space.winfo_width() / 2 - self.x0) * \
                    100 / (self.scale_factor * self.zoom_percent)
                y = (event.y - self.space.winfo_height() / 2 - self.y0) * \
                    100 / (self.scale_factor * self.zoom_percent)
                body.x = x
                body.y = y
                x, y, R = self.scale_coordinates(body)
                self.space.coords(body.image, x - R, y - R, x + R, y + R)

        dragging_planet = any([body.drag_readiness for body in self.celestial_bodies])
        #  dragging background
        if not dragging_planet:
            self.x0 = event.x - self.start_x0
            self.y0 = event.y - self.start_y0

        self.update_screen()

    def zoom(self, event):
        if (event.num == 5 or event.delta < 0) and self.zoom_percent > 50:  # Scroll down
            self.zoom_percent -= 10
        elif (event.num == 4 or event.delta > 0) and self.zoom_percent < 400:  # Scroll up
            self.zoom_percent += 10

        self.update_screen()

    def scale_coordinates(self, cel_obj):
        """
        Scales cel_obj's x, y, when user zooms in or out.
        :param cel_obj: celestial object
        :return: (new_x, new_y)
        """
        new_x = cel_obj.x * self.scale_factor * self.zoom_percent / 100 + self.space.winfo_width() / 2 + self.x0
        new_y = cel_obj.y * self.scale_factor * self.zoom_percent / 100 + self.space.winfo_height() / 2 + self.y0
        new_R = cel_obj.R * self.scale_factor * self.zoom_percent / 100
        return new_x, new_y, new_R

    def change_position(self):
        """
        Move objects x, y.
        :return: None
        """
        dt = 800
        all_objects = self.celestial_bodies + self.ocean
        for body in all_objects:
            body.move(all_objects, dt)
            self.change_sliders_value()
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
        self.ocean.clear()
        self.space.delete("all")

        try:
            file_name = askopenfile(filetypes=(("Text file", ".txt"),)).name
        except AttributeError:
            raise ValueError("Please upload a file")

        self.celestial_bodies.extend(read_space_objects_data_from_file(file_name))
        self.celestial_bodies.sort(key=lambda obj: obj.m, reverse=True)

        for i, body in enumerate(self.celestial_bodies):
            body.create_image(self.space)
            self.mass_sliders[i].set(body.m / 1E22)

        self.change_sliders_value()  # adjusting velocity sliders

        for molecule in self.ocean:
            molecule.create_image(self.space)

        max_x_or_y = max(
            max([(body.x, body.y) for body in self.celestial_bodies + self.ocean],
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
            V_new = float(value)
            self.celestial_bodies[i].Vx *= V_new / V_init
            self.celestial_bodies[i].Vy *= V_new / V_init

    def show_ocean(self):
        """
        If Check box is checked fills self.ocean list.
        :return: None
        """
        if self.showing_ocean.get():
            self.ocean.extend(create_water(self.celestial_bodies[0]))
            for molecule in self.ocean:
                molecule.create_image(self.space)

            self.update_screen()
        else:
            for molecule in self.ocean:
                self.space.delete(molecule.image)
            self.ocean.clear()

    def change_sliders_value(self):
        """
        Changes velocity slider values when celestial bodies are moving.
        :return: None
        """
        for i, body in enumerate(self.celestial_bodies):
            V = (body.Vx ** 2 + body.Vy ** 2) ** 0.5
            self.velocity_sliders[i].set(V)


if __name__ == '__main__':
    window = Window(800, 700)
    window.run()
