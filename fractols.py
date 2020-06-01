import turtle

def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)

def draw_koch(l, n):
    if n == 0:
        turtle.forward(l)
        return
    else:
        x = l / 3
        draw_koch(x, n - 1)
        turtle.left(60)
        draw_koch(x, n - 1)
        turtle.right(120)
        draw_koch(x, n - 1)
        turtle.left(60)
        draw_koch(x, n - 1)

def draw_mincovskii(l, n) :
    if n == 0:
        turtle.forward(l)
        return

    draw_mincovskii(l, n - 1)
    turtle.left(90)
    for i in range(2):
        draw_mincovskii(l, n - 1)
        turtle.right(90)
    for i in range(2):
        draw_mincovskii(l, n - 1)
    for i in range(2):
        turtle.left(90)
        draw_mincovskii(l, n - 1)
    turtle.right(90)
    draw_mincovskii(l, n - 1)

def draw_kantor(l, n, x, y):
    if (n == -1):
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)
    draw_kantor(l / 3, n - 1, x, y - 25)
    draw_kantor(l / 3, n - 1, x + 2*l / 3, y - 25)

if __name__ == "__main__":
    turtle.color('purple')
    turtle.width(3)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.speed('fastest')
    draw_kantor(600, 5, -300, 0)