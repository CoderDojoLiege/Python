from turtle import *
speed(8)

def dessinecarre (x,y, l) :
	color("blue", "green")
	begin_fill()
	
	up()
	goto(x,y)
	down()
	for i in range(4):
		forward(l)
		right(90)
		
	end_fill()

def dessine3carre (x,y, l) :		
		
	dessinecarre (x,y, l)
	dessinecarre (x+l,y, l)
	dessinecarre (x+l+l+l,y, l)

def dessineface (x,y, l) :
 
	dessine3carre (x,y, l)
	dessine3carre (x,y-l, l)
	dessine3carre (x,y-l-l, l)




dessineface (-100,100, 50)
dessineface (-200,200, 50)
speed (0)
color ("red")
up()
goto(100,0)
down()
for i in range (1) : 
	right (60)
	forward (70)
	left (120)
	forward (150)
up()	
goto(1000000,8678)	
exitonclick()
