import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import os
import sh
import des


    # получить информацию об устройстве (sda или sdb)

def get_device_info():


    with sh.contrib.sudo:
        cmd = 'smartctl -i /dev/sda'

    data = os.popen(cmd)
    res = data.read().splitlines()
    device_info = {}
    with open(r"info.txt", "w+") as file:
        for i in range(4, len(res) - 1):
            line = res[i]
            temp = line.split(':', 1)
            a=temp[0]
            b=temp[1]
            file.write(a+':')
            file.write(b+'\n')
    file.close()

        # функция для проверки атрибутов

def check_device_attributes():
    cmd = 'smartctl -A /dev/sda'
    data = os.popen(cmd).read()
    res = data.splitlines()
    health ={}
    with open(r"attributes.txt", "w") as file:
        ##file.write(res[4] + '\n')
        ##file.write(res[5] + '\n')
        for i in range(7, len(res)-1):
            line = res[i]
            line = line.strip()
            file.write(line +'\n')
    file.close()

    # функция общая проверка

def check_device_all():
    cmd = 'smartctl -x /dev/sda'
    data = os.popen(cmd).read()
    res = data.splitlines()
    line = {}
    temp = {}
    with open(r"all.txt", "w") as file:
        for i in range(108, len(res) - 1):
            line = res[i]
            temp = line.split('\n')
            a=temp[0]
            file.write(a+'\n')
    file.close()

    # количество папок и файлов в фс

def number_of_files_and_folders():
    cmd = 'tree -a'
    data = os.popen(cmd).read()
    res = data.splitlines()
    line = {}
    temp = {}
    with open(r"number.txt", "w") as file:
        for i in range(len(res)-1, len(res)):
            line = res[i]
            temp = line.split('\n')
            a = temp[0]
            file.write(a + '\n')
    file.close()

        # данные фс

def fs_info():
    with sh.contrib.sudo:
        cmd = 'tune2fs -l /dev/sdb3'
    data = os.popen(cmd)
    res = data.read().splitlines()
    fs_info = {}
    with open(r"fs_info.txt", "w") as file:
        for i in range(2, len(res)):
            line = res[i]
            temp = line.split(':', 1)
            a=temp[0]
            b=temp[1]
            file.write(a+':')
            file.write(b+'\n')
    file.close()

        # фс и основные величины
def name_fs():
    cmd = 'df -Th | grep ^/dev'
    data = os.popen(cmd).read()
    res = data.splitlines()
    line = {}
    temp = {}
    ##line1 ={'Файл.система   Тип      Размер Использовано  Дост Использовано% Cмонтировано в'}
    with open(r"name_fs.txt", "w") as file:
        for i in range(0, 1):
            line = res[i]
            temp = line.split('\n')
            a = temp[0]
            file.write(a + '\n')
    file.close()

class ExampleApp(QtWidgets.QMainWindow, des.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)
def main():
    app = QtWidgets.QApplication(sys.argv)
    file = open("qss.qss", 'r')
    with file:
        qss=file.read()
        ##app.setStyleSheet(qss)
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    get_device_info()
    check_device_attributes()
    check_device_all()
    number_of_files_and_folders()
    fs_info()
    name_fs()
    main()


