class Line:
	def __init__(self, p1, p2):
		self.x1 = p1[0]
		self.y1 = p1[1]
		self.x2 = p2[0]
		self.y2 = p2[1]

		# linear equation: y = m.x + b, m = slope, b is level of y when x is 0, then b = y - m.x
		self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
		self.b = self.y1 - (self.m * self.x1)

	def equation(self, x):
		return (self.m * x) + self.b
	def is_increasing(self):
		return self.m > 0

def find_intersection(line1, line2):
	if line1.m > 0 and line2.m > 0:
		increasing_faster, increasing_slower = (line1, line2) if line1.m > line2.m else (line2, line1)

		if increasing_faster.y1 < increasing_slower.y2 and increasing_faster.x1 >= increasing_slower.x1:
			if increasing_faster.equation(increasing_slower.x2) > increasing_slower.y2:
				print('There is intersection')
			else:
				print('There is no intersection')
		else:
			print('There is no intersection')

	elif line1.m > 0 or line2.m > 0:
		increasing_faster, increasing_slower = (line1, line2) if line1.m > line2.m else (line2, line1)

		if increasing_faster.y1 < increasing_slower.y1 and increasing_faster.x1 < increasing_slower.x2:
			if increasing_faster.equation(increasing_slower.x2) > increasing_slower.y2:
				print('There is intersection')
			else:
				print('There is no intersection')
		else:
			print('There is no intersection')

	elif line1.m < 0 and line2.m < 0:
		decreasing_faster, decreasing_slower = (line1, line2) if line1.m < line2.m else (line2, line1)

		if decreasing_faster.y1 > decreasing_slower.y2 and decreasing_faster.x1 < decreasing_slower.x2:
			if decreasing_faster.equation(decreasing_slower.x2) < decreasing_slower.y2:
				print('There is intersection')
			else:
				print('There is no intersection')
		else:
			print('There is no intersection')
