from random import randint
from PIL import Image
import math
import matplotlib.pyplot as plt
import numpy as np

aa = 0.025

i_s = 225 + 1 #15 * 15 pixel image + bias node

w_gh=[[0.0/i_s]*i_s for i in range(i_s)]
w_hi=[[0.0/i_s]*i_s for i in range(i_s)]
w_ij=[[0.0/i_s]*i_s for i in range(i_s)]
w_jk=[[0.0/i_s]*i_s for i in range(i_s)]
w_ko=[[0.0/i_s]*i_s for i in range(2)]

#initialize Nodes
NG=[0]*i_s
NH=[0]*i_s
NI=[0]*i_s
NJ=[0]*i_s
NK=[0]*i_s
DO = [0] * 2
O=[0]*2 # init output

dw_gh=[[.5/i_s]*i_s for i in range(i_s)]
dw_gh2=[[.5/i_s]*i_s for i in range(i_s)]
dw_hi=[[.5/i_s]*i_s for i in range(i_s)]
dw_hi2=[[.5/i_s]*i_s for i in range(i_s)]
dw_ij2=[[.5/i_s]*i_s for i in range(i_s)]
dw_jk2=[[.5/i_s]*i_s for i in range(i_s)]
dw_ko2=[[.5/i_s]*i_s for i in range(2)]
dw_ij=[[.5/i_s]*i_s for i in range(i_s)]
dw_jk=[[.5/i_s]*i_s for i in range(i_s)]
dw_ko=[[.5/i_s]*i_s for i in range(2)]

errco = 1.0/(3*i_s*i_s)
z_gh=[[0]*i_s for i in range(i_s)]
z_hi=[[0]*i_s for i in range(i_s)]
z_ij=[[0]*i_s for i in range(i_s)]
z_jk=[[0]*i_s for i in range(i_s)]
z_ko=[[0]*i_s for i in range(2)]
zweight = 0

#global variables
g_tsetsize = 5
g_tcyclesize = 3
g_tsetsnum = 50
g_cfiles = 42
g_xfiles = 72


inputv = [[0]*255]
targets = [0] * (g_tsetsize*4)
errors = []

def sigmoid(x):
    if x > 500:
        x = 500.0
    if x < -500:
        x = -500.0
    return 1 / (1 + math.exp(-x))

#read in network state (filenames, type)
def getNetState():
    saveFile = open("savedstate.bin", "rb")
    x = np.fromfile(saveFile, "float")
    saveFile.close()
    y = i_s*i_s
    for i in range(i_s):
        for j in range(i_s):
            w_gh[i][j] = x[i*i_s + j]
            w_hi[i][j] = x[i*i_s + j + y]
            w_ij[i][j] = x[i*i_s + j + (y*2)]
            w_jk[i][j] = x[i*i_s + j + (y*3)]
    for i in range(2):
        for j in range(i_s):
            w_ko[i][j] = x[i*i_s + j + (y*4)]
    #returns weights + vals



#Calculate Outputs
def calcoutputs(inputv, n):
    for g in range(i_s): #calculate Hth nodes
        NG[g] = inputv[n][g]
        #NI[i] = sigmoid(NI[i])
    NG[225] = 1 #bias node
    for h in range(i_s): #calculate Ith nodes
        NH[h] = 0
        for g in range(i_s):
            NH[h] = NH[h] + w_gh[g][h] * NG[g]
        NH[h] = sigmoid(NH[h])
    NH[225] = 1 #bias node
    for i in range(i_s): #calculate Ith nodes
        NI[i] = 0
        for h in range(i_s):
            NI[i] = NI[i] + w_hi[h][i] * NH[h]
        NI[i] = sigmoid(NI[i])
    NI[225] = 1 #bias node
    for j in range(i_s): #calculate Jth nodes
        NJ[j] = 0
        for i in range(i_s):
            NJ[j] = NJ[j] + w_ij[i][j] * NI[i]
        NJ[j] = sigmoid(NJ[j])
    NJ[225] = 1 #bias node
    for k in range(i_s): #calculate Kth nodes
        NK[k] = 0
        for j in range(i_s):
            NK[k] = NK[k] + w_jk[j][k] * NJ[j]
        NK[k] = sigmoid(NK[k])
    NK[225] = 1 #bias node
    for _o in range(2): #calculate Oth nodes
        O[_o] = 0
        for k in range(i_s):
            O[_o]= O[_o] + w_ko[_o][k] * NK[k]
        O[_o] = sigmoid(O[_o])

counter = 1
xaxis = []

error_b=0
error_x=0
error_o=0
error_xo=0
display_data_cnt=0
spread=10

getNetState()
for _x in range(1, 73):
    for __o in range(1, 31):
        for x in range(225):
            inputv[0][x] = randint(1, 50)
        targets = [0, 0]
        calcoutputs(inputv, 0)
        if (abs(round(O[0])-targets[0])+ abs(round(O[1])-targets[1]) > 0):
            error_b+=1
        if(display_data_cnt%spread < 1):
            print(targets, O, error_b, 100*error_b/(display_data_cnt + 1.0))

        img = Image.open('x' + str(_x) + '.png')
        for x in range(225):
            inputv[0][x] = list(img.getdata())[x][0] + randint(1, 50)
        targets = [1, 0]
        calcoutputs(inputv, 0)
        if (abs(round(O[0])-targets[0])+ abs(round(O[1])-targets[1]) > 0):
            error_x+=1
        if(display_data_cnt%spread < 1):
            print(targets, O, error_x, 100*error_x/(display_data_cnt + 1.0))

        img = Image.open('c' + str(12+__o) + '.png')
        for x in range(225):
            inputv[0][x] = list(img.getdata())[x][0] + randint(1, 50)
        targets = [0, 1]
        calcoutputs(inputv, 0)
        if (abs(round(O[0])-targets[0])+ abs(round(O[1])-targets[1]) > 0):
            error_o+=1
        if(display_data_cnt%spread < 1):
            print(targets, O, error_o, 100*error_o/(display_data_cnt + 1.0))

        img = Image.open('c' + str(12+__o) + '.png')
        img2 = Image.open('x' + str(_x) + '.png')
        for x in range(225):
            a = list(img.getdata())[x][0] + list(img2.getdata())[x][0]+ randint(1, 50)
            if a > 255:
                a = 255
            inputv[0][x] = a
        targets = [1, 1]
        calcoutputs(inputv, 0)
        if (abs(round(O[0])-targets[0])+ abs(round(O[1])-targets[1]) > 0):
            error_xo+=1
        if(display_data_cnt%spread < 1):
            print(targets, O, error_xo, 100*error_xo/(display_data_cnt + 1.0))


        display_data_cnt +=1


print(targets, errors, O)
plt.plot(xaxis, errors)
plt.show()
