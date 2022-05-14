import math

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

    # The final answer is pointVector2
    pointVector2 = PointVector(Point(0, 0), Point(0, 0))

    # If c1 and c2 are on the x-axis
    if (c1.center.y == c2.center.y and c1.center.y == 0):

    #See which circle's center is closer to the origin
        if c1.center.x < c2.center.x :
           ct1 = Circle(Point(c1.center.x, c1.center.y), c1.r)
        else:
            ct1 = Circle(Point(c2.center.x, c2.center.y), c2.r)
        if c1.center.x < c2.center.x:
           ct2 = Circle(Point(c2.center.x, c2.center.y), c2.r)
        else:
            ct2 = Circle(Point(c1.center.x, c1.center.y), c1.r)
    # Center distance double
        l = getDistanceBetweenTwoPoint(ct1.center, ct2.center)

    # Calculate the cosine of the angle formed by the intersection and the x-axis
        cos = (ct1.r * ct1.r + l * l - ct2.r * ct2.r) / (2 * ct1.r * l)
        if cos > 1:
            cos = 0

    # Calculating sin
        sin = math.sqrt(1 - cos * cos)
    # Get the coordinates
        pointVector2.p1.x = ct1.center.x + ct1.r * cos
        pointVector2.p2.x = pointVector2.p1.x
        pointVector2.p1.y = ct1.r * sin
        pointVector2.p2.y = 0 - pointVector2.p1.y


        return pointVector2

    # If c1 and c2 are on the y-axis
    if (c1.center.x == c2.center.x and c1.center.x == 0):

        # See which circle's center is closer to the origin
        if c1.center.y < c2.center.y:
            ct1 = Circle(Point(c1.center.x, c1.center.y), c1.r)
        else:
            ct1 = Circle(Point(c2.center.x, c2.center.y), c2.r)
        if c1.center.y < c2.center.y:
            ct2 = Circle(Point(c2.center.x, c2.center.y), c2.r)
        else:
            ct2 = Circle(Point(c1.center.x, c1.center.y), c1.r)

        # Center distance double
        l = getDistanceBetweenTwoPoint(ct1.center, ct2.center)
        # Calculate the cosine of the angle formed by the intersection and the x-axis
        cos = (ct1.r * ct1.r + l * l - ct2.r * ct2.r) / (2 * ct1.r * l)
        if cos > 1:
            cos = 0

        # Calculating sin
        sin = math.sqrt(1 - cos * cos)
        # Get the coordinates
        pointVector2.p1.y = ct1.center.y + ct1.r * cos
        pointVector2.p2.y = pointVector2.p1.y
        pointVector2.p1.x = ct1.r * sin
        pointVector2.p2.x = 0 - pointVector2.p1.x

        return pointVector2

# If the center of a circle is on the x-axis, the center of a circle is on the y-axis
    if (c1.center.x == 0 and c2.center.y == 0) or (c2.center.x == 0 and c1.center.y == 0):

    # Set the circle on the y-axis to ct1 and the circle on the x-axis to ct2
        if c1.center.x == 0:
            ct1 = Circle(Point(c1.center.x, c1.center.y), c1.r)
        else:
            ct1 = Circle(Point(c2.center.x, c2.center.y), c2.r)

        if c1.center.y == 0:
            ct2 = Circle(Point(c1.center.x, c1.center.y), c1.r)
        else:
            ct2 = Circle(Point(c2.center.x, c2.center.y), c2.r)


    # Center distance double
        l = getDistanceBetweenTwoPoint(ct1.center, ct2.center)

    # Find the cos of a angle
        aCos = (ct1.r * ct1.r + l * l - ct2.r * ct2.r) / (2 * ct1.r * l)
        if aCos > 1:
            aCos = 0
    # Find the arc of the a angle
        aAngle = math.acos(aCos)
    #Find the tan of b
        aTan = ct2.center.x / ct1.center.y

   #Find the arc of the b angle
        bAngle = math.atan(aTan)

    # Get the coordinates
        pointVector2.p1.x = ct1.center.x + math.sin(bAngle - aAngle)
        pointVector2.p1.y = ct1.center.y - math.cos(bAngle - aAngle)
        pointVector2.p2.x = ct1.center.x + math.sin(bAngle + aAngle)
        pointVector2.p2.y = ct1.center.y - math.cos(bAngle - aAngle)

        return pointVector2

    return pointVector2

#Get the center point of three points
def getCenterOfThreePoint(p1, p2, p3):
    return Point((p1.x + p2.x + p3.x)/3, ((p1.y + p2.y + p3.y)/3))

