import sys


class HashmalGui(object):
    def __init__(self):
	from PyQt4.QtGui import QApplication
        super(HashmalGui, self).__init__()
        self.app = QApplication(sys.argv)

    def main(self):
	from main_window import HashmalMain
        self.main_window = HashmalMain(self.app)
        self.main_window.show()
        sys.exit(self.app.exec_())

