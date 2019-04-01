import sys
from sumform_rc import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt, QDir
from main import file_rows


class MyMainWindow(QMainWindow, Ui_MainWindow):
    # 选择文件按钮
    selectDirSignal = pyqtSignal()

    # 开始统计按钮
    sumStartSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.fr = file_rows()

    def selectDirAction(self):
        # print('选择')
        # dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.Directory)
        # dlg.setFilter(QDir.Files)
        # if dlg.exec_():
        #     filenames = dlg.selectedFiles()
        #     self.dir_str.setText(filenames[0])
        dir_path = QFileDialog.getExistingDirectory(self, "文件选择", "./")
        self.dir_str.setText(dir_path)

    def sumStartVoid(self):
        # print('开始统计')
        if self.dir_str.text():
            num = self.fr.get_rows(self.dir_str.text())
            self.rows_num.setText('文件夹：%s\n代码总行数：%s' % (self.dir_str.text(), num))
        else:
            QMessageBox.warning(self, '注意', '请选择文件夹', QMessageBox.Yes, QMessageBox.Yes)

    def initUI(self):
        # 绑定
        self.sumstart.clicked.connect(self.sumStartVoid)
        self.selectDir.clicked.connect(self.selectDirAction)
        self.rows_num.setText('选择文件后点击开始统计')
        # // 窗体透明，控件不透明
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowOpacity(0.5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
