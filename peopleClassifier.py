import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # create a button
        self.button = QPushButton("Click me!", self)
        self.button.move(50,50)
        self.button.clicked.connect(self.buttonClicked)

        # create a table view
        self.tableView = QTableView(self)
        self.tableView.setSortingEnabled(True)
        self.tableView.setGeometry(50, 100, 400, 200)

        # create a model for the table view
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Age', 'Gender'])

        # Add some items to the model
        items = [
            ['Alice', '23', 'Female'],
            ['Bob', '45', 'Male'],
            ['Charlie', '31', 'Male'],
            ['Danielle', '27', 'Female'],
        ]
        for item in items:
            row = [QStandardItem(str(x)) for x in item]
            self.model.appendRow(row)

        # set the model for the table view
        self.tableView.setModel(self.model)

        # create a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.tableView)

        # create a widget and set the layout
        widget = QWidget()
        widget.setLayout(layout)

        # set the central widget of the main window
        self.setCentralWidget(widget)

        # set the window properties
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('People Classifier')
        self.show()

    def buttonClicked(self):
        print('Button clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
