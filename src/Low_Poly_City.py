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
    
    def __index__(self):

        super(low_poly_city_ui, self).__index__(parent=maya_main_window())
        House.PolyHouse()
        self.title_lable()
        self.setWindowTitle("Low Poly Buildings")
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.resize(500, 300)
        self.create_widgets()
        self.create_layout()



    def title_lable(self):
        self.title_lbl = QtWidgets.QLabel("LowPoly Buildings")
        self.title_lbl.setStyleSheet("font: bold 40px")

    def create_widgets(self):

        pass



    def create_layout(self):


        pass



