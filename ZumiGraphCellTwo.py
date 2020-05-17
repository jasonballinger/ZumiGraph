from zumi.zumi import Zumi
import IPython.display
from IPython.display import Image
import math
import time

G = Graph()
zumi = Zumi()
zumi.mpu.calibrate_MPU()
# make sure to reset the gyro
# since we are using go_straight()
zumi.reset_gyro()

# CONSTANTS
DIV_CONST = 6.0
POWER = 40


def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time


def change_curr_heading_to_desired_heading(currAngle, desiredAngle):
    turn_magnitude = abs(currAngle - desiredAngle)

    # turning left
    if currAngle < desiredAngle:
        zumi.turn_left(turn_magnitude)
        return desiredAngle
    # turning right
    elif currAngle > desiredAngle:
        zumi.turn_right(turn_magnitude)
        return desiredAngle
    else:
        return desiredAngle


def load_graph(num):
    global G

    while num < 1 or num > 5:
        num = input("Invalid Graph number, please enter a new one:  ")
        num = int(num)

    fileName = ""

    if num == 1:
        # set the file name
        fileName = "simpleG.jpg"
        G.create_simple()
    elif num == 2:
        # set the file name
        fileName = "simp_diff_len.jpg"
        G.create_simple_different_road_lengths()
    elif num == 3:
        # set the file name
        fileName = "simp_diff_ang.jpg"
        G.create_simple_different_angles()
    elif num == 4:
        # set the file name
        fileName = "mystery.jpg"
        G.mystery_graph()
    elif num == 5:
        # set the file name
        fileName = "complex.jpg"
        G.create_complex()

        # display the image here
    display(Image(filename=('/home/pi/Dashboard/user/jason/MyImages/' + fileName), width=300, height=200))


def printTable():
    print("1 - G.create_simple()")
    print("2 - G.create_simple_different_road_lengths()")
    print("3 - G.create_simple_different_angles()")
    print("4 - G.mystery_graph()  ")
    print("5 - G.create_complex() ")


def load_route(dictionary):
    global G

    print("Vertices: [ ", end='')
    # first print all the keys = letters out to the console
    for key in dictionary:
        print(key, end=', ')
    print("]")

    # prompt the user to enter a startNode
    startVertex = input("Input a starting Vertex:  ")

    while startVertex not in dictionary:
        print("You entered an INVALID vertex ")
        startVertex = input("Input a starting Vertex again:  ")

    # print what the user entered
    print(startVertex)

    # prompt the user to enter a endNode
    endVertex = input("Input a ending Vertex:  ")

    while endVertex not in dictionary:
        print("You entered an INVALID vertex ")
        endVertex = input("Input a end Vertex again:  ")

    # print what the user entered
    print(endVertex)

    return G.search(startVertex, endVertex)


def main():
    # display to the user what are the graph options
    printTable()
    # prompt the user for a graph to load
    graph_num = input("Load Graph #")
    graph_num = int(graph_num)  # converted the data from a string into an integer
    load_graph(graph_num)

    # ask the user for two way-points so Zumi can figure out a route
    route = load_route(G.nodes_dict)

    print("-----  Final Route: ----- ")
    i = 0
    for item in route:
        print("\t edge name: ", item[0].get_edgeName(), "desired angle", item[1])
        i += 1

    heading = 90

    while len(route) != 0:
        pair = route[0]
        edge = pair[0]
        distance = edge.road_length
        desired_angle = pair[1]

        print("desired_angle==", desired_angle)
        # Step1: change heading to desired heading
        heading = change_curr_heading_to_desired_heading(heading, desired_angle)

        # Step2: get the distance we need to go
        desired_distance = distance
        print("desired_distance==", desired_distance)
        total_time = getTimeForTravel(desired_distance)
        zumi.forward(POWER, total_time)

        # Step3: deletes the first element in list
        route.pop(0)


if __name__ == "__main__":
    try:
        main()
    finally:
        zumi.stop()
        print("done")