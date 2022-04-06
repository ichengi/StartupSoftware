# -*-coding:utf-8-*-
import subprocess
import sys
from time import sleep

from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

# 通用的打开程序设置
def startProgramDefault(ProgramSettings: dict) -> int:
    if ProgramSettings['Operation'] == 'open' and ProgramSettings['bShow'] == 1:
        # subprocess的cwd参数指改变工作目录
        open_state = subprocess.Popen([ProgramSettings['program_path'], ProgramSettings['Parameters']],
                                      cwd=ProgramSettings['Directory'])

        return open_state.returncode

class MainWindow():
    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.StartButton.clicked.connect(self.handleStart)

    def handleStart(self):
        self.ui.MessageShow.append('运行按钮被点击了')
        testdic = {
            "program_path": "C:\\MeoAssistantArknights_v3.0.9\\MeoAsstGui.exe",
            "Operation": "open",
            "Parameters": "",
            "Directory": "C:\\MeoAssistantArknights_v3.0.9",
            "bShow": 1,
            "operation": [
                {
                    "operationimg": "res/img/MAALinkStart.png",
                    "operationaction": "click"
                }
            ]
        }
        states = startProgramDefault(testdic)  # 判断程序打开
        sleep(2)  # todo 暂时未判断窗口是否显示，拿个延时顶一哈，可能考虑加个死循环，或者找其他方法
        for operation_item in testdic['operation']:  # 执行点击命令
            order = f"""pyautogui.{operation_item['operationaction']}("{operation_item['operationimg']}")"""
            exec(order)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec_())
