#arucomarker object, designed to keep track of the id and pixel coordinates of each marker
class Marker:
    def __init__(self, id, corner1, corner2, corner3, corner4):
        self.id = id
        self.corner1 = corner1
        self.corner2 = corner2
        self.corner3 = corner3
        self.corner4 = corner4
