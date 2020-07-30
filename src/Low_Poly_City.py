import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QPushButton

from shiboken2 import wrapInstance

import House
import Building



def maya_main_window():
    """Return the maya main window widget
    small function to create a Window from maya"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class low_poly_city_ui(QtWidgets.QDialog):

    def __init__(self):
        super(low_poly_city_ui, self).__init__(parent=maya_main_window())
        self.scene = House.PolyHouse()
        self.scene_2 = Building.PolyBuilding()
        self.setWindowTitle("Low Poly Buildings")
        self.resize(600, 300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)

        self.display_widgets()
        self.window_layout()
        #self.create_connections()
        self.populate_ui()



        #self.cmd = 'polyCone's

    def display_widgets(self):
        self.title_widget()
        self.building_widget()
        self.size_widget()
        self.house_button()
        self.office_building_button()

    def title_widget(self):
        self.title_lbl = QtWidgets.QLabel("LowPoly Buildings")
        self.title_lbl.setStyleSheet("font: bold 40px")


    def size_widget(self):
        self.size_lbl = QtWidgets.QLabel("size")
        self.size_lbl.setStyleSheet("font: bold 20 px")
        self.size_cmb = QtWidgets.QComboBox()
        self.size_cmb.addItems("5")
        self.size_cmb.addItems(['5', '10', '15', '20', '25'])



    def size_layout(self):
        self.size_layout = QtWidgets.QVBoxLayout()
        self.size_layout.addWidget(self.size_lbl)
        self.size_layout.addWidget(self.size_cmb)
        self.main_layout.addLayout(self.size_layout)




    def building_widget(self):
        self.building_lbl = QtWidgets.QLabel("buildings")
        self.building_lbl.setStyleSheet("font: bold 20px")
        self.building_spinbox = QtWidgets.QSpinBox()
        self.building_spinbox.setValue(1)


    def building_layout(self):
        self.building_layout = QtWidgets.QVBoxLayout()
        self.building_layout.addWidget(self.building_lbl)
        self.building_layout.addWidget(self.building_spinbox)
        self.main_layout.addLayout(self.building_layout)
        self.setLayout(self.main_layout)


    def office_building_button(self):
        self.office_building_lbl = QtWidgets.QLabel()

        self.office_building_btn = QtWidgets.QPushButton()
        self.office_building_btn.setIcon(QtGui.QIcon("D:\\Projects\\toolsdev_assignment3B\\src\\building_image.png"))
        self.office_building_btn.setIconSize(QtCore.QSize(128, 128))

    def office_building_lay(self):
        self.office_lay = QtWidgets.QHBoxLayout()
        self.office_lay.addWidget(self.office_building_btn)
        self.main_layout.addLayout(self.office_lay)




    """Button that create a house Geometry once it is press"""
    def house_button(self):
        self.house_lbl = QtWidgets.QLabel()
        self.house_btn = QtWidgets.QPushButton()
        self.house_btn.setIcon(QtGui.QIcon("D:\\Projects\\toolsdev_assignment3B\\src\\house_image.png"))
        self.house_btn.setIconSize(QtCore.QSize(128, 128))

    """Layout for were the house button is placed"""
    def house_lay(self):
        self.house_buttons_lay = QtWidgets.QHBoxLayout()
        self.house_buttons_lay.addWidget(self.house_btn)
        self.main_layout.addLayout(self.house_buttons_lay)



    """Layouts the house and building buttons"""
    def bottom_buttons(self):
        self.house_lay()
        self.office_building_lay()


    """What the Maya UI will look like as it is layout"""
    def window_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.building_layout()
        self.size_layout()
        self.bottom_buttons()


    @QtCore.Slot()
    def populate_ui(self):
        self.scene.foundation = self.house_btn
        self.scene.roof_2 = self.house_btn
        self.scene.door_2 = self.house_btn



    """
    A connection that executes a house or building button to create the low poly Building 
    
    
    """
    #@QtCore.Slot()
    #def create_connections(self):

     #   self.house_btn.clicked.connect()
      #  self.office_building_btn.click.connect()