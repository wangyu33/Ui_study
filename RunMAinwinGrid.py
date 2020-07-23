#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : RunMAinwinGrid.py
# Author: WangYu
# Date  : 2020-07-23

import sys
import  MainwinGrid

from  PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = MainwinGrid.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())