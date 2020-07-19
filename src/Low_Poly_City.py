import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore

from shiboken2 import wrapInstance

import House


def maya_main_window():
    """Return the maya main window widget
    small function to create a Window from maya"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class low_poly_city_ui(QtWidgets.QDialog):

    def __init__(self):
        super(low_poly_city_ui, self).__init__(parent=maya_main_window())
        self.scene = House.PolyHouse()
        self.setWindowTitle("Low Poly Buildings")

        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.resize(500, 200)
        self.display_widgets()
        self.window_layout()
        self.create_layout()



        #self.cmd = 'polyCone'

    def display_widgets(self):
        self.title_widget()
        self.create_widgets()

    def title_widget(self):
        self.title_lbl = QtWidgets.QLabel("LowPoly Buildings")
        self.title_lbl.setStyleSheet("font: bold 40px")

    def create_widgets(self):
        self.x_lbl = QtWidgets.QLabel("position")

    def create_layout(self):
        self.create_layouts = QtWidgets.QHBoxLayout()
        self.create_layouts.addWidget(self.x_lbl)
        self.main_layout.addLayout(self.create_layouts)
        self.setLayout(self.main_layout)


    def window_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.create_layout()