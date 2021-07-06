import numpy as np
import matplotlib.pyplot as plt

class CellularAutomata(object):
    def __init__(self, dim = 25):
        self.dim = dim
        self.grid = np.zeros((self.dim, self.dim))
        for y in range(self.dim):
            for x in range(self.dim):
                if y == x:
                    self.grid[y][x] = 1


    
    def generate(self, gens = 150, show = 2):
        images = []
        if show != 0:
            self.show()
        def convert_to_grayscale(x):
            if x == 1:
                return 255
            return x
        self.convert = np.vectorize(convert_to_grayscale)
        
        for gen in range(gens):
            self.update()
            img_arr = np.array(self.grid)
            img_arr = self.convert(img_arr).astype(np.uint8)
            images.append(img_arr)
            if show != 0 and gen % show == 0:
                self.show()
        return images

        
    def update(self):
        updates = []
        left_x, right_x = -1, 2
        left_y, right_x = -1, 2
        num_alive = self.grid[:2,:2].sum()
        for cell_y in range(self.dim):
            left_y, right_y = max(cell_y - 1, 0), min(cell_y + 2, self.dim)
            for cell_x in range(self.dim):
                left_x, right_x = max(cell_x - 1, 0), min(cell_x + 2, self.dim)
                num_alive = self.grid[left_y:right_y, left_x:right_x].sum()
                next_state = int(num_alive < 4 and num_alive > 1)
                if next_state != self.grid[cell_y][cell_x]:
                    updates.append((cell_y, cell_x))
        for y, x in updates:
            self.grid[y][x] = not(self.grid[y][x])              


    def show(self, title = None):
        if title:
            plt.title(title)
        plt.imshow(self.grid, cmap='gray')
        plt.show()