
from PyQt5 import *
import sys
from selenium import webdriver
from time import sleep
from UI_Dialog import *
from PyQt5 import QtWidgets,QtCore,QtGui


class Window(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.Login)
        self.ui.buttonBox.accepted.connect(self.Password)
        self.ui.buttonBox.accepted.connect(self.parser)

    def Login(self):
        x = str(self.ui.lineEdit.text())
        return x

    def Password(self):
        x = str(self.ui.lineEdit_2.text())
        return x

    def parser(self):
        self.driver = webdriver.Chrome("C:\Python36\selenium\chromedriver.exe")
        self.navigate()

    def navigate(self):
        self.driver.get("https://yandex.ru")
        self.inputi()
        self.vkButton()
        self.TabArray()
        self.email()
        self.password()
        self.authButton()

    def password(self):
        p = self.driver.find_element_by_css_selector("#index_pass")
        x = self.Password()
        p.send_keys(x)

    def email(self):
        w = self.driver.find_element_by_css_selector("#index_email")
        x = self.Login()
        w.send_keys(x)

    def inputi(self):
        inputElement = self.driver.find_element_by_id("text")
        inputElement.send_keys("vk.com")
        inputElement.submit()

    def vkButton(self):
        findbutton = self.driver.find_element_by_link_text("vk.com")
        findbutton.click()
        sleep(3)

    def authButton(self):
        button = self.driver.find_element_by_css_selector("#index_login_button").click()

    def TabArray(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

    def Login(self):
        x = str(self.ui.lineEdit.text())
        return x



    def Password(self):
        x = str(self.ui.lineEdit_2.text())
        return x










if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())

