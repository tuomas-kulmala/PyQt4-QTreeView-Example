import sys
from PyQt4 import Qt

class Window(Qt.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.initWindow()

    def initWindow(self):
        # Create layouts
        v_layout =  Qt.QVBoxLayout()
        h1_layout = Qt.QHBoxLayout()
        h2_layout = Qt.QHBoxLayout()

        # Models
        model = Qt.QStandardItemModel()
        model.appendRow(Qt.QStandardItem('eka'))
        model.appendRow(Qt.QStandardItem('toka'))
        model.appendRow(Qt.QStandardItem('kolmas'))

        model.setHeaderData(0, Qt.Qt.Horizontal, Qt.QVariant("Topic"))

        #proxyModel = Qt.QSortFilterProxyModel(self)
        #proxyModel.setSourceModel(model)

        # Create window elements
        treeview_1 = Qt.QTreeView()
        treeview_1.setModel(model)



        button_1 = Qt.QPushButton('OK')




        # Add elements to layouts
        h1_layout.addWidget(treeview_1)
        h2_layout.addWidget(button_1)

        #v_layout.addChildLayout(h1_layout)
        #v_layout.addChildLayout(h2_layout)
        # Set layout
        self.setLayout(h1_layout)

        # Set window title
        self.setWindowTitle('PyQt QTreeView Example')
        self.setFixedSize(1200,1000)
        self.show()


def main():
    app = Qt.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()