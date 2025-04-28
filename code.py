# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:59:45 2025

@author: janis
"""

import pyvisa as pv
import time
import numpy as np


def plot(title, xlab, ylab, data, resol, name, format1, save):
    import matplotlib.pyplot as plt
    plt.title(label = title)
    plt.xlabel(xlabel = xlab)
    plt.ylabel(ylabel = ylab)
    plt.grid(visible = True, axis = "both", which = "both")
    plt.scatter(x = data[0], y = data[1], color = 'blue', marker = "x", linewidth = 2, label = "data points")
    plt.legend()
    
    from datetime import datetime
    now = str (datetime.now()).replace(" ", "_")
    if (save):
        plt.savefig(fname = name + title + now + "."+format1, format = format1, dpi = resol, transparent = True)
    plt.show()

def writeFile(file, data):
    filename = file
    f = open(filename, 'w')
    for i in len(data[0]):
        line = ""
        for j in len(data):
            line = line + "," + data[j][i]
        if len(line) > 0:
            line = line[1:]
        f.write(line + "\n")

### start of execution

rm = pv.ResourceManager()
resource = rm.list_resources()

def task1_1():
    lists = [["$U_{in}", "$\displaystyle \si{\volt}$"]["$U_{out}$", "$\displaystyle \si{\volt}$"]]
    
    genVolt = rm.open(resource[1])
    genVolt.write('OUTP:MODE AC')
    genVolt.write("VOLT 1.0")
    genVolt.write("OUTP ON")
    
    voltMeter = rm.open(resource[2])
    print(voltMeter.write('*IDN?'))
    value = voltMeter.write(":MEASure:VOLTage:DC?")
    
    measTime = 0.4
    
    plotDat = [lists[0][2:], lists[1][2:]]
    
    for i in np.arrange(30, 3000, 50):
        genVolt.write("FREQ "+str(i))
        value = voltMeter.write(":MEASure:VOLTage:DC?")
        lists[0].append(i)
        lists[1].append(float(value))
        plot("RC-Hochpass", "f in Hz", "Amplitude in V", plotDat, 1200, "frequenzgang", "jpg", False)
        time.sleep(measTime)
    
    voltMeter.close()
    genVolt.write("OUTP OFF")
    genVolt.close()
    plot("RC-Hochpass", "f in Hz", "Amplitude in V", lists, 1200, "frequenzgang", "jpg", True)
    
    writeFile("freqRCHoch1_1.csv", lists)

def task1_4():
    lists = [["$U_{in}", "$\si{\volt}$"]["RLC-meter", "$\displaystyle \si{\volt}$"]]
    
    genVolt = rm.open(resource[1])
    genVolt.write('OUTP:MODE AC')
    genVolt.write("VOLT 1.0")
    genVolt.write("OUTP ON")
    
    rlcMet = rm.open(resource[3])
    print(rlcMet.write('*IDN?'))
    value = rlcMet.write(":MEASure:VOLTage:DC?")
    
    measTime = 0.4
    
    plotDat = [lists[0][2:], lists[1][2:]]
    
    for i in np.arrange(30, 3000, 50):
        genVolt.write("FREQ "+str(i))
        rlcMet.write('INIT')
        value = rlcMet.query("READ?")
        lists[0].append(i)
        lists[1].append(float(value))
        plot("kondensator", "f in Hz", "Amplitude in V", plotDat, 1200, "frequenzgang", "jpg", False)
        time.sleep(measTime)
    
    rlcMet.close()
    genVolt.wrie("OUTP OFF")
    plot("RC-Hochpass", "f in Hz", "Amplitude in V", lists, 1200, "frequenzgang", "jpg", True)
    
    writeFile("condensator1_4.csv", lists)

def task2_2a():
    lists = [["$U_{in}", "$\displaystyle \si{\volt}$"]["$U_{out}$", "$\displaystyle \si{\volt}$"]]
    
    genVolt = rm.open(resource[1])
    genVolt.write('OUTP:MODE AC')
    genVolt.write("VOLT 1.0")
    genVolt.write("OUTP ON")
    
    voltMeter = rm.open(resource[2])
    print(voltMeter.write('*IDN?'))
    value = voltMeter.write(":MEASure:VOLTage:DC?")
    
    measTime = 0.4
    
    plotDat = [lists[0][2:], lists[1][2:]]
    
    for i in np.arrange(30, 3000, 50):
        genVolt.write("FREQ "+str(i))
        value = voltMeter.write(":MEASure:VOLTage:DC?")
        lists[0].append(i)
        lists[1].append(float(value))
        plot("LC-Hochpass1stOrder", "f in Hz", "Amplitude in V", plotDat, 1200, "frequenzgang", "jpg", False)
        time.sleep(measTime)
    
    voltMeter.close()
    genVolt.write("OUTP OFF")
    genVolt.close()
    plot("LC-Hochpass1stOrder", "f in Hz", "Amplitude in V", lists, 1200, "frequenzgang", "jpg", True)
    
    writeFile("freqRCHoch2_4_1stOrder.csv", lists)

def task2_2b():
    lists = [["$U_{in}", "$\displaystyle \si{\volt}$"]["$U_{out}$", "$\displaystyle \si{\volt}$"]]
    
    genVolt = rm.open(resource[1])
    genVolt.write('OUTP:MODE AC')
    genVolt.write("VOLT 1.0")
    genVolt.write("OUTP ON")
    
    voltMeter = rm.open(resource[2])
    print(voltMeter.write('*IDN?'))
    value = voltMeter.write(":MEASure:VOLTage:DC?")
    
    measTime = 0.4
    
    plotDat = [lists[0][2:], lists[1][2:]]
    
    for i in np.arrange(30, 3000, 50):
        genVolt.write("FREQ "+str(i))
        value = voltMeter.write(":MEASure:VOLTage:DC?")
        lists[0].append(i)
        lists[1].append(float(value))
        plot("LC-Hochpass2ndOrder", "f in Hz", "Amplitude in V", plotDat, 1200, "frequenzgang", "jpg", False)
        time.sleep(measTime)
    
    voltMeter.close()
    genVolt.write("OUTP OFF")
    genVolt.close()
    plot("LC-Hochpass2ndOrder", "f in Hz", "Amplitude in V", lists, 1200, "frequenzgang", "jpg", True)
    
    writeFile("freqRCHoch2_4_2ndOrder.csv", lists)

if (__name__ == '__main__'):
    task1_1()
    # tasl1_4()