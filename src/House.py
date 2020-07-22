import logging
import maya.cmds as mc
import pymel.core as pmc


log = logging.getLogger(__name__)


class PolyHouse(object):

    def makeObject(self):
        mc.polyCube()
        pmc.polyCone()


    def __init__(self, x=1, y=1, w=1, h=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = 10

    @property
    def x(self):
        self.x = mc.polyCube
        return

    def y(self):
        self.y = 1

    def w(self):
        self.w = 1

    @x.setter
    def x(self, value):
        self._x = value


