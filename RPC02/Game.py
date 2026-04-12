from math import dist, pow, sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_shape(points):
    # Calcular las longitudes de los lados
    side_lengths = [dist(points[i], points[(i+1)%4]) for i in range(4)]
    
    # Calcular las longitudes de las diagonales
    diag_lengths = [dist(points[i], points[(i+2)%4]) for i in range(2)]
    
    # Verificar si todos los lados son iguales
    all_sides_equal = len(set(side_lengths)) == 1
    
    # Verificar si todas las diagonales son iguales
    all_diags_equal = len(set(diag_lengths)) == 1
    
    # Verificar si los lados opuestos son iguales
    opposite_sides_equal = side_lengths[0] == side_lengths[2] and side_lengths[1] == side_lengths[3]
    
    # Verificar si las diagonales son perpendiculares
    diags_perpendicular = (points[0].x-points[2].x)*(points[1].x-points[3].x) + (points[0].y-points[2].y)*(points[1].y-points[3].y) == 0
    
    if all_sides_equal and diags_perpendicular:
        return "square"
    elif diags_perpendicular and opposite_sides_equal:
        return "rectangle"
    elif all_sides_equal:
        return "rhombus"
    elif opposite_sides_equal:
        return "parallelogram"
    elif all_diags_equal:
        return "kite"
    elif side_lengths[0] == side_lengths[2] or side_lengths[1] == side_lengths[3]:
        return "trapezium"
    else:
        return "none"

points = [Point(*map(int, input().split())) for _ in range(4)]
print(get_shape(points))