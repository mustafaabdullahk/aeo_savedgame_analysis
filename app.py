# if __name__ == "__main__":

import sys
import csv
import operator
import pandas as pd
import numpy as np
import os.path
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from matplotlib import pyplot as plt
from random import randint
#from matplotlib.animation import FuncAnimation
from collections import deque
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt, QThread, QTimer
import urllib,requests
import re

array=[]
a=[]

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()        
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Import saved game file')
        self.b2 = QtWidgets.QPushButton('Get info from data')
        self.b1 = QtWidgets.QPushButton('Get sorted students for your compnay!!')
        #self.led = QtWidgets.QLabel('Enter URL')
        #self.le = QtWidgets.QLineEdit('')
        #self.le1d = QtWidgets.QLabel('Enter name of player')
        #self.le1 = QtWidgets.QLineEdit('')
        #self.le2d = QtWidgets.QLabel('Enter score range')
        #self.le2 = QtWidgets.QLineEdit('')
        #self.cb = QtWidgets.QComboBox('')
        self.cb = QComboBox()
        self.cb_speed = QComboBox()
        self.cb_speed.addItem("Real Time")
        self.cb_speed.addItem("2x Accelerated")
        self.cb_speed.addItem("4x Accelerated")
        self.cb_speed.addItem("16x Accelerated")
        #self.cb.currentIndexChanged.connect(self.selectionchange)

        font = QtGui.QFont()
        font.setPointSize(18)

        self.l = QtWidgets.QLabel(" ")
        self.l.setAlignment(Qt.AlignCenter)

        #self.l3 = QtWidgets.QLabel(' ')
        #self.l3.setAlignment(Qt.AlignCenter)

        self.l5 = QtWidgets.QLabel(' ')
        self.l5.setAlignment(Qt.AlignCenter)

        self.l6 = QtWidgets.QLabel(' ')
        self.l6.setAlignment(Qt.AlignCenter)

        self.l7 = QtWidgets.QLabel(' ')
        self.l7.setAlignment(Qt.AlignCenter)

        self.l8 = QtWidgets.QLabel(' ')
        self.l8.setAlignment(Qt.AlignCenter)

        self.l9 = QtWidgets.QLabel(' ')
        self.l9.setAlignment(Qt.AlignCenter)

        self.b3 = QtWidgets.QPushButton("Plot Game Statictics")
        self.b4 = QtWidgets.QPushButton("Replay Game from Save File")
        self.b5 = QtWidgets.QPushButton("Download")

        h_box1 = QtWidgets.QHBoxLayout()        
        #h_box1.addWidget(self.le1d)
        #h_box1.addWidget(self.le1)

        h_box2 = QtWidgets.QHBoxLayout()
        #h_box2.addWidget(self.le2d)
        #h_box2.addWidget(self.le2)

        self.pw1 = pg.PlotWidget(title="Wood")
        self.pw2 = pg.PlotWidget(title="Food")
        self.pw3 = pg.PlotWidget(title="Gold")
        self.pw4 = pg.PlotWidget(title="Stone")

        #h_box2.addWidget(self.pw1)
        #h_box2.addWidget(self.pw2)
        #h_box2.addWidget(self.pw3)
        self.r_time = [1, 1, 1]
        self.r_wood = [1, 1, 1]
        self.r_food = [1, 1, 1]
        self.r_gold = [1, 1, 1]
        self.r_stone = [1, 1, 1]
        self.r_vils = [1, 1, 1]
        self.r_mils = [1, 1, 1]
        #pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)
        self.pl = self.pw1.plot(pen='g')

        v_box = QtWidgets.QVBoxLayout()
        #v_box.addWidget(self.led)
        #v_box.addWidget(self.le)
        v_box.addWidget(self.b5)
        v_box.addWidget(self.b)
        v_box.addWidget(self.cb)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.l)
        #v_box.addWidget(self.l5)
        #v_box.addWidget(self.l6)
        v_box.addWidget(self.l7)
        v_box.addWidget(self.l8)
        v_box.addWidget(self.cb_speed)
        v_box.addWidget(self.b3)
        v_box.addWidget(self.b4)
        #v_box.addWidget(self.l9)


        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        #v_box.addWidget(self.b1)
        #v_box.addWidget(self.l3)

        v_box.addWidget(self.pw1)
        v_box.addWidget(self.pw2)
        v_box.addWidget(self.pw3)
        v_box.addWidget(self.pw4)

        self.setLayout(v_box)
        self.setWindowTitle("AgeOfEmpires Game Analysis")

        #hbox = QHBoxLayout()

        self.b.clicked.connect(self.btn_click)
        #self.b1.clicked.connect(self.btn1_click)
        self.b2.clicked.connect(self.btn2_click)        
        self.b3.clicked.connect(self.graph)
        self.b4.clicked.connect(self.replay)
        self.b5.clicked.connect(self.download)
        self.show()
        self.b4.setEnabled(False)
        self.b3.setEnabled(False)
        self.b2.setEnabled(False)
        self.b1.setEnabled(False)
        self.b.setEnabled(False)



    def btn_click(self):
        file = 'aotstats.txt'
        if os.path.isfile(file):
            with open(file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for line in reader:
                    array.append(tuple(line))

            if array:
                self.l.setText('File uploaded')
                a.append(1)
                data = pd.read_csv('aotstats.txt')
                player= np.array(data['player'].head(4))
                for i in range(4):
                    self.cb.addItem(player[i])
                self.b1.setEnabled(True)
                self.b2.setEnabled(True)

            elif not array:
                self.l.setText('Empty file !! Please enter valid file name...')
        else:
            self.l.setText('File not found!! Please enter valid file name...')
            self.l5.setText(" ")
            self.l6.setText(" ")
            self.l7.setText(" ")
            self.l8.setText(" ")

#    def btn1_click(self):
#        if 1 in a:
#            co = self.le1.text()
#            mg = self.le2.text()
#            if len(co)>=1 and len(mg)>=1 and (any(c.isdigit() for c in mg)) and not (any(c.isalpha() for c in mg)):
#                array.sort(key=operator.itemgetter(1), reverse=True)
#                with open( co+'.csv' ,'w') as csvfile:
#                    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                    filewriter.writerow(["Player" , "Score"])
#                    for x in array:
#                        if x[1]<mg:
#                            break
#                        filewriter.writerow([x[0], x[1]])

#                self.l3.setText('File saved with name ' + co+'.csv')
#                del array[:]
#                del a[:]
#            else:
#                self.l3.setText('Error! Please enter valid player and score first.')
#        else:
#            self.l3.setText('Please upload a valid file first.')

    def btn2_click(self):
        if 1 in a:
            global cgpa,wood,food,gold,stone,vils,mils,time
            data = pd.read_csv('aotstats.txt')
            player= np.array(data['player'].head(4))
            demo = data.loc[data['player'] == self.cb.currentText()]
            cgpa = np.array(demo['wood'])
            wood = np.array(demo['wood'])
            food = np.array(demo['food'])
            gold = np.array(demo['gold'])
            stone = np.array(demo['stone'])
            vils = np.array(demo['vils'])
            mils = np.array(demo['mils'])
            time = np.array(demo['time'])

            score_parray = data.tail(4)
            score_data = score_parray.loc[score_parray['player'] == self.cb.currentText()]
            score = (np.array(score_data['mils']) * 15) + (np.array(score_data['vils']) * 10 ) + ((np.array(score_data['food']) + np.array(score_data['wood'])+ np.array(score_data['gold'])+ np.array(score_data['stone'])) * 0.2)

            self.l7.setText("Score:       "+ str(score))
            self.l8.setText("Players: "+ str(player))
            self.b3.setEnabled(True)
            self.b4.setEnabled(True)
        else:
            self.l7.setText('Error! Please upload a valid file first...')
            self.l5.setText(' ')
            self.l6.setText(' ')
            self.l8.setText(' ')

    def graph(self):
        if 1 in a:
            if time.any():
                #plt.bar(range(len(time)), wood)
                #plt.bar(range(len(time)), food)
                #plt.bar(range(len(time)), stone)
                #plt.bar(range(len(time)), gold)
                #plt.xlabel('Students')
                #plt.ylabel('CGPA')
                #data = {'a': time,
                #        'c': np.random.randint(0, len(wood), len(wood)),
                #        'd': np.random.randn(len(wood))}
                #data['b'] = np.array(wood)
                #groups = ("coffee", "tea", "water")
                #plt.scatter('a', 'b', c='c', s='d', data=data,label=groups)
                plt.plot(np.array(time), np.array(wood))
                plt.plot(np.array(time), np.array(food))
                plt.plot(np.array(time), np.array(gold))
                plt.plot(np.array(time), np.array(stone))
                plt.plot(np.array(time), np.array(vils))
                plt.plot(np.array(time), np.array(mils))
                plt.legend(["Wood", "Food", "Gold", "Stone", "Vils", "Mils"])
                plt.xlabel('Time')
                plt.ylabel('Resources')
                plt.show()
                self.l9.setText("Histograph plotted")
                #np.delete(cgpa)
            else:
                self.l9.setText("Please calculate aggregated data first")
        else:
            self.l9.setText("Please calculate aggregated data first")

    def draw_chart(self, r_time, r_wood, r_food, r_gold, stone):
         self.pl.setData(x=r_time, y=r_wood)
         #cnt = len(r_time)
         #new_y = []
         #for i in range(cnt):
             #new_y.append(time[cnt])
         bar_chart = pg.BarGraphItem(x=r_time, height=r_wood, width=1, brush='y', pen='r')
         self.pw2.addItem(bar_chart)
         bar_chart2 = pg.BarGraphItem(x=r_time, height=r_food, width=1, brush='y', pen='r')
         self.pw3.addItem(bar_chart2)
         bar_chart3 = pg.BarGraphItem(x=r_time, height=r_gold, width=1, brush='y', pen='r')
         self.pw4.addItem(bar_chart3)

    def replay(self):
        self.mytimer = QTimer()
        if self.cb_speed.currentText() == "Real Time":
            self.mytimer.start(1000)
        if self.cb_speed.currentText() == "2x Accelerated":
            self.mytimer.start(500)
        if self.cb_speed.currentText() == "4x Accelerated":
            self.mytimer.start(250)
        if self.cb_speed.currentText() == "16x Accelerated":
            self.mytimer.start(62.5)
        self.mytimer.timeout.connect(self.get_data)
        self.draw_chart(self.r_time, self.r_wood, self.r_food, self.r_gold,self.r_stone)
        self.counter = 0
        self.show()

    def download(self):
        url = 'http://operations.sparsetechnology.com/public/users/yca/aotstats.txt'
        r = requests.get(url, allow_redirects=True)
        urllib.request.urlretrieve(url, 'aotstats.txt')
        self.b.setEnabled(True)

    @pyqtSlot()
    def get_data(self):        
        #data: str = time.strftime("%S", time.localtime())
        #last_x = self.x[-1]
        self.counter += 1
        self.r_time.append(np.array(time[self.counter]))
        self.r_wood.append(np.array(food[self.counter]))
        self.r_food.append(np.array(food[self.counter]))
        self.r_gold.append(np.array(food[self.counter]))
        self.r_stone.append(np.array(food[self.counter]))
        self.draw_chart(self.r_time,self.r_wood, self.r_food, self.r_gold, self.r_stone)

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
