from math import pi

#------------------volume of cube------------------- 
# cone,  cylinder,sphere

cube_value =int(input("enter the value  of cube : "))
print(f"volume of {cube_value} is {cube_value**3}\n\n")

#------------------volume of cylinder------------------- 

cylinder_radius =int(input("enter the value  of cylinder radius : "))
cylinder_height =int(input("enter the value  of cylinder height : "))
print(f"volume of cylinder is {pi*(cylinder_radius**2)*cylinder_height}\n\n")

#------------------volume of cone------------------- 

cone_radius =int(input("enter the value  of cone radius : "))
cone_height =int(input("enter the value  of cone height : "))
print(f"volume of cone is {(1/3*pi)*(cone_radius**2)*cone_height}\n\n")

# ------------------volume of sphere------------------- 

sphere_radius =int(input("enter the value of sphere radius : "))
print(f"volume of sphere is {(4/3*pi)*(sphere_radius**3)}\n\n")
