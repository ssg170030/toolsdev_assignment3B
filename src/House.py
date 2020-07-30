import sys
import logging
import pymel.core as pm

log = logging.getLogger(__name__)
sys.setrecursionlimit(10 * 6)

    #"""arguments are considered to be numbers"""


class PolyHouse(object):



    """Creates the house out of Polygons"""
    @property
    def create_procedural_scene(self):


        value = pm.polyCube(name='House')[0]

        value.translateY.set(0.3)

    @create_procedural_scene.setter
    def create_procedural_scene(self, value):
        self._create_procedural_scene = value