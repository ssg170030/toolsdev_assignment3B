import pymel.core as pmc


class PolyBuilding(object):

    """varibles used for each shape
    building polyCube
    windows smaller polyCubes"""
    def __init__(self, building='', windows='', door=''):
        self.building_1 = building
        self.windows_1 = windows
        self.door_1 = door


    """Storing the polygons into a function"""
    @property
    def create_procedural_Building(self):
        self.var = self.building_1[1]
        self.var.translate.set(0)
        self.var_2 = self.windows_1[1]
        self.var_2.translateY.set(5)
        self.var_3 = self.door_1[1]
        self.var_3.set(1.0)

        shape = self.var.getShape()
        shape.longName()
        shape.name()
        shape.numEdges()
        shape.numVertices()
        self.var.translateY.get()

    @property
    def __getitem__(self, item):
        self.var = self.bricks
        self.var_2 = self.windows_1
        self.var_3 = self.door_1