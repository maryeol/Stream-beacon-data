import math
from cmath import sqrt

RSSI_TO_DISTANCE_A = 60
RSSI_TO_DISTANCE_N = 3.3

class Point:
    x: float
    y: float
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])



class PointVector:
    p1: Point
    p2: Point
    def __init__(self, p1, p2):
        self.p1 = Point(p1.x, p1.y)
        self.p2 = Point(p2.x, p2.y)

class Circle:
    r: float
    def __init__(self, center, r):
        self.center = Point(center.x, center.y)
        self.r = r

    def __repr__(self):
        return "".join(["Circle(", str(self.center), ", r = ", str(self.r), ")"])



#Method to calculate Distance to Signal strength
def calculate(rssi):
    return ((0.882909233)* pow((rssi/-58),4.57459326)+0.045275821)


#Get the distance between two points
def getDistanceBetweenTwoPoint(a, b):
    return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))

#Determine if the two circles intersect
def isTwoCircleIntersect(c1, c2):
    return getDistanceBetweenTwoPoint(c1.center, c2.center) < c1.r + c2.r

#Find the intersection of two intersecting circles

def getIntersectionPointsOfTwoIntersectCircle(c1, c2):

    #the final answer is pointVector2
    pointVector2 = PointVector(Point(0, 0), Point(0, 0))
    x0 = c1.center.x
    y0 = c1.center.y
    r0 = c1.r
    x1 = c2.center.x
    y1 = c2.center.y
    r1 = c2.r
    d = getDistanceBetweenTwoPoint(c1.center, c2.center)
    #non intersecting
    if d > r0 + r1:
        return None
    #One circle within other
    if d < abs(r0 - r1):
        return None
    #coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        pointVector2.p1.x = x3
        pointVector2.p1.y = y3

        pointVector2.p2.x = x4
        pointVector2.p2.y = y4

    return pointVector2

#Get the center point of three points
def getCenterOfThreePoint(p1, p2, p3):
    return Point((p1.x + p2.x + p3.x)/3, ((p1.y + p2.y + p3.y)/3))

