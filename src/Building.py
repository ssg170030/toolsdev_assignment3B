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

        xform = building_1[1]
        xform.translate.set(0)
        xform = windows_1[1]
        xform.translateY.set(5)
        xform = door_1[1]
        xform.translateY.set(1.0)

        shape = xform.getShape()
        shape.longName()
        shape.name()
        shape.numEdges()
        shape.numVertices()
        xform.translateY.get()
