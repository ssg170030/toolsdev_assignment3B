from PySide2 import QtWidgets


class basicUI(QtWidgets.QDialog):

    def __index__(self):
        super(basicUI, self).__init__()
        self.setWindowTitle("Basic UI Example")
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.fruit_cmb = QtWidgets.QComboBox()
        self.fruit_cmb.addItems(['apple', 'orange', 'banana'])

    def create_layout(self):
        self.lay = QtWidgets.QFormLayout()
        self.lay.addRow("Fruit", self.fruit_cmb)
        self.setLayout(self.lay)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = basicUI()
    window.show()
    # executes application
    app.exec_()
