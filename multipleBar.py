import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QStatusBar, QTextEdit, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # create a menu bar
        menubar = self.menuBar()

        # create a file menu
        fileMenu = menubar.addMenu('&File')

        # create a new action
        newAction = QAction('&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create a new document')
        newAction.triggered.connect(self.newFile)

        # create an open action
        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open an existing document')
        openAction.triggered.connect(self.openFile)

        # Add the actions to the file menu
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)

        # create a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add the actions to the toolbar
        toolbar.addAction(newAction)
        toolbar.addAction(openAction)

        # create a text edit widget
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # create a status bar
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        # set the window properties
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Example')
        self.show()

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if filename:
            with open(filename, 'r') as f:
                self.textEdit.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


