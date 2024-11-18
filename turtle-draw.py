import turtle
import math

TEXTFILENAME_PROMPT = "Please enter the name of the input file: "
WINDOW_SIZE = 450

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

window = turtle.Screen()
window.title("Turtle Drawing Application")
window.screensize(WINDOW_SIZE, WINDOW_SIZE)

spiral = turtle.Turtle()
spiral.speed(0)
spiral.penup()

input_filename = input(TEXTFILENAME_PROMPT).strip()

total_distance = 0
current_x, current_y = 0, 0

try:
    with open(input_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            components = line.split()
            if len(components) == 1 and components[0].lower() == "stop":
                spiral.penup()
            elif len(components) == 3:
                color = components[0].lower()
                x, y = int(components[1]), int(components[2])

                spiral.pencolor(color)
                spiral.goto(x, y)
                spiral.pendown()

                distance = calculate_distance(current_x, current_y, x, y)
                total_distance += distance

                current_x, current_y = x, y
            else:
                print(f"Invalid line format: {line}")
except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
    exit(1)

spiral.penup()
spiral.goto(WINDOW_SIZE / 2 - 100, -WINDOW_SIZE / 2 + 20)
spiral.write(f"Total Distance: {total_distance:.2f}", align="center", font=("Arial", 12, "normal"))

input("Drawing complete. Press Enter to exit.")
turtle.bye()
