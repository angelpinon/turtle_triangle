import math
from turtle import *

##Law of Cosine

def myTriangle():
    firstSide = int(input("first side length:" ))
    secondSide = int(input("second side length: "))
    firstAngle = int(input("first angle: "))

    thirdSide = (pow(firstSide,2)+pow(secondSide,2))-((2)*(secondSide)*(firstSide)*(math.cos(math.radians(firstAngle))))
    thirdSide2 = pow(thirdSide,0.5)

    print(thirdSide2)


    secondAngle = math.acos(((pow(secondSide,2))-(pow(firstSide,2))-(pow(thirdSide2,2)))/((-2)*(firstSide)*(thirdSide2)))
    secondAngle2 = math.degrees(secondAngle)

    print(secondAngle2)


    thirdAngle = 180-firstAngle-secondAngle2

    print(thirdAngle)


    ##Turtle Drawing##
    pinon = Turtle()

    pinon.goto(0,0)
    pinon.down()
    pinon.forward(firstSide)
    pinon.left(180-thirdAngle)
    pinon.forward(secondSide)
    pinon.left(180-firstAngle)
    pinon.forward(thirdSide2)


if __name__=="__main__":
    myTriangle()
