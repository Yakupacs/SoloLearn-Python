weight = int(input())
height = float(input())
BMI = weight / (height * 2)

if (BMI < 18.5):
	print("Underweight")
elif (BMI < 25):
	print("Normal")
elif (BMI < 30):
	print("Overweight")
else:
	print("Obesity")