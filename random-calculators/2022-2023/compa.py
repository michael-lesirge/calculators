# Check if 2 lines are parrels or perpendicular

from helper import sint, gcd, get_point

def slp(x1, y1, x2, y2):
    print("(%s - %s) / (%s - %s)" % (y2, y1, x2, x1))
    t, b = sint(y2 - y1), sint(x2 - x1)
    print("(%s) / (%s)" % (t, b))
    try:
        s = sint(t / b)
    except ZeroDivisionError:
        s = "undifined"

    if t < 0 and b < 0:
        t, b = abs(t), abs(b)
    
    print("%s / %s" % (t, b))

    try:
        if isinstance(t, int) and isinstance(b, int):
            d = sint(gcd(abs(t), abs(b)))
            if d != 1:
                print("%s / %s gcd: %s" % (sint(t / d), sint(b / d), d))
    except ZeroDivisionError:
        pass

    print(s)

    return s

while True:
    x1, y1 = get_point("1")
    x2, y2 = get_point("2")

    s1 = slp(x1, y1, x2, y2)

    x1, y1 = get_point("1")
    x2, y2 = get_point("2")

    s2 = slp(x1, y1, x2, y2)
    
    input()

    if s1 == s2:
        print("%s = %s" % (s1, s2))
        print("lines are parrels")
    elif s1 * s2 == -1:
        print("%s * %s = -1" % (s1, s2))
        print("lines are perpendicular")
    else:
        print("%s, %s" % (s1, s2))
        print("neither")
    print()