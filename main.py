import tkinter as tk


class Window:
    def __init__(self, width, height, zoom_percent=100):
        self.width = width
        self.height = height
        self.zoom_percent = zoom_percent

        self.root = tk.Tk()
        self.root.title('Tidal Effects')

        self.space = tk.Canvas(self.root, width=(0.9 * self.width),
                               height=self.height, bg='black')
        self.space.pack(side=tk.LEFT)
        self.frame = tk.Frame(self.root, width=(0.1 * self.width))
        self.frame.pack(side=tk.RIGHT)

        self.celestial_bodies = []  # TODO: add all elements

    def run(self):
        """
        Handles all events, and runs root.mainloop()

        :return: None
        """

        self.space.bind('<ButtonPress>', self.zoom)
        self.root.mainloop()

    def zoom(self, event):
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
        new_x = cel_obj.x * self.zoom_percent / 100
        new_y = cel_obj.y * self.zoom_percent / 100
        return new_x, new_y

    def change_position(self):
        """
        Move objects x, y.

        :return: None
        """
        for body in self.celestial_bodies:
            x, y = self.scale_coordinates(body)
            r = body.r
            self.space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == '__main__':
    window = Window(600, 600)
    window.run()
