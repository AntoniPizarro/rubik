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