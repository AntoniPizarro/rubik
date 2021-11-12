from pprint import pprint
from funciones import mount_cube_3x3

cube = {
    "U" : [0,0,0,0,0,0,0,0,0],
    "R" : [1,1,1,1,1,1,1,1,1],
    "F" : [2,2,2,2,2,2,2,2,2],
    "L" : [3,3,3,3,3,3,3,3,3],
    "B" : [4,4,4,4,4,4,4,4,4],
    "D" : [5,5,5,5,5,5,5,5,5]
}

class Cube:

    def __init__(self, cube):
        self.cube = cube
    
    def get_cube(self):
        return self.cube
    
    def is_solved(self):
        for key in self.cube:
            sum = 0
            for value in self.cube[key]:
                sum += value
            if sum != self.cube[key][0] * 9:
                return False
        return True

    def F(self, prima=False):
        plane = self.cube["F"]
        plane_D = self.cube["D"]
        plane_R = self.cube["R"]
        plane_L = self.cube["L"]
        plane_U = self.cube["U"]
        if prima:
            plane_F_init_1 = plane[7]
            plane_F_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_F_init_1
            plane[8] = plane[6]
            plane[6] = plane_F_init_2

            plane_D_init_1 = plane_D[0]
            plane_D_init_2 = plane_D[1]
            plane_D_init_3 = plane_D[2]
            plane_D[0] = plane_L[2]
            plane_D[1] = plane_L[5]
            plane_D[2] = plane_L[8]

            plane_L[2] = plane_U[6]
            plane_L[5] = plane_U[7]
            plane_L[8] = plane_U[8]

            plane_U[6] = plane_R[0]
            plane_U[7] = plane_R[3]
            plane_U[8] = plane_R[6]

            plane_R[0] = plane_D_init_1
            plane_R[3] = plane_D_init_2
            plane_R[6] = plane_D_init_3
        else:
            plane_F_init_1 = plane[2]
            plane_F_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_F_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_F_init_2

            plane_D_init_1 = plane_D[0]
            plane_D_init_2 = plane_D[1]
            plane_D_init_3 = plane_D[2]
            plane_D[0] = plane_R[0]
            plane_D[1] = plane_R[3]
            plane_D[2] = plane_R[6]

            plane_R[0] = plane_U[6]
            plane_R[3] = plane_U[7]
            plane_R[6] = plane_U[8]

            plane_U[6] = plane_L[2]
            plane_U[7] = plane_L[5]
            plane_U[8] = plane_L[8]

            plane_L[2] = plane_D_init_1
            plane_L[5] = plane_D_init_2
            plane_L[8] = plane_D_init_3
    
    def R(self, prima=False):
        plane = self.cube["R"]
        plane_D = self.cube["D"]
        plane_B = self.cube["B"]
        plane_F = self.cube["F"]
        plane_U = self.cube["U"]
        if prima:
            plane_R_init_1 = plane[7]
            plane_R_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_R_init_1
            plane[8] = plane[6]
            plane[6] = plane_R_init_2

            plane_D_init_1 = plane_D[2]
            plane_D_init_2 = plane_D[5]
            plane_D_init_3 = plane_D[8]
            plane_D[2] = plane_F[2]
            plane_D[5] = plane_F[5]
            plane_D[8] = plane_F[8]

            plane_F[2] = plane_U[2]
            plane_F[5] = plane_U[5]
            plane_F[8] = plane_U[8]

            plane_U[2] = plane_B[0]
            plane_U[5] = plane_B[3]
            plane_U[8] = plane_B[6]

            plane_B[0] = plane_D_init_1
            plane_B[3] = plane_D_init_2
            plane_B[6] = plane_D_init_3
        else:
            plane_R_init_1 = plane[2]
            plane_R_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_R_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_R_init_2

            plane_D_init_1 = plane_D[2]
            plane_D_init_2 = plane_D[5]
            plane_D_init_3 = plane_D[8]
            plane_D[2] = plane_B[0]
            plane_D[5] = plane_B[3]
            plane_D[8] = plane_B[6]

            plane_B[0] = plane_U[2]
            plane_B[3] = plane_U[5]
            plane_B[6] = plane_U[8]

            plane_U[2] = plane_F[2]
            plane_U[5] = plane_F[5]
            plane_U[8] = plane_F[8]

            plane_F[2] = plane_D_init_1
            plane_F[5] = plane_D_init_2
            plane_F[8] = plane_D_init_3
    
    def L(self, prima=False):
        plane = self.cube["L"]
        plane_D = self.cube["D"]
        plane_B = self.cube["B"]
        plane_F = self.cube["F"]
        plane_U = self.cube["U"]
        if prima:
            plane_L_init_1 = plane[7]
            plane_L_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_L_init_1
            plane[8] = plane[6]
            plane[6] = plane_L_init_2

            plane_D_init_1 = plane_D[0]
            plane_D_init_2 = plane_D[3]
            plane_D_init_3 = plane_D[6]
            plane_D[0] = plane_B[2]
            plane_D[3] = plane_B[5]
            plane_D[6] = plane_B[8]

            plane_B[2] = plane_U[0]
            plane_B[5] = plane_U[3]
            plane_B[8] = plane_U[6]

            plane_U[0] = plane_F[0]
            plane_U[3] = plane_F[3]
            plane_U[6] = plane_F[6]

            plane_F[0] = plane_D_init_1
            plane_F[3] = plane_D_init_2
            plane_F[6] = plane_D_init_3
        else:
            plane_L_init_1 = plane[2]
            plane_L_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_L_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_L_init_2

            plane_D_init_1 = plane_D[0]
            plane_D_init_2 = plane_D[3]
            plane_D_init_3 = plane_D[6]
            plane_D[0] = plane_F[0]
            plane_D[3] = plane_F[3]
            plane_D[6] = plane_F[6]

            plane_F[0] = plane_U[0]
            plane_F[3] = plane_U[3]
            plane_F[6] = plane_U[6]

            plane_U[0] = plane_B[2]
            plane_U[3] = plane_B[5]
            plane_U[6] = plane_B[8]

            plane_B[2] = plane_D_init_1
            plane_B[5] = plane_D_init_2
            plane_B[8] = plane_D_init_3
    
    def U(self, prima=False):
        plane = self.cube["U"]
        plane_R = self.cube["R"]
        plane_B = self.cube["B"]
        plane_F = self.cube["F"]
        plane_L = self.cube["L"]
        if prima:
            plane_U_init_1 = plane[7]
            plane_U_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_U_init_1
            plane[8] = plane[6]
            plane[6] = plane_U_init_2

            plane_F_init_1 = plane_F[0]
            plane_F_init_2 = plane_F[1]
            plane_F_init_3 = plane_F[2]
            plane_F[0] = plane_L[0]
            plane_F[1] = plane_L[1]
            plane_F[2] = plane_L[2]

            plane_L[0] = plane_B[0]
            plane_L[1] = plane_B[1]
            plane_L[2] = plane_B[2]

            plane_B[0] = plane_R[0]
            plane_B[1] = plane_R[1]
            plane_B[2] = plane_R[2]

            plane_R[0] = plane_F_init_1
            plane_R[1] = plane_F_init_2
            plane_R[2] = plane_F_init_3
        else:
            plane_U_init_1 = plane[2]
            plane_U_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_U_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_U_init_2

            plane_F_init_1 = plane_F[0]
            plane_F_init_2 = plane_F[1]
            plane_F_init_3 = plane_F[2]
            plane_F[0] = plane_R[0]
            plane_F[1] = plane_R[1]
            plane_F[2] = plane_R[2]

            plane_R[0] = plane_B[0]
            plane_R[1] = plane_B[1]
            plane_R[2] = plane_B[2]

            plane_B[0] = plane_L[0]
            plane_B[1] = plane_L[1]
            plane_B[2] = plane_L[2]

            plane_L[0] = plane_F_init_1
            plane_L[1] = plane_F_init_2
            plane_L[2] = plane_F_init_3
    
    def B(self, prima=False):
        plane = self.cube["B"]
        plane_R = self.cube["R"]
        plane_D = self.cube["D"]
        plane_U = self.cube["U"]
        plane_L = self.cube["L"]
        if prima:
            plane_B_init_1 = plane[7]
            plane_B_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_B_init_1
            plane[8] = plane[6]
            plane[6] = plane_B_init_2

            plane_D_init_1 = plane_D[6]
            plane_D_init_2 = plane_D[7]
            plane_D_init_3 = plane_D[8]
            plane_D[6] = plane_R[0]
            plane_D[7] = plane_R[1]
            plane_D[8] = plane_R[2]

            plane_R[2] = plane_U[0]
            plane_R[5] = plane_U[1]
            plane_R[8] = plane_U[2]

            plane_U[0] = plane_L[0]
            plane_U[1] = plane_L[3]
            plane_U[2] = plane_L[6]

            plane_L[0] = plane_D_init_1
            plane_L[3] = plane_D_init_2
            plane_L[6] = plane_D_init_3
        else:
            plane_B_init_1 = plane[2]
            plane_B_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_B_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_B_init_2

            plane_D_init_1 = plane_D[6]
            plane_D_init_2 = plane_D[7]
            plane_D_init_3 = plane_D[8]
            plane_D[6] = plane_L[0]
            plane_D[7] = plane_L[3]
            plane_D[8] = plane_L[6]

            plane_L[0] = plane_U[0]
            plane_L[3] = plane_U[1]
            plane_L[6] = plane_U[2]

            plane_U[0] = plane_R[0]
            plane_U[1] = plane_R[1]
            plane_U[2] = plane_R[2]

            plane_R[2] = plane_D_init_1
            plane_R[5] = plane_D_init_2
            plane_R[8] = plane_D_init_3
    
    def D(self, prima=False):
        plane = self.cube["D"]
        plane_R = self.cube["R"]
        plane_F = self.cube["F"]
        plane_B = self.cube["B"]
        plane_L = self.cube["L"]
        if prima:
            plane_D_init_1 = plane[7]
            plane_D_init_2 = plane[0]
            plane[0] = plane[2]
            plane[7] = plane[3]
            plane[3] = plane[1]
            plane[1] = plane[5]
            plane[2] = plane[8]
            plane[5] = plane_D_init_1
            plane[8] = plane[6]
            plane[6] = plane_D_init_2

            plane_B_init_1 = plane_B[6]
            plane_B_init_2 = plane_B[7]
            plane_B_init_3 = plane_B[8]
            plane_B[6] = plane_L[6]
            plane_B[7] = plane_L[7]
            plane_B[8] = plane_L[8]

            plane_L[6] = plane_F[6]
            plane_L[7] = plane_F[7]
            plane_L[8] = plane_F[8]

            plane_F[6] = plane_R[6]
            plane_F[7] = plane_R[7]
            plane_F[8] = plane_R[8]

            plane_R[6] = plane_B_init_1
            plane_R[7] = plane_B_init_2
            plane_R[8] = plane_B_init_3
        else:
            plane_D_init_1 = plane[2]
            plane_D_init_2 = plane[1]
            plane[2] = plane[0]
            plane[0] = plane[6]
            plane[6] = plane[8]
            plane[8] = plane_D_init_1
            plane[1] = plane[3]
            plane[3] = plane[7]
            plane[7] = plane[5]
            plane[5] = plane_D_init_2

            plane_B_init_1 = plane_B[6]
            plane_B_init_2 = plane_B[7]
            plane_B_init_3 = plane_B[8]
            plane_B[6] = plane_R[6]
            plane_B[7] = plane_R[7]
            plane_B[8] = plane_R[8]

            plane_R[6] = plane_F[6]
            plane_R[7] = plane_F[7]
            plane_R[8] = plane_F[8]

            plane_F[6] = plane_L[6]
            plane_F[7] = plane_L[7]
            plane_F[8] = plane_L[8]

            plane_L[6] = plane_B_init_1
            plane_L[7] = plane_B_init_2
            plane_L[8] = plane_B_init_3

c1 = {
    "U" : [],
    "D" : [],
    "R" : [],
    "B" : [],
    "L" : [],
    "F" : []
}

for i in range(9):
    c1["U"].append(0)
    c1["D"].append(1)
    c1["R"].append(2)
    c1["B"].append(3)
    c1["L"].append(4)
    c1["F"].append(5)

cube1 = Cube(c1)
print(mount_cube_3x3(cube1.get_cube()))
print("Solved: " + str(cube1.is_solved()))
print("=" * 29)
cube1.R()
movments = ["R", "L'", "B", "F'", "D", "U'", "R", "L'"]
'''for mov in movments:
    if mov.upper() == "R":
        cube1.R()
    elif mov.upper() == "R'":
        cube1.R(True)
    elif mov.upper() == "F":
        cube1.F()
    elif mov.upper() == "F'":
        cube1.F(True)
    elif mov.upper() == "D":
        cube1.D()
    elif mov.upper() == "D'":
        cube1.D(True)
    elif mov.upper() == "B":
        cube1.B()
    elif mov.upper() == "B'":
        cube1.B(True)
    elif mov.upper() == "L":
        cube1.L()
    elif mov.upper() == "L'":
        cube1.L(True)
    elif mov.upper() == "U":
        cube1.U()
    elif mov.upper() == "U'":
        cube1.U(True)'''

print(mount_cube_3x3(cube1.get_cube()))
print("Solved: " + str(cube1.is_solved()))