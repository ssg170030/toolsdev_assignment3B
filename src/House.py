import pymel.core as pmc







class PolyHouse(object):

    """varibles that will be passed into the Low_Poly_City"""
    def __init__(self, foundation='', roof='', door=''):
        self.building_1 = foundation
        self.windows_1 = roof
        self.door_1 = door

    """Storing the polygons into a function"""

    @property
    def create_procedural_House(self, building_1, roof_1, door_1):
        self.bricks = pmc.polyCube()
        self.windows_1 = pmc.polyCube()
        self.door_1 = pmc.polyCube()

        self.var = building_1[1]
        self.var.translate.set(0)
        self.var_2 = roof_1[1]
        self.var_2.translateY.set(5)
        self.var_3 = door_1[1]
        self.var_3.set(1.0)

        shape = self.var.getShape()
        shape.longName()
        shape.name()
        shape.numEdges()
        shape.numVertices()
        self.var.translateY.get()

    """items are stores in var to be used define the size and posistion of 
    each polygon"""
    @property
    def __getitem__(self, item):
        self.var = self.bricks
        self.var_2 = self.windows_1
        self.var_3 = self.door_1