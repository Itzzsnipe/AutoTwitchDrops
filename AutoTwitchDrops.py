from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QProgressBar, QMessageBox, QTextEdit
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import sys
from selenium import webdriver
from time import sleep

CHROME_DRIVER_PATH = "Put driver exe path here"
CHROME_USER_DATA_DIR = "C:\Users\<your_username>\AppData\Local\Google\Chrome\User Data"
CHROME_PROFILE_DIRECTORY = "Profile 1"

class TwitchStreamerThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, channels, time):
        super().__init__()
        self.channels = channels
        self.time = time
        self.elapsed_time = 0
        self.remaining_time = time * 60

    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")
        options.add_argument(f"profile-directory={CHROME_PROFILE_DIRECTORY}")

        try:
            driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

            for channel in self.channels:
                driver.get(channel)
                self.elapsed_time = 0
                self.remaining_time = self.time * 60

                for t in range(self.time * 60):
                    sleep(1)
                    self.elapsed_time += 1
                    self.remaining_time -= 1
                    progress = int((t+1) / (self.time * 60) * 100)
                    self.progress.emit(progress)

            driver.quit()
        except Exception as e:
            self.show_error_dialog(str(e))

    def show_error_dialog(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec_()

class TwitchStreamerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.streamer_thread = None

        self.layout = QVBoxLayout()

        self.channel_entry = QLineEdit()
        self.channel_entry.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 2px solid #E0E0E0;")
        self.channel_entry.setPlaceholderText("Input twitch URL here")
        self.layout.addWidget(self.channel_entry)

        self.add_channel_button = QPushButton("Add Channel")
        self.add_channel_button.setStyleSheet("background-color: #E0E0E0; color: #333333; font-weight: bold; font-size: 14pt;")
        self.add_channel_button.clicked.connect(self.add_channel)
        self.layout.addWidget(self.add_channel_button)

        self.channel_list = QListWidget()
        self.channel_list.setStyleSheet("background-color: #FFFFFF; color: #000000;")
        self.layout.addWidget(self.channel_list)

        self.remove_channel_button = QPushButton("Remove Channel")
        self.remove_channel_button.setStyleSheet("background-color: #E0E0E0; color: #333333; font-weight: bold; font-size: 14pt;")
        self.remove_channel_button.clicked.connect(self.remove_channel)
        self.layout.addWidget(self.remove_channel_button)

        self.time_entry = QLineEdit()
        self.time_entry.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 2px solid #E0E0E0;")
        self.time_entry.setPlaceholderText("Time per channel (minutes)")
        self.layout.addWidget(self.time_entry)

        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet("background-color: #E0E0E0; color: #333333; font-weight: bold; font-size: 14pt;")
        self.start_button.clicked.connect(self.start)
        self.layout.addWidget(self.start_button)

        self.instructions_button = QPushButton("Instructions")
        self.instructions_button.setStyleSheet("background-color: #E0E0E0; color: #333333; font-weight: bold; font-size: 14pt;")
        self.instructions_button.clicked.connect(self.show_instructions)
        self.layout.addWidget(self.instructions_button)

        self.elapsed_time_label = QLabel("Elapsed Time: 0s")
        self.elapsed_time_label.setStyleSheet("color: #000000;")
        self.layout.addWidget(self.elapsed_time_label)

        self.remaining_time_label = QLabel("Remaining Time: 0s")
        self.remaining_time_label.setStyleSheet("color: #000000;")
        self.layout.addWidget(self.remaining_time_label)

        self.progressbar = QProgressBar()
        self.progressbar.setStyleSheet("QProgressBar { background-color: #FFFFFF; color: #000000; border: none; }"
                                        "QProgressBar::chunk { background-color: #000000; }")
        self.layout.addWidget(self.progressbar)

        self.setLayout(self.layout)

        self.setWindowTitle("Twitch Streamer")
        self.setStyleSheet("background-color: #FFFFFF;")

        font = QFont("Arial")
        font.setPointSize(12)
        self.setFont(font)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

    def add_channel(self):
        channel = self.channel_entry.text().strip()
        if channel:
            self.channel_entry.clear()
            self.channel_list.addItem(channel)
        else:
            self.show_error_dialog("Please enter a valid Twitch URL.")

    def remove_channel(self):
        current_row = self.channel_list.currentRow()
        if current_row > -1:
            self.channel_list.takeItem(current_row)

    def start(self):
        channels = [self.channel_list.item(i).text() for i in range(self.channel_list.count())]
        time = self.time_entry.text().strip()

        if not channels:
            self.show_error_dialog("Please add at least one channel.")
            return

        if not time.isdigit() or int(time) <= 0:
            self.show_error_dialog("Please enter a valid time (positive integer) for each channel.")
            return

        self.streamer_thread = TwitchStreamerThread(channels, int(time))
        self.streamer_thread.progress.connect(self.progressbar.setValue)
        self.streamer_thread.start()

        self.timer.start(1000)  # Update time labels every second

    def update_time(self):
        elapsed_time_text = f"Elapsed Time: {self.streamer_thread.elapsed_time}s"
        remaining_time_text = f"Remaining Time: {self.streamer_thread.remaining_time}s"

        self.elapsed_time_label.setText(elapsed_time_text)
        self.remaining_time_label.setText(remaining_time_text)

    def show_instructions(self):
        instructions = """
        Instructions for Using Twitch Streamer App:
        
        1. Install Python: Download and install Python from the official website.
        2. Install Selenium: Open the command prompt and run 'pip install selenium'.
        3. Install PyQt5: Open the command prompt and run 'pip install pyqt5'.
        4. Set Up ChromeDriver: Download the correct ChromeDriver version and set the path.
        5. Install "Automatic Twitch Drops Monitor" extension for Google Chrome.
        6. Configure the Twitch Streamer App by updating the variables in the code.
        7. Run the app, add Twitch channels, set the duration, and click Start.
        """

        instructions_dialog = QMessageBox()
        instructions_dialog.setWindowTitle("Instructions")
        instructions_dialog.setText(instructions)
        instructions_dialog.exec_()

    def show_error_dialog(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec_()

app = QApplication(sys.argv)

window = TwitchStreamerApp()
window.show()

sys.exit(app.exec_())
