import math
import generate_env
import numpy as np

BROWN = (147, 108, 1)
DARK_GREY = (46, 45, 43)
GREY = (66, 65, 63)  
OFF_WHITE = (248, 240, 227)
FOOD_GREEN = (111, 194, 118)  # Soft Green
POISON_PURPLE = (127, 1, 254)  # Deep Purple
OBSTACLE_BLACK = (0, 0, 0)  # Black
CHEMOATTRACTANT_YELLOW = (250, 237, 39)  # Soft Yellow
CHEMOREPELLENT_RED = (87, 14, 14)  # Dark Red


# Axial Coordinates
class Hexagon:
    def __init__(self, x, y, color=OFF_WHITE):
        self.x = x
        self.y = y
        self.q = x
        self.r = y - (x + (x & 1)) // 2
        self.color = color
        self.neighbors = []
        self.channels = {
            'food': 0,
            'poison': 0,
            'obstacle': 0,
            'chemoattractant': 0,
            'chemorepellant': 0
        }        

    def add_neighbor(self, key):
        self.neighbors.append(key)
    
    def get_vertices(self, hexagon_size): # for visualization
        x = hexagon_size * 3/2 * self.q
        y = hexagon_size * (math.sqrt(3) / 2 * self.q + math.sqrt(3) * self.r)
        
        vertices = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            vertex_x = x + hexagon_size * math.cos(angle_rad)
            vertex_y = y + hexagon_size * math.sin(angle_rad)
            vertices.append((vertex_x, vertex_y))
        
        return vertices

    
class HexagonGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.generate_map()


    def generate_map(self):
        hexagon_array = np.empty((self.height, self.width), dtype=object)
        for x in range(self.width):
            for y in range(self.height):
                if x % 2 == 0:
                    color = OFF_WHITE
                else:
                    color = OBSTACLE_BLACK
                hexagon = Hexagon(x, y, color)
                hexagon_array[y][x] = hexagon
        return hexagon_array
    

    # Specificially for pygame coords
    def hexagon_clicked(self, mouse_pos, screen_width, screen_height): 
        # Convert mouse position to relative position within the grid
        relative_x = mouse_pos[0] - screen_width / 2
        relative_y = mouse_pos[1] - screen_height / 2

        # Calculate axial coordinates based on relative position and hexagon size
        q = (2 / 3 * relative_x) / self.hexagon_size
        r = (-1 / 3 * relative_x + math.sqrt(3) / 3 * relative_y) / self.hexagon_size

        # Iterate through hexagons and find the clicked hexagon
        for hexagon in self.hexagons.values():
            if hexagon.q == round(q) and hexagon.r == round(r):
                return hexagon

        return None




# Example usage
# grid = HexagonGrid(radius=3)
# for key in grid.hexagons:
#     hex = grid.hexagons[key]
#     neighbors = hex.neighbors
#     print(f"{key}: {neighbors}")









