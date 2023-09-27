
def main():

   # collecting user input
   import math
   angle = float(input("Enter the angle: "))
   distance = float(input("Enter the distance: "))
   height = float(input("Enter the height: "))

   # processing
   buildingHeight = (math.tan(angle * (math.pi / 180)) * distance) + height

   # output
   print (f"The height of the building is {buildingHeight:0.0f}")

if __name__ == '__main__':
   main()


