#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: WangYu
# Date  : 2020-07-23

import sys
from PyQt5.QtWidgets import QApplication,QWidget

#ui文件转为py
#1: python -m PyQt5.uic.pyuic demo1.ui -o demo1.py
#2: pyuic5 demo1.ui -o demo1.py
if __name__ == '__main__':

    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口尺寸
    w.resize(400, 200)
    w.move(300,300)
    #设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的应用')
    #显示窗口
    w.show()
    sys.exit(app.exec_())
