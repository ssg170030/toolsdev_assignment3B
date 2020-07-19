import logging
import maya.cmds  as mc
import pymel.core as pmc
from pymel.core.system import Path

log = logging.getLogger(__name__)

class PolyHouse(object):


    def __index__(self, x = '', y= '', w= '' , h= ''):

        self.x = 10
        self.y =10
        self.w=10
        self.h=10

    @property
    def x(self):
        print('getting')
        self.x = mc
        return

    @property
    def y(self):
        print('getting')
        self.y = mc
        return

    @property
    def w(self):
        print('getting')
        self.x = mc
        return

    @property
    def h(self):
        print('getting')
        self.x = mc
        return