import turtle,time
wn=turtle.Screen()
wn.bgpic('street.gif')
image=['00.gif','01.gif','02.gif',\
        '03.gif','04.gif','05.gif',\
        '06.gif','07.gif','08.gif',\
        '09.gif']

image1=['00r.gif','01r.gif','02r.gif',\
        '03r.gif','04r.gif','05r.gif',\
        '06r.gif','07r.gif','08r.gif',\
        '09r.gif']
man=turtle.Turtle()
man.up()
man.goto(-40,-275)
def addshapes():
    for i in range(10):
        wn.addshape(image[i])
        wn.addshape(image1[i])
addshapes()

while True:
    for m in range(60):
        m1=m%10
        man.shape(image[m1])
        man.fd(10)
        time.sleep(0.2)
    for m in range(60):
        m1=m%10
        man.shape(image1[m1])
        man.fd(-10)
        time.sleep(0.2)
    
            
        
    
    
    
