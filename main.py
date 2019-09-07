# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(600, 150, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.subtitle = QtWidgets.QLabel(self.centralwidget)
        self.subtitle.setGeometry(QtCore.QRect(600, 180, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.berat_badan_line = QtWidgets.QLineEdit(self.centralwidget)
        self.berat_badan_line.setGeometry(QtCore.QRect(480, 250, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.berat_badan_line.setFont(font)
        self.berat_badan_line.setObjectName("berat_badan_line")
        self.berat_badan_label = QtWidgets.QLabel(self.centralwidget)
        self.berat_badan_label.setGeometry(QtCore.QRect(300, 260, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.berat_badan_label.setFont(font)
        self.berat_badan_label.setObjectName("berat_badan_label")
        self.tinggi_badan_label = QtWidgets.QLabel(self.centralwidget)
        self.tinggi_badan_label.setGeometry(QtCore.QRect(300, 370, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.tinggi_badan_label.setFont(font)
        self.tinggi_badan_label.setObjectName("tinggi_badan_label")
        self.tinggi_badan_line = QtWidgets.QLineEdit(self.centralwidget)
        self.tinggi_badan_line.setGeometry(QtCore.QRect(480, 360, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tinggi_badan_line.setFont(font)
        self.tinggi_badan_line.setObjectName("tinggi_badan_line")
        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setGeometry(QtCore.QRect(290, 470, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.processButton.setFont(font)
        self.processButton.setObjectName("processButton")
        self.processButton.clicked.connect(self.process)
        self.index_max_method = QtWidgets.QLabel(self.centralwidget)
        self.index_max_method.setGeometry(QtCore.QRect(880, 460, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.index_max_method.setFont(font)
        self.index_max_method.setObjectName("index_max_method")
        self.hasil_max_method_text = QtWidgets.QLabel(self.centralwidget)
        self.hasil_max_method_text.setGeometry(QtCore.QRect(880, 490, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hasil_max_method_text.setFont(font)
        self.hasil_max_method_text.setObjectName("hasil_max_method_text")
        self.max_method_text = QtWidgets.QLabel(self.centralwidget)
        self.max_method_text.setGeometry(QtCore.QRect(860, 440, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.max_method_text.setFont(font)
        self.max_method_text.setObjectName("max_method_text")
        self.diperoleh_text = QtWidgets.QLabel(self.centralwidget)
        self.diperoleh_text.setGeometry(QtCore.QRect(860, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.diperoleh_text.setFont(font)
        self.diperoleh_text.setObjectName("diperoleh_text")
        self.himpunan_hasil_text = QtWidgets.QLabel(self.centralwidget)
        self.himpunan_hasil_text.setGeometry(QtCore.QRect(860, 280, 341, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.himpunan_hasil_text.setFont(font)
        self.himpunan_hasil_text.setText("")
        self.himpunan_hasil_text.setObjectName("himpunan_hasil_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logika Fuzzy"))
        self.title.setText(_translate("MainWindow", "EVALUASI  KESEHATAN ORANG"))
        self.subtitle.setText(_translate("MainWindow", "m  e  n  g  g  u  n  a  k  a  n     l  o  g  i  k  a     f  u  z  z  y"))
        self.berat_badan_label.setText(_translate("MainWindow", "Berat Badan (kg)"))
        self.tinggi_badan_label.setText(_translate("MainWindow", "Tinggi Badan (cm)"))
        self.processButton.setText(_translate("MainWindow", "PROSES"))
        self.index_max_method.setText(_translate("MainWindow", "Index :"))
        self.hasil_max_method_text.setText(_translate("MainWindow", "Hasil :"))
        self.max_method_text.setText(_translate("MainWindow", "Max Method"))
        self.diperoleh_text.setText(_translate("MainWindow", "Diperoleh"))
        self.himpunan_hasil_text.setText(_translate("MainWindow", ""))

    def process(self):
        height_input = float(self.tinggi_badan_line.text())
        height_list = self.get_height_list(height_input)

        weight_input = float(self.berat_badan_line.text())
        weight_list = self.get_weight_list(weight_input)
        
        health_list = self.get_health_list(height_list, weight_list)
        health = self.get_max_index(health_list)

        result_string = ""
        for i in range(len(health_list)):
            result_string += self.get_result_string(i, health_list[i]) + "\n\n"
        self.himpunan_hasil_text.setText(result_string)
        self.himpunan_hasil_text.show()

        index_value = "Index : " + str(health.index)
        self.index_max_method.setText(index_value)
        self.index_max_method.show()

        result_value = "Hasil : " + str(health.name)
        self.hasil_max_method_text.setText(result_value)
        self.hasil_max_method_text.show()

    def get_result_string(self, i, health):
        return (str(str(i+1) + ". " + str(health.index) + " - " + health.name))
        
    def get_max_index(self, health_list):
        temp = []
        for health in health_list:
            temp.append(health.index)
        max_value = max(temp)
        result = None
        for health in health_list:
            if health.index == max_value:
                result = health
                break
        return result
    
    def get_health_list(self, height_list, weight_list):
        health_list = []
        for height in height_list:
            for weight in weight_list:
                health_list.append(self.get_health_object(height, weight))
        return health_list

    def get_health_object(self, _height, _weight):
        number = -1
        name = ["Tidak Sehat", "Agak Sehat", "Sehat", "Sangat Sehat"]
        print(str(_height.id) + " " + str(_weight.id))
        if _height.id == 0:
            if _weight.id == 0:
                number = 3
            elif _weight.id == 1:
                number = 2
            elif _weight.id == 2:
                number = 1
            elif _weight.id == 3:
                number = 0
            elif _weight.id == 4:
                number = 0
        elif _height.id == 1:
            if _weight.id == 0:
                number = 2
            elif _weight.id == 1:
                number = 3
            elif _weight.id == 2:
                number = 2
            elif _weight.id == 3:
                number = 1
            elif _weight.id == 4:
                number = 0
        elif _height.id == 2:
            if _weight.id == 0:
                number = 1
            elif _weight.id == 1:
                number = 3
            elif _weight.id == 2:
                number = 3
            elif _weight.id == 3:
                number = 1
            elif _weight.id == 4:
                number = 0
        elif _height.id == 3:
            if _weight.id == 0:
                number = 0
            elif _weight.id == 1:
                number = 2
            elif _weight.id == 2:
                number = 3
            elif _weight.id == 3:
                number = 2
            elif _weight.id == 4:
                number = 0
        elif _height.id == 4:
            if _weight.id == 0:
                number = 0
            elif _weight.id == 1:
                number = 1
            elif _weight.id == 2:
                number = 3
            elif _weight.id == 3:
                number = 2
            elif _weight.id == 4:
                number = 1
        index = min(_height.index, _weight.index)
        print(str(number) + " " + name[number] + " " + str(index) + " " + "Sehat")
        return (self.get_object(number, name[number], index, "Sehat"))
    
    def get_height_list(self, height_input):
        height_list = []
        name = ["Sangat Pendek", "Pendek", "Sedang", "Tinggi", "Sangat Tinggi"]
        index_1 = 0.0
        index_2 = 0.0
        number_1 = -1
        number_2 = -1
        if 0 < height_input <= 115.0:
            number_1 = 0
            index_1 = 1.0
        elif 115.0 < height_input < 120.0:
            number_1 = 0
            number_2 = 1
            index_1, index_2 = self.get_index(115.0, 120.0, height_input)
        elif 120.0 <= height_input <= 140.0:
            number_1 = 1
            index_1 = 1.0
        elif 140.0 < height_input < 145.0:
            number_1 = 1
            number_2 = 2
            index_1, index_2 = self.get_index(140.0, 145.0, height_input)
        elif 145.0 <= height_input <= 160.0:
            number_1 = 2
            index_1 = 1.0
        elif 160.0 < height_input < 165.0:
            number_1 = 2
            number_2 = 3
            index_1, index_2 = self.get_index(160.0, 165.0, height_input)
        elif 165.0 <= height_input <= 180.0:
            number_1 = 3
            index_1 = 1.0
        elif 180.0 < height_input < 185.0:
            number_1 = 3
            number_2 = 4
            index_1, index_2 = self.get_index(180.0, 185.0, height_input)
        elif height_input >= 185.0:
            number_1 = 4
            index_1 = 1.0
        height_1 = self.get_object(number_1, name[number_1], index_1, "Tinggi")
        height_list.append(height_1)
        print(str(number_1) + " " + str(height_1.index) + " " + height_1.name)
        if index_2 != 0.0 and number_2 != -1:
            height_2 = self.get_object(number_2, name[number_2], index_2, "Tinggi")
            height_list.append(height_2)
            print(str(number_2) + " " + str(height_2.index) + " " + height_2.name)
        return height_list
    
    def get_object(self, _id, _name, _index, _category):
        keanggotaan = Keanggotaan()
        keanggotaan.id = _id
        keanggotaan.name = _name
        keanggotaan.index = _index
        keanggotaan.category = _category
        return keanggotaan
        
    def get_index(self, _min, _max, _value):
        result_1 = (_max - _value) / (_max - _min)
        result_2 = (_value - _min) / (_max - _min)
        return result_1, result_2

    def get_weight_list(self, weight_input):
        weight_list = []
        name = ["Sangat Kurus", "Kurus", "Biasa", "Berat", "SangatBerat"]
        index_1 = 0.0
        index_2 = 0.0
        number_1 = -1
        number_2 = -1
        if 0.0 < weight_input <= 40.0:
            number_1 = 0
            index_1 = 1.0
        elif 40.0 < weight_input < 45.0:
            number_1 = 0
            number_2 = 1
            index_1, index_2 = self.get_index(40.0, 45.0, weight_input)
        elif 45.0 <= weight_input <= 50.0:
            number_1 = 1
            index_1 = 1.0
        elif 50.0 < weight_input < 55.0:
            number_1 = 1
            number_2 = 2
            index_1, index_2 = self.get_index(50.0, 55.0, weight_input)
        elif 55.0 <= weight_input <= 60.0:
            number_1 = 2
            index_1 = 1.0
        elif 60.0 < weight_input < 65.0:
            number_1 = 2
            number_2 = 3
            index_1, index_2 = self.get_index(60.0, 65.0, weight_input)
        elif 65.0 <= weight_input <= 80.0:
            number_1 = 3
            index_1 = 1.0
        elif 80.0 < weight_input < 85.0:
            number_1 = 3
            number_2 = 4
            index_1, index_2 = self.get_index(80.0, 85.0, weight_input)
        elif weight_input >= 85.0:
            number_1 = 4
            index_1 = 1.0
        weight_1 = self.get_object(number_1, name[number_1], index_1, "Berat")
        print(str(number_1) + " " + str(weight_1.index) + " " + weight_1.name)
        weight_list.append(weight_1)
        if index_2 != 0.0 and number_2 != -1:
            weight_2 = self.get_object(number_2, name[number_2], index_2, "Berat")
            weight_list.append(weight_2)
            print( str(number_2) + " " + str(weight_2.index) + " " + weight_2.name)
        return weight_list

class Keanggotaan:
    def __init__(self):
        self._id = 0
        self._name = ""
        self._index = 0.0
        self._category = ""
    
    # function to get value of _id
    def get_id(self):
        return self._id

    # function to set value of _id
    def set_id(self, id):
        self._id = id
    
    # function to delete _id attribute 
    def del_id(self):
        del self._id
    
    id = property(get_id, set_id, del_id)

    # function to get value of _name 
    def get_name(self): 
        return self._name
       
    # function to set value of _name  
    def set_name(self, name): 
        self._name = name
  
    # function to delete _name attribute 
    def del_name(self): 
        del self._name
     
    name = property(get_name, set_name, del_name) 
    
    # function to get value of _index
    def get_index(self): 
        return self._index
       
    # function to set value of _index
    def set_index(self, index): 
        self._index = index
  
    # function to delete _index attribute 
    def del_index(self): 
        del self._index
     
    index = property(get_index, set_index, del_index)

    # function to get value of _category
    def get_category(self):
        return self._category
    
    # function to set value of _category
    def set_category(self, c):
        self._category = c
    
    # function to delete _category attribute 
    def del_category(self):
        del self._category
    
    category = property(get_category, set_category, del_category)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
