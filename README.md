# intersection-between-two-lines
simple algorithm to find if there is an intersection between two lines or not

linear equation: y = m.x + b, m = slope, b is level of y when x is 0, then b = y - m.x

algorithm steps:
1 - find m.
2 - find b.
3 - choose the line Which have the greater slope, if the two lines are decreasing choose the one who decreasing fast.
4 - sure that x1 of great line in domain of the other line.
5 - if the equation of greater line satisfy:
    f1(x2) > f2(x2), then there is an intersection
    f1 = greater line functon
    f2 = slower line function 
    
