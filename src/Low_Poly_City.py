import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtGui, QtCore

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
        self.resize(600, 300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)

        self.display_widgets()
        self.window_layout()
        self.create_connections()




        #self.cmd = 'polyCone'

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
        self.y_lbl = QtWidgets.QLabel("size")
        self.y_cmb = QtWidgets.QComboBox()
        self.y_cmb.addItems("5")
        self.y_cmb.addItems(['5', '10', '15', '20', '25'])
        self.y_lbl.setStyleSheet("font: bold 20 px")


    def size_layout(self):
        self.size_layout = QtWidgets.QVBoxLayout()
        self.size_layout.addWidget(self.y_lbl)
        self.size_layout.addWidget(self.y_cmb)
        self.main_layout.addLayout(self.size_layout)




    def building_widget(self):
        self.x_lbl = QtWidgets.QLabel("buildings")
        self.x_spinbox = QtWidgets.QSpinBox()
        self.x_spinbox.setValue(1)
        self.x_lbl.setStyleSheet("font: 20px")

    def building_layout(self):
        self.building_layout = QtWidgets.QVBoxLayout()
        self.building_layout.addWidget(self.x_lbl)
        self.building_layout.addWidget(self.x_spinbox)
        self.main_layout.addLayout(self.building_layout)
        #self.setLayout(self.main_layout)


    def office_building_button(self):
        self.office_building_lbl = QtWidgets.QLabel()
        self.office_building_lbl.setPixmap(QtGui.QPixmap('building_image.png'))
        self.office_building_btn = QtWidgets.QPushButton()
        self.office_building_btn.setIcon(QtGui.QIcon("building_image.png"))
        self.office_building_btn.setIconSize(QtCore.QSize(32, 32))

    def office_building_lay(self):
        self.office_lay = QtWidgets.QVBoxLayout()
        self.office_lay.addWidget(self.office_building_lbl)
        self.office_lay.addWidget(self.office_building_btn)
        self.main_layout.addLayout(self.office_lay)




    def house_button(self):
        self.house_lbl = QtWidgets.QLabel()
        self.house_lbl.setPixmap(QtGui.QPixmap("house_image.png"))
        self.house_btn = QtWidgets.QPushButton()
        self.house_btn.setIcon(QtGui.QIcon("house_image.png"))
        self.house_btn.setIconSize(QtCore.QSize(32, 32))

    def house_lay(self):
        self.house_buttons_lay = QtWidgets.QVBoxLayout()
        self.house_buttons_lay.addWidget(self.house_lbl)
        self.house_buttons_lay.addWidget(self.house_btn)
        self.main_layout.addLayout(self.house_buttons_lay)





    def window_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.building_layout()
        self.size_layout()
        self.house_lay()
        self.office_building_lay()




    def create_connections(self):
        self.y_cmb.currentIndexChanged.connect(self.update_connections)

    def update_connections(self):
        self.y_lbl.setText(self.y_cmb.currentText())

