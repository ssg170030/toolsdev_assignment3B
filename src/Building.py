import pymel.core as pmc


class PolyBuilding(object):

    def __init__(self, building='', windows='', door=''):
        self.building_1 = building
        self.windows_1 = windows
        self.door_1 = door

    @property
    def create_procedural_Building(self, building_1, windows_1, door_1):
        self.bricks = pmc.polyCube()
        self.windows_1 = pmc.polyCube()
        self.door_1 = pmc.polyCube()

        self.var = building_1[1]
        self.var.translate.set(0)
        self.var_2 = windows_1[1]
        self.var_2.translateY.set(5)
        self.var_3 = door_1[1]
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
