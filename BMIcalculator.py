# 1st input: enter height in meters 
height = input("Please input your height in meters\n")
# 2nd input: enter weight in kilograms 
weight = input("Please input your weight in kg\n")
# print(type(height))
height1 = float(height)
weight1 = int(weight)
# print(type(height1))

BMI = int(weight1 / (height1 **2))
BMI2 = str(BMI)
# print (BMI2)
print ("your BMI is" + " " + BMI2)
# BMI = weight (height)