# -*-coding:utf-8-*-
import subprocess
import sys
from time import sleep

from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

# 通用的打开程序设置1
def startProgramDefault(ProgramSettings: dict) -> int:
    if ProgramSettings['Operation'] == 'open' and ProgramSettings['bShow'] == 1:
        # subprocess的cwd参数指改变工作目录
        open_state = subprocess.Popen([ProgramSettings['program_path'], ProgramSettings['Parameters']],
                                      cwd=ProgramSettings['Directory'])

        return open_state.returncode

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = QUiLoader().load('main.ui')
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.StartButton.clicked.connect(self.handleStart)

    def handleStart(self):
        with open("res\ProgramConfig.json", "r") as json_file:
            programdata = json.load(json_file)

        for item in self.ui.Prolist.buttons():  # 遍历选中的按钮
            if item.isChecked() and item.text() in programdata['Programs']:
                prodataitem = programdata['Programs'][item.text()]
                states = startProgramDefault(prodataitem)  # 判断程序打开
                sleep(3)  # todo 暂时未判断窗口是否显示，拿个延时顶一哈，可能考虑加个死循环，或者找其他方法
                for operation_item in prodataitem['operation']:  # 执行点击命令
                    order = f"""pyautogui.{operation_item['operationaction']}("{operation_item['operationimg']}")"""
                    exec(order)
                    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec_())
