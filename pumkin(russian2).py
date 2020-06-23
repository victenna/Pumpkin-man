import turtle,time
wn=turtle.Screen()
wn.bgpic('street.gif')
image=['00.gif','01.gif','02.gif',\
        '03.gif','04.gif','05.gif',\
        '06.gif','07.gif','08.gif',\
        '09.gif']
man=turtle.Turtle()
man.up()
man.goto(-40,-275)
def addshapes():
    for i in range(10):
        wn.addshape(image[i])
addshapes()
for m in range(100):
    m1=m%10
    man.shape(image[m1])
    man.fd(10)
    time.sleep(0.2)
    
    
    
