import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600
RADIUS = 7
num_cells = 50
normal_cell_color = (45, 200, 110)
infected_cell_color = (230, 130, 30)

cells = []


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Vector:
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def add(self, otherVector):
        new = Vector(self.h + otherVector.h, self.v + otherVector.v)
        return new

    def divide(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divideby 0")
        return Vector(self.h / scalar, self.v / scalar)


class Cell:
    def __init__(self, location, velocity, size=RADIUS, infected=False):
        self.location = location
        self.velocity = velocity
        self.size = size
        self.infected = infected
        self.color = normal_cell_color if not infected else infected_cell_color

    def move_cell(self, cells):
        self.location.x += self.velocity.h
        self.location.y += self.velocity.v

        if self.location.x - self.size < 0:
            self.location.x = self.size
            self.velocity.h *= -1
        elif self.location.x + self.size > WIDTH:
            self.location.x = WIDTH - self.size
            self.velocity.h *= -1

            # Bounce off top and bottom walls
        if self.location.y - self.size < 0:
            self.location.y = self.size
            self.velocity.v *= -1
        elif self.location.y + self.size > HEIGHT:
            self.location.y = HEIGHT - self.size
            self.velocity.v *= -1

    def check_collide(self, other):
        distance = math.sqrt((self.location.x - other.location.x) ** 2 + (self.location.y - other.location.y) ** 2)
        if distance < self.size + other.size:
            if self.infected or other.infected:
                self.infected = True
                other.infected = True
                self.color = infected_cell_color
                other.color = infected_cell_color

    def draw_cell(self):
        screen.draw.filled_circle((self.location.x, self.location.y), self.size, self.color)


def draw():
    screen.clear()
    for cell in cells:
        cell.draw_cell()


def update():
    for cell in cells:
        cell.move_cell(cells)

    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            cells[i].check_collide(cells[j])


for i in range(50):
    x, y = random.randint(RADIUS, WIDTH - RADIUS), random.randint(RADIUS, HEIGHT - RADIUS)
    point = Point(x, y)
    h, v = random.uniform(-3, 3), random.uniform(-3, 3)
    vector = Vector(h, v)
    is_infected = (i == 0)
    cells.append(Cell(point, vector, infected=is_infected))

pgzrun.go()
