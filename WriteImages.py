from PIL import Image
import math
from random import randint

#Make Xs
k = math.pi/2
count = 0
for length in range(3, 7):
    for j in range(0, 18):
        count = count + 1
        angle = 5*j*(math.pi/180)
        angle2 = k
        csn = math.cos(angle)
        csn2 = math.cos(angle + angle2)
        slope = math.tan(angle)
        slope2 = math.tan(angle+angle2)
        a = []

        for xp in range(0,15):
            for yp in range(0,15):
                a.append((0, 0, 0))
        for c in range(0, length + 1):
            dx1 = c * csn + 0
            nx1 = math.floor(dx1)
            dx1 = dx1 - nx1
            nx2 = -nx1
            dx2 = -dx1
            dx3 = c * csn2
            nx3 = math.floor(dx3)
            dx3 = dx3-nx3
            nx4 = -nx3
            dy1 = slope * (nx1+dx1) + 0
            my1 = math.floor(dy1)
            dy1 = dy1 - my1
            my2 = -my1
            dy3 = slope2 * (nx3 + dx3)
            my3 = math.floor(dy3)
            dy3 = dy3 - my3
            my4 = -my3
            v11 = int(205 * (1 - dx1) * (1 - dy1))
            v12 = int(205 * (1 - dx1) * dy1)
            v21 = int(205 * dx1 * (1 - dy1))
            v22 = int(205 * dx1 * dy1)

            temp = a[int(((-my1)+7)*15+nx1+7)]
            a[int(((-my1)+7)*15+nx1+7)] = (temp[0]+v11,temp[1]+v11,temp[2]+v11)
            temp = a[int(((-my1)+7)*15+(nx1+1)+7)]
            a[int(((-my1)+7)*15+(nx1+1)+7)] = (temp[0]+v21,temp[1]+v21,temp[2]+v21)
            temp = a[int(((-(my1 + 1))+7)*15+nx1+7)]
            a[int(((-(my1 + 1))+7)*15+nx1+7)] = (temp[0]+v12,temp[1]+v12,temp[2]+v12)
            temp = a[int(((-(my1 + 1))+7)*15+(nx1+1)+7)]
            a[int(((-(my1 + 1))+7)*15+(nx1+1)+7)] = (temp[0]+v22,temp[1]+v22,temp[2]+v22)

            temp = a[int(((-my2)+7)*15+nx2+7)]
            a[int(((-my2)+7)*15+nx2+7)] = (temp[0]+v11,temp[1]+v11,temp[2]+v11)
            temp = a[int(((-my2)+7)*15+(nx2-1)+7)]
            a[int(((-my2)+7)*15+(nx2-1)+7)] = (temp[0]+v21,temp[1]+v21,temp[2]+v21)
            temp = a[int(((-(my2 - 1))+7)*15+nx2+7)]
            a[int(((-(my2 - 1))+7)*15+nx2+7)] = (temp[0]+v12,temp[1]+v12,temp[2]+v12)
            temp = a[int(((-(my2 - 1))+7)*15+(nx2-1)+7)]
            a[int(((-(my2 - 1))+7)*15+(nx2-1)+7)] = (temp[0]+v22,temp[1]+v22,temp[2]+v22)

            v11 = int(255 * (1 - dx3) * (1 - dy3))
            v12 = int(255 * (1 - dx3) * dy3)
            v21 = int(255 * dx3 * (1 - dy3))
            v22 = int(255 * dx3 * dy3)

            temp = a[int(((-my3)+7)*15+nx3+7)]
            a[int(((-my3)+7)*15+nx3+7)] = (temp[0]+v11,temp[1]+v11,temp[2]+v11)
            temp = a[int(((-my3)+7)*15+(nx3+1)+7)]
            a[int(((-my3)+7)*15+(nx3+1)+7)] = (temp[0]+v21,temp[1]+v21,temp[2]+v21)
            temp = a[int(((-(my3 + 1))+7)*15+nx3+7)]
            a[int(((-(my3 + 1))+7)*15+nx3+7)] = (temp[0]+v12,temp[1]+v12,temp[2]+v12)
            temp = a[int(((-(my3 + 1))+7)*15+(nx3+1)+7)]
            a[int(((-(my3 + 1))+7)*15+(nx3+1)+7)] = (temp[0]+v22,temp[1]+v22,temp[2]+v22)

            temp = a[int(((-my4)+7)*15+nx4+7)]
            a[int(((-my4)+7)*15+nx4+7)] = (temp[0]+v11,temp[1]+v11,temp[2]+v11)
            temp = a[int(((-my4)+7)*15+(nx4-1)+7)]
            a[int(((-my4)+7)*15+(nx4-1)+7)] = (temp[0]+v21,temp[1]+v21,temp[2]+v21)
            temp = a[int(((-(my4- 1))+7)*15+nx4+7)]
            a[int(((-(my4 - 1))+7)*15+nx4+7)] = (temp[0]+v12,temp[1]+v12,temp[2]+v12)
            temp = a[int(((-(my4 - 1))+7)*15+(nx4-1)+7)]
            a[int(((-(my4 - 1))+7)*15+(nx4-1)+7)] = (temp[0]+v22,temp[1]+v22,temp[2]+v22)
        img = Image.new('RGB', (15, 15))
        img.putdata(tuple(a))
        img.save('x' + str(count) + '.png')

#Make Os
count = 0

for circ in range(1, 43):
    count = count + 1
    angle = 24.0/circ
    rad = circ/(2*math.pi)

    a = []

    for xp in range(0,15):
        for yp in range(0,15):
            a.append((0, 0, 0))
    for c in range(0, 15*circ):
        dx = rad*math.cos(angle*c)
        dy = rad*math.sin(angle*c)
        x = math.floor(dx)
        dx = dx - x
        y = math.floor(dy)
        dy = dy - y

        v11 = int(14 * (1 - dx) * (1 - dy))
        v12 = int(14 * (1 - dx) * dy)
        v21 = int(14 * dx * (1 - dy))
        v22 = int(14 * dx * dy)

        temp = a[int(((-y)+7)*15+x+7)]
        a[int(((-y)+7)*15+x+7)] = (temp[0]+v11,temp[1]+v11,temp[2]+v11)
        temp = a[int(((-y)+7)*15+(x+1)+7)]
        a[int(((-y)+7)*15+(x+1)+7)] = (temp[0]+v21,temp[1]+v21,temp[2]+v21)
        temp = a[int(((-(y + 1))+7)*15+x+7)]
        a[int(((-(y + 1))+7)*15+x+7)] = (temp[0]+v12,temp[1]+v12,temp[2]+v12)
        temp = a[int(((-(y + 1))+7)*15+(x+1)+7)]
        a[int(((-(y + 1))+7)*15+(x+1)+7)] = (temp[0]+v22,temp[1]+v22,temp[2]+v22)
    img = Image.new('RGB', (15, 15))
    img.putdata(tuple(a))
    img.save('c' + str(count) + '.png')
