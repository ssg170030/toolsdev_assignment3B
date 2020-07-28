import sys

import logging
import pymel.core as pm

log = logging.getLogger(__name__)
sys.setrecursionlimit(10 * 6)

    #"""arguments are considered to be numbers"""


class PolyHouse(object):

    def __init__(self, foundation=1,roof_2=1, door_2=1):
        self.bricks = foundation
        self.roof = roof_2
        self.door = door_2
        #self.create_procedural_scene(xPosition, yPosition, zPosition)
    def create_procedural_scene(self, bricks=1, roof=1, door=1):
        self.bricks = pm.polyCube()
        self.roof = pm.polyCone()
        self.door = pm.Cube()

        xform = bricks[1]
        xform.translateZ.set(0)
        xform = roof[1]
        xform.translateY.set(1.0)
        xform = door[1]
        shape = xform.getShape()
        shape.longName()
        shape.name()
        shape.numEdges()
        shape.numVertices()
        xform.translateY.get()



