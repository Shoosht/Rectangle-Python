import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def input_and_write_coordinates(file_name):
    print("Enter coordinates in the format 'x,y'")

    coordinates = []
    for i in range(4):
        coordinate = input(f"Enter coordinate {i}: ")
        coordinates.append(coordinate)

    with open(file_name, "w") as file:
        for i, coordinate in enumerate(coordinates):
            if i < len(coordinates) - 1:
                file.write(coordinate + '\n')
            else:
                file.write(coordinate)

def read_points_from_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read().replace(" ", "").replace("\n", ",")
        coordinates = text.strip().split(',')
    return coordinates

def create_points(coordinates):
    points = []
    for i in range(0, len(coordinates), 2):
        temp = Point(int(coordinates[i]), int(coordinates[i+1]))
        points.append(temp)
    return points

def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def possible_rectangle(points):
    distanceAB = calculate_distance(points[0], points[1])
    distanceAC = calculate_distance(points[0], points[2])
    distanceBC = calculate_distance(points[1], points[2])

    rectangle_diagonal = max(distanceAB, distanceAC, distanceBC)

    rectangle_flag = False

    while not rectangle_flag:
        angleABtoAC = (distanceAB**2 + distanceAC**2 - distanceBC**2) / (2 * distanceAB * distanceAC)
        angle1 = math.acos(angleABtoAC)
        if abs(math.degrees(angle1) - 90.0) < 0.00001:
            rectangle_flag = True
        
        angleACtoBC = (distanceAC**2 + distanceBC**2 - distanceAB**2) / (2 * distanceAC * distanceBC)
        angle2 = math.acos(angleACtoBC)
        if abs(math.degrees(angle2) - 90.0) < 0.00001:
            rectangle_flag = True

        angleABtoBC = (distanceAB**2 + distanceBC**2 - distanceAC**2) / (2 * distanceAB * distanceBC)
        angle3 = math.acos(angleABtoBC)
        if abs(math.degrees(angle3) - 90.0) < 0.00001:
            rectangle_flag = True
        
        break

    return rectangle_flag, rectangle_diagonal

def min_max_coordinates(points):
    min_x = points[0].x
    max_x = points[0].x
    min_y = points[0].y
    max_y = points[0].y
    
    for point in points[1:]:
        if point.x < min_x:
            min_x = point.x
        elif point.x > max_x:
            max_x = point.x
        
        if point.y < min_y:
            min_y = point.y
        elif point.y > max_y:
            max_y = point.y
    
    return min_x, max_x, min_y, max_y

def is_point_X_in_rectangle(points, x):
    min_x, max_x, min_y, max_y = min_max_coordinates(points)

    if min_x < points[x].x < max_x and min_y < points[x].y < max_y:
        print(True)
    else:
        print(False)

def main():
    file_name = "data.txt"
    point_x = 3

    input_and_write_coordinates(file_name)

    coordinates = read_points_from_file(file_name)

    points = create_points(coordinates)

    rectangle, hypotenuse = possible_rectangle(points)
    if rectangle is not True:
        print("The three points cannot form a rectangle.")
        sys.exit(1)
    
    is_point_X_in_rectangle(points, point_x)

    print("The diagonal length of the three point rectangle is", hypotenuse)

if __name__ == "__main__":
    main()
