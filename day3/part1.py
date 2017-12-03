num=int(open('day3.input').read().rstrip())

n=1
x=0
y=0

xmin=0
xmax=0
ymin=0
ymax=0
d=0
dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

mem={}

while n<num:
    if n==1:
        mem[(x, y)]=1
    else:
        mem[(x, y)]=0
        for xx in range(-1, 2):
            for yy in range(-1, 2):
                if (x+xx, y+yy) not in mem:
                    mem[(x+xx, y+yy)]=0
                if xx==0 and yy==0:
                    continue
                mem[(x, y)]+=mem[(x+xx, y+yy)]
    x+=dx[d]
    y+=dy[d]
    if x<xmin or x>xmax or y<ymin or y>ymax:
        d=(d+1)%4
        ymin=min(y, ymin)
        ymax=max(y, ymax)
        xmin=min(x, xmin)
        xmax=max(x, xmax)
    n+=1

print abs(x)+abs(y)
