class Block:
    w_x = 10000
    w_y = 30
    w = 1
    h = 1

    def __init__(self, canvas, color):

        block_list = [[1 for i in range(self.w)] for i in range(self.h)]

        self.canvas = canvas

        self.id = [
            self.canvas.create_rectangle(
                i * self.w_x,
                j * self.w_y,
                (i + 1) * self.w_x,
                (j + 1) * self.w_y,
                fill=color,
            )
            for i in range(self.w)
            for j in range(self.h)
        ]

    def draw(self):
        block_pos = [self.canvas.coords(self.id[i]) for i in range(self.w * self.h)]
