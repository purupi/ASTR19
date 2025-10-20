import math

def main():
	print("x\t\tsin(x)")
	print("~"*25)

	n = 1000
	start = 0
	end = 2*math.pi
	step = (end-start)/(n-1)

	for i in range(n):
		x = start+i*step
		y = math.sin(x)
		print(f"{x:.6f}\t\t{y:.6f}")

main()