# get what type of shape a Quadrilateral is from line lengths and slopes

from helper import get_sint

def sq(x):
    return (x)**2

def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5

al, bl, cl, dl = list((input("letters: ") or "abcd").upper())

ab_slp = get_sint("%s slp" % (al+bl))
bc_slp = get_sint("%s slp" % (bl+cl))
cd_slp = get_sint("%s slp" % (cl+dl))
da_slp = get_sint("%s slp" % (dl+al))
ab_dis = get_sint("%s dis" % (al+bl))
bc_dis = get_sint("%s dis" % (bl+cl))
cd_dis = get_sint("%s dis" % (cl+dl))
da_dis = get_sint("%s dis" % (dl+al))

# Rect Shape:
#  a - b
#  |   |
#  d - c

# Parallelogram: Opposite Sides are Congruent; Slopes of opposite sides do not make perpendicular lines
# Rhombus: All sides are Congruent; Slopes of opposite sides are congruent; they do not make perpendicular lines
# Rectangle: Opposite sides are Congruent; Slopes of opposite sides make perpendicular lines
# Square: All sides are Congruent; Slopes of opposite sides make perpendicular lines

is_para = False
is_rhom = False
is_rect = False
if ab_dis == cd_dis and da_dis == bc_dis:
    is_para = True
    if ab_dis == da_dis == cd_dis == bc_dis:
        is_rhom = True
    if (ab_slp * da_slp == -1 or (ab_slp == 0 and da_slp == float("NaN")) or (ab_slp == float("NaN") and da_slp == 0)) and (bc_slp * cd_slp == -1 or (bc_slp == 0 and cd_slp == float("NaN")) or (bc_slp == float("NaN") and cd_slp == 0)):
        is_rect = True

if is_rhom and is_rect:
    print("Square")
elif is_rhom:
    print("Rhombus")
elif is_rect:
    print("Rectangle")
elif is_para:
    print("Parallelogram")
else:
    print("Quadrilateral")