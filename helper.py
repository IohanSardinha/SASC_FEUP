from shapely import Point
import random

def random_point_inside_polygon(polygon):
    minx, miny, maxx, maxy = polygon.bounds
    while True:
        random_point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(random_point):
            return random_point.x, random_point.y