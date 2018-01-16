#这个无界面窗口用来演示如何创建信号 如何创建槽函数 如何连接和响应
from PyQt5.QtCore import QObject, pyqtSignal

class QTypeSignal(QObject):
    sendMsg = pyqtSignal(object) #object是什么鬼?

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        self.sendMsg.emit('Hello, World!') #emit是发射的意思?

class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self, msg):
        print('接收到信号=>'+ msg)

if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()

    print('-------把信号绑定到槽上------')
    send.sendMsg.connect(slot.get)

    send.run()

    print('-------吧信号与槽函数断开-----')
    send.sendMsg.disconnect(slot.get)
    send.run()

