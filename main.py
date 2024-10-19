# -*- coding: utf-8 -*-
# Subscribe to PyShine Youtube channel for more detail!
#
# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# WEBSITE: www.pyshine.com

import os
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import pandas as pd
import sip  # can be installed : pip install sip


# Set the font to use
font_path = fm.findfont(fm.FontProperties(family='SimSun'))  # make japanese readable
plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    #########################################################
    # ⇓ Replace Ui_MainWindow from main_.py from main_.ui ⇓ #
    #########################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spacerItem2 = QtWidgets.QSpacerItem(20, 469, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(self.spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFIle.addAction(self.actionOpen_csv_file)
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#########################################################
# ⇑ Replace Ui_MainWindow from main_.py from main_.ui ⇑ #
#########################################################

        self.filename = ''
        self.canv = MatplotlibCanvas(self)
        self.df = []

        self.toolbar = Navi(self.canv, self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)

        self.themes = ['bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot', 'grayscale', 'Solarize_Light2', 'tableau-colorblind10']

        self.comboBox.addItems(self.themes)

        self.pushButton.clicked.connect(self.getFile)
        self.comboBox.currentIndexChanged['QString'].connect(self.Update)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionOpen_csv_file.triggered.connect(self.getFile)

    def Update(self, value):
        print("Theme selected:", value)
        plt.clf()
        plt.style.use(value)
        try:
            self.horizontalLayout.removeWidget(self.toolbar)
            self.horizontalLayout_3.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.horizontalLayout_3.removeItem(self.spacerItem2)
        except Exception as e:
            print(e)
            pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv, self.centralwidget)

        self.horizontalLayout.addWidget(self.toolbar)
        self.horizontalLayout_3.addWidget(self.canv)

        self.canv.axes.cla()
        ax = self.canv.axes
        self.df.plot(ax=self.canv.axes)
        legend = ax.legend()
        legend.set_draggable(True)

        ax.set_title(self.Title)

        self.canv.draw()

    def getFile(self):
        """ This function will get the address of the csv file location
            also calls a readData function
        """
        try:
            self.filename = QFileDialog.getOpenFileName(filter="csv (*.csv)")[0]
            print("File :", self.filename)
            self.readData()
        except Exception as e:
            print(e)
            pass

    def readData(self):
        """ This function will read the data using pandas and call the update
            function to plot
        """
        try:
            base_name = os.path.basename(self.filename)
            self.Title = os.path.splitext(base_name)[0]
            print('FILE', self.Title)
            self.df = pd.read_csv(self.filename, encoding='utf-8').fillna(0)
            self.df.set_index(self.df.columns[0], inplace=True)
            self.Update(self.themes[0])  # lets 0th theme be the default : bmh
        except Exception as e:
            print(e)
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyShine csv plot"))
        self.label.setText(_translate("MainWindow", "Select Theme"))
        self.label_2.setText(_translate("MainWindow", "Input File"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_csv_file.setText(_translate("MainWindow", "Open csv file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    # Handle dragEnter event
    def dragEnterEvent(self, e: QDragEnterEvent):
        """
        This function will detect the drag enter event from the mouse on the main window
        """
        # Accept drag if it contains URLs (e.g., files)
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
        else:
            e.ignore()

    # Handle drop event
    def dropEvent(self, e: QDropEvent):
        """
        This function will enable the drop file directly on to the
        main window. The file location will be stored in the self.filename
        """
        if e.mimeData().hasUrls():
            urls = e.mimeData().urls()
            # Only process the first file for simplicity
            if urls:
                file_path = urls[0].toLocalFile()
                self.label_2.setText(f"Input file: {file_path}")
                for url in e.mimeData().urls():
                    fname = str(url.toLocalFile())
                self.filename = fname
                self.readData()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi(ui)

    ui.show()
    sys.exit(app.exec_())


