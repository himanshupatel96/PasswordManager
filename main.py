from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.startUI()

	def startUI(self):

		self.setStyleSheet('background-color:white;')
		self.move(500,100)
		self.resize(500,500)

def main():

	mainApplication = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(mainApplication.exec_())

if __name__ == "__main__":
	main()