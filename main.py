
import sys
from PyQt5.QtGui import QPalette, QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLabel, QWidget, QMessageBox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import threading

label_font = QFont("Times", 16)
btn_font = QFont("Times", 16, QFont.Bold)

site_visited = 1
site_failed = 1

# Read user agents from the text file
with open('agents.txt', 'r') as f:
    user_agents = [line.strip() for line in f]

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(user_agents)

# Example usage
user_agent = get_random_user_agent()
print(f"Using User-Agent: {user_agent}")

class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Website viewer Booster")
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Left side

        left_side = QWidget()
        left_layout = QVBoxLayout()
        left_side.setLayout(left_layout)
        left_side.setStyleSheet("background-color:rgb(40,44,52)")

        self.text_input1 = QLineEdit()
        self.text_input1.setStyleSheet("min-height:30px;border-radius:5px;border:1px solid #999;padding-left:10px;color:white;")
        self.text_input1.setPlaceholderText("Link One")
        left_layout.addWidget(self.text_input1)

        self.text_input2 = QLineEdit()
        self.text_input2.setStyleSheet("min-height:30px;border-radius:5px;border:1px solid #999;padding-left:10px;color:white;")
        self.text_input2.setPlaceholderText("Link One")
        left_layout.addWidget(self.text_input2)

        self.text_input3 = QLineEdit()
        self.text_input3.setStyleSheet("min-height:30px;border-radius:5px;border:1px solid #999;padding-left:10px;color:white;")
        self.text_input3.setPlaceholderText("Link One")
        left_layout.addWidget(self.text_input3)

        self.button = QPushButton("Start")
        self.button.setStyleSheet("min-height:40px;border-radius:10px;background-color:darkred;")
        self.button.setFont(btn_font)
        self.button.clicked.connect(self.start)
        palette = self.button.palette()
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.button.setPalette(palette)
        left_layout.addWidget(self.button)

        self.stop_button = QPushButton("Stop Selenium")
        self.stop_button.setStyleSheet("min-height:40px;border-radius:10px;background-color:darkred;")
        self.stop_button.setFont(btn_font)
        self.stop_button.clicked.connect(self.stop_selenium)
        left_layout.addWidget(self.stop_button)

        # Right side

        right_side = QWidget()
        right_layout = QVBoxLayout()
        right_side.setLayout(right_layout)
        right_side.setStyleSheet("background-color:rgb(51,56,56)")

        self.label1 = QLabel("Site viewed: 1002")
        self.label1.setStyleSheet("color:white")
        self.label1.setFont(label_font)
        right_layout.addWidget(self.label1)

        self.label2 = QLabel("Site failed: 3")
        self.label2.setStyleSheet("color:white")
        self.label2.setFont(label_font)
        right_layout.addWidget(self.label2)

        self.selenium_status_label = QLabel()
        self.selenium_status_label.setStyleSheet("color:white")
        self.selenium_status_label.setFont(label_font)
        right_layout.addWidget(self.selenium_status_label)

        # Main

        main_layout.addWidget(left_side, stretch=7)
        main_layout.addWidget(right_side, stretch=3)

        self.setCentralWidget(main_widget)
        self.show()
        self.resize(700, 500)

    def load_proxies(self, path):
        return open(path).read().split('\n')


    def load_session(self, proxy):
        proxy, port = proxy.split(':')
        id = random.randrange(0, len(user_agents))
        agent = user_agents[id]
        options = Options()
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.http", proxy)
        options.set_preference("network.proxy.type_port", port)
        options.set_preference("network.proxy.ssl", proxy)
        options.set_preference("network.proxy.ssl_port", port)
        options.set_preference("general.useragent.override", agent)
        options.headless = True

        driver = webdriver.Firefox(options=options)

        try:
            driver.get(self.text_input1.text())
            time.sleep(3)
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.get(self.text_input2.text())
            time.sleep(3)
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            driver.get(self.text_input3.text())
            time.sleep(3)
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.quit()
        except:
            driver.quit()
            raise Exception("Failed to load website")

    def main(self):
        global site_visited
        global site_failed
        proxies = self.load_proxies("proxies.txt")

        while True:
            id = random.randrange(0, len(proxies))
            proxy = proxies[id]
            try:
                self.load_session(proxy)
                print("View counted:", site_visited)
                self.label1.setText("Site visited: {}".format(site_visited))
                site_visited += 1
                self.selenium_status_label.setText("")  # Clear the status label
            except Exception as e:
                self.label2.setText("Site failed: {}".format(site_failed))
                site_failed += 1
                print("View failed:", site_failed)
                print(e)

    def start(self):
        if not self.text_input1.text() or not self.text_input2.text() or not self.text_input3.text():
            message = QMessageBox()
            message.setWindowTitle("Input Error")
            message.setText("Please fill in all input fields.")
            message.exec_()
        else:
            self.selenium_status_label.setText("Selenium is starting...")
            thread = threading.Thread(target=self.main)
            thread.start()
    def stop_selenium(self):
        if hasattr(self, 'driver'):  # Check if driver attribute exists
          self.selenium_status_label.setText("Stopping Selenium...")
          self.driver.quit()
        else:
          self.selenium_status_label.setText("Selenium is not running...")       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec_())