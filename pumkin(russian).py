import turtle,time
wn=turtle.Screen()
wn.setup(1000,700)
wn.bgpic('street.gif')
wn.addshape('man.gif')
man=turtle.Turtle()
man.up()
man.goto(-80,-240)
man.shape('man.gif')
for i in range(200):
    man.fd(2)
    time.sleep(0.01)
    
