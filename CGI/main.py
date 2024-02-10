import matplotlib.pyplot as plt


def visual_show(all_points, point1, point2):
    # Extract x and y coordinates from list
    x_coord = [coord[0] for coord in all_points]
    y_coord = [coord[1] for coord in all_points]
    plt.plot(x_coord, y_coord, marker='o', color='green')
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")
    plt.title(f"Line Between  {point1}  &  {point2}")
    plt.grid(True)
    x = [point1[0], point2[0]]
    y = [point1[1], point2[1]]
    plt.plot(x, y, marker='o', color='blue')
    plt.show()


def bresenham_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dy = y2 - y1
    dx = x2 - x1
    if dy < dx:
        slope_less_than_one(point1, point2)
    else:
        slope_greater_than_or_equal_one(point1, point2)


def slope_less_than_one(point1, point2):
    all_points = []
    x1, y1 = point1
    x2, y2 = point2
    x, y = x1, y1
    dy = y2 - y1
    dx = x2 - x1
    p = 2 * dy - dx

    while x <= x2:
        all_points.append((x, y))
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
    visual_show(all_points, point1, point2)


def slope_greater_than_or_equal_one(point1, point2):
    all_points = []
    x1, y1 = point1
    x2, y2 = point2
    x, y = x1, y1
    dy = y2 - y1
    dx = x2 - x1
    p = 2 * dx - dy

    while y <= y2:
        all_points.append((x, y))
        y += 1
        if p < 0:
            p = p + 2 * dx
        else:
            p = p + 2 * dx - 2 * dy
            x += 1
    visual_show(all_points, point1, point2)


def main():
    print('\nBresenham Line Drawing Algorithm')

    point1 = [1, 1]
    point2 = [8, 4]
    bresenham_line(point1, point2)

    point1 = [1, 1]
    point2 = [4, 8]
    bresenham_line(point1, point2)


if __name__ == "__main__":
    main()
