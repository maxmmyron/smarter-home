import turtle

sr_light = 0
sr_temp_int = 25
sr_heater = 0
sr_ac = 1

tls = turtle.Turtle()
tls.hideturtle()
tls.speed(0)
sr = turtle.Turtle()
sr_temp = turtle.Turtle()

tls.color("black", "cyan")

if sr_light == 1:
    tls.color("black", "orange")

#top left square 
tls.begin_fill()

tls.left(90)
tls.forward(100)
tls.left(90)
tls.forward(100)
tls.left(90)
tls.forward(100)
tls.left(90)
tls.forward(100)

tls.end_fill()


if sr_heater == 1 and sr_ac ==1:
    sr_temp.hideturtle()
    sr_temp.speed(0)
    sr_temp.penup()
    sr_temp.setx(-98)
    sr_temp.sety(30)
    sr_temp.write(str(sr_temp_int) + " Degrees Warning")

elif sr_heater == 1 and sr_ac == 0:
    sr_temp.hideturtle()
    sr_temp.speed(0)
    sr_temp.penup()
    sr_temp.setx(-80)
    sr_temp.sety(30)
    sr_temp.color("red")
    sr_temp.write(str(sr_temp_int) + " Degrees")
    
elif sr_ac == 1 and sr_heater == 0:
    sr_temp.hideturtle()
    sr_temp.speed(0)
    sr_temp.penup()
    sr_temp.setx(-80)
    sr_temp.sety(30)
    sr_temp.color("blue")
    sr_temp.write(str(sr_temp_int) + " Degrees")

else :
    sr_temp.hideturtle()
    sr_temp.speed(0)
    sr_temp.penup()
    sr_temp.setx(-80)
    sr_temp.sety(30)
    sr_temp.write(str(sr_temp_int) + " Degrees")


#sitting room text
sr.hideturtle()
sr.speed(0)
sr.penup()
sr.setx(-80)
sr.sety(50)
sr.write("Sitting Room")

#kitchen

k_light = 1
k_temp_int = 19
k_heater = 1
k_ac = 1

trs = turtle.Turtle()
trs.hideturtle()
trs.speed(0)
k = turtle.Turtle()
k_temp = turtle.Turtle()

trs.color("black", "cyan")

if k_light == 1:
    trs.color("black", "orange")

#top right square 
trs.begin_fill()

trs.forward(100)
trs.left(90)
trs.forward(100)
trs.left(90)
trs.forward(100)
trs.left(90)
trs.forward(100)

trs.end_fill()


if k_heater == 1 and k_ac ==1:
    k_temp.hideturtle()
    k_temp.speed(0)
    k_temp.penup()
    k_temp.setx(2)
    k_temp.sety(30)
    k_temp.write(str(k_temp_int) + " Degrees Warning")

elif k_heater == 1 and k_ac == 0:
    k_temp.hideturtle()
    k_temp.speed(0)
    k_temp.penup()
    k_temp.setx(30)
    k_temp.sety(30)
    k_temp.color("red")
    k_temp.write(str(k_temp_int) + " Degrees")
    
elif k_ac == 1 and k_heater == 0:
    k_temp.hideturtle()
    k_temp.speed(0)
    k_temp.penup()
    k_temp.setx(30)
    k_temp.sety(30)
    k_temp.color("blue")
    k_temp.write(str(k_temp_int) + " Degrees")

else :
    k_temp.hideturtle()
    k_temp.speed(0)
    k_temp.penup()
    k_temp.setx(30)
    k_temp.sety(30)
    k_temp.write(str(k_temp_int) + " Degrees")


#Kitchen text
k.hideturtle()
k.speed(0)
k.penup()
k.setx(30)
k.sety(50)
k.write("Kitchen")

#Bathroom

br_light = 0
br_temp_int = 9
br_heater = 1
br_ac = 0

brs = turtle.Turtle()
br = turtle.Turtle()
br_temp = turtle.Turtle()

brs.color("black", "cyan")

if br_light == 1:
    brs.color("black", "orange")

#bottom right square 

brs.hideturtle()
brs.speed(0)

brs.begin_fill()

brs.right(90)
brs.forward(100)
brs.left(90)
brs.forward(100)
brs.left(90)
brs.forward(100)
brs.left(90)
brs.forward(100)

brs.end_fill()


if br_heater == 1 and br_ac ==1:
    br_temp.hideturtle()
    br_temp.speed(0)
    br_temp.penup()
    br_temp.setx(2)
    br_temp.sety(-70)
    br_temp.write(str(br_temp_int) + " Degrees Warning")

elif br_heater == 1 and br_ac == 0:
    br_temp.hideturtle()
    br_temp.speed(0)
    br_temp.penup()
    br_temp.setx(30)
    br_temp.sety(-70)
    br_temp.color("red")
    br_temp.write(str(br_temp_int) + " Degrees")
    
elif br_ac == 1 and br_heater == 0:
    br_temp.hideturtle()
    br_temp.speed(0)
    br_temp.penup()
    br_temp.setx(30)
    br_temp.sety(-70)
    br_temp.color("blue")
    br_temp.write(str(br_temp_int) + " Degrees")

else :
    br_temp.hideturtle()
    br_temp.speed(0)
    br_temp.penup()
    br_temp.setx(30)
    br_temp.sety(-70)
    br_temp.write(str(br_temp_int) + " Degrees")


#Bathroom text
br.hideturtle()
br.speed(0)
br.penup()
br.setx(30)
br.sety(-50)
br.write("Bathroom")

turtle.done()