"""
Python Data Structures and Algorithms - A Game-Based Approach
Helper functions and values for use with other files in this project.
Robin Andrews - https://compucademy.net/
"""

offsets = {
    "right": (1, 0),
    "left": (-1, 0),
    "down": (0, -1),
    "up": (0, 1),
    "down_right": (1,-1),
    "up_right": (1,1),
    "down_left": (-1,-1),
    "up_left": (-1,1)
}


def is_legal_pos(pos):
    x, y = pos
    x_max = 400
    y_max = 300
    
    if x in range(0, x_max) and y in range(0, y_max):
        
        if (x - 90)**2 + (y - 70)**2 <= 35**2:
            return False
        
        elif y >=  -1.43*x + 176.58 and y >=  -1.43*x + 438.05 and y >=  0.7*x + 74.39 and y >=  0.7*x + 98.8:
            return False
        
        # elif y >=  -1.43*x + 176.58 and y >=  -1.43*x + 438.05 and y >=  0.7*x + 74.39 and y >=  0.7*x + 98.8:
        #     return False
        
        # elif y >=  -1.43*x + 176.58 and y >=  -1.43*x + 438.05 and y >=  0.7*x + 74.39 and y >=  0.7*x + 98.8:
        #     return False
        
        elif ((x - 246)/60)**2 + ((y - 175)/30)**2 <= 1:
            return False
        
        else:
            return True
        
    else:
        return False
    

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
