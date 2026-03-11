# graphing_module.py
import turtle
import os
import math
# from PIL import Image, ImageFilter


def graph_data(altitude, unknown, unknown_name="Unknown"):
    """
    Creates a Turtle graph for the unknown values against altitude,
    saves as PNG file with high resolution.

    Parameters:
        altitude (list of numbers): Altitude values
        unknown (list of numbers): Values to plot
        unknown_name (str): Name to use for axis title and file name
    """
    if len(altitude) != len(unknown):
        raise ValueError("Altitude and unknown lists must have the same length")

    # Graph settings
    GRAPH_MIN, GRAPH_MAX = -250, 250
    GRAPH_SIZE = GRAPH_MAX - GRAPH_MIN
    PADDING = 0.05
    GUIDELINE_COLOR = "#000000"
    GRAPH_COLOR = "#0000FF"

    alt_min, alt_max = min(altitude), max(altitude)
    unk_min, unk_max = min(unknown), max(unknown)

    # Add padding
    alt_pad = (alt_max - alt_min) * PADDING or 1
    unk_pad = (unk_max - unk_min) * PADDING or 1
    alt_min -= alt_pad
    alt_max += alt_pad
    unk_min -= unk_pad
    unk_max += unk_pad

    alt_range = alt_max - alt_min
    unk_range = unk_max - unk_min
    alt_scale = GRAPH_SIZE / alt_range
    unk_scale = GRAPH_SIZE / unk_range

    # Helper to scale data to screen
    def data_to_screen(x, y):
        x = GRAPH_MIN + (x - alt_min) * alt_scale
        y = GRAPH_MIN + (y - unk_min) * unk_scale
        return round(x, 1), round(y, 1)

    # Helper to compute nice tick intervals
    def nice_interval(value_range, ticks=8):
        raw = value_range / ticks
        if raw <= 0:
            raise ValueError("Cannot compute interval with zero range")
        mag = 10 ** math.floor(math.log10(raw))
        norm = raw / mag
        if norm < 1.5:
            return 1 * mag
        elif norm < 3:
            return 2 * mag
        elif norm < 7:
            return 5 * mag
        else:
            return 10 * mag

    alt_tick = nice_interval(alt_range)
    unk_tick = nice_interval(unk_range)

    # Setup turtle
    turtle.setup(width=1080, height=1080)
    screen = turtle.Screen()
    t1 = turtle.Turtle()
    t1.speed(0)
    t1.hideturtle()
    t1.penup()

    # Draw axes
    t1.pencolor(GUIDELINE_COLOR)
    t1.goto(GRAPH_MIN, GRAPH_MIN)
    t1.pendown()
    t1.goto(GRAPH_MAX, GRAPH_MIN)
    t1.penup()
    t1.goto(GRAPH_MIN, GRAPH_MIN)
    t1.pendown()
    t1.goto(GRAPH_MIN, GRAPH_MAX)

    # X ticks
    val = math.ceil(alt_min / alt_tick) * alt_tick
    while val <= alt_max:
        x, _ = data_to_screen(val, unk_min)
        t1.penup()
        t1.goto(x, GRAPH_MIN)
        t1.pendown()
        t1.goto(x, GRAPH_MIN - 7)
        t1.penup()
        t1.goto(x, GRAPH_MIN - 20)
        t1.write(int(val), align="center")
        val += alt_tick

    # Y ticks
    val = math.ceil(unk_min / unk_tick) * unk_tick
    while val <= unk_max:
        _, y = data_to_screen(alt_min, val)
        t1.penup()
        t1.goto(GRAPH_MIN, y)
        t1.pendown()
        t1.goto(GRAPH_MIN - 7, y)
        t1.penup()
        t1.goto(GRAPH_MIN - 12, y - 5)
        t1.write(int(val), align="right")
        val += unk_tick

    # Axis labels
    t1.penup()
    t1.goto(0, GRAPH_MIN - 45)
    t1.write("Altitude (m)", align="center", font=("Arial", 10, "normal"))
    t1.goto(GRAPH_MIN - 90, 0)
    t1.setheading(90)
    t1.write(f"{unknown_name}", align="center", font=("Arial", 10, "normal"))
    t1.setheading(0)

    # Plot data
    t1.pencolor(GRAPH_COLOR)
    t1.penup()
    for i, (alt_point, val) in enumerate(zip(altitude, unknown)):
        x, y = data_to_screen(alt_point, val)
        if i == 0:
            t1.goto(x, y)
            t1.pendown()
        else:
            t1.goto(x, y)
        t1.dot(5)

    # Title
    t1.penup()
    t1.goto(0, GRAPH_MAX + 25)
    t1.write(f"{unknown_name} vs Altitude", align="center", font=("Arial", 14, "bold"))
    # Save as high-res PNG
    screen = t1.getscreen()
    canvas = screen.getcanvas()

    turtle.done()