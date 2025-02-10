import os
import sys
import time
from time import strftime

import speech_recognition as aud
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from gtts import gTTS


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

'''  first Error - Programme is Breaking while voiceAssistance is talking and if i ignore this runs only 2 times '''
name = input("Enter your name : ")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setAcceptDrops(True)
        # set the title
        self.setWindowTitle("Image")
        self.setGeometry(200,200,WINDOW_WIDTH,WINDOW_HEIGHT)

        '''
         self.pixmap = QPixmap("/home/faizan/Desktop/All python Folders/speechRecognition/microphone-black-shape.png")
         self.image_label = QLabel(self)
         self.image_label.setPixmap(self.pixmap)
         self.image_label.move(30,50)
        '''
        self.button = QPushButton("", self)
        self.button.setIcon(QIcon("/home/faizan/Desktop/All-python-Folders/speechRecognition/microphone-black-shape.png"))
        self.button.move(280,230)
        self.button.clicked.connect(self.onclick)
        self.show()

    def onclick(self):

        CurrentTime = strftime('%H:%M:%S')

        a = aud.Recognizer()
        with aud.Microphone() as source:
            print("Say Something")
            output_speech = a.listen(source)
            time.sleep(2)

            tts = gTTS(text=a.recognize_google(output_speech), lang="en")
            if a.recognize_google(output_speech) == 'hello':
                tts = gTTS(text=f'{name}Hello how are you', lang='en')
                tts.save('spain.mp3')
                os.system('mpg123 spain.mp3')
            elif a.recognize_google(output_speech) == 'current time':
                tts = gTTS(text=f'currrent time is {CurrentTime}', lang='en')
                tts.save('time.mp3')
                os.system('mpg123 time.mp3')
           

            time.sleep(2)
            tts.save("speech.mp3")
            os.system("mpg123 speech.mp3")
        try:
            print("You sayed : ", a.recognize_google(output_speech))
            time.sleep(1)
        except aud.UnknownValueError:
            print("Voice is not clear")
        except aud.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())






