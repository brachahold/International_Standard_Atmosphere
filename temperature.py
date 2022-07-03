def get_slope(x1, y1, x2, y2):
    return 0 if x1 == x2 else (y1 - y2) / (x1 - x2)


def get_point_on_line(x1, y1, y2, slope):
    return x1 if not slope else x1 - ((y1 - y2) / slope)


heights = [0, 11000, 20000, 32000]
temp = [15.0, -56.5, -56.5, -44.5]
slopes = [get_slope(temp[i], heights[i], temp[i + 1], heights[i + 1]) for i in range(len(heights) - 1)]


def get_temperature(m):
    i = 0
    while i < len(heights) - 1 and m > heights[i + 1]:
        i += 1
    return get_point_on_line(temp[i], heights[i], m, slopes[i])




