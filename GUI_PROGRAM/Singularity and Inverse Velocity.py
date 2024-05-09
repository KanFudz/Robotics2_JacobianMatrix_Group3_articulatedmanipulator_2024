## Articulated

# import libraries
import numpy as np
import sympy as sp

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

#joint variables: mm if d and degrees if theta
T1 = float(input("T1 = "))
T2 = float(input("T2 = "))
T3 = float(input("T3 = "))

#Convert Rotation angles
#deg to radian
T1 = (T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi
T3 = (T3/180.0)*np.pi

#Parametric Table: (Theta, alpha, r, d)
PT = [[T1,(90.0/180.0)*np.pi,0,a1],
      [T2,(0.0/180.0)*np.pi,a2,0],
      [T3,(0.0/180.0)*np.pi,a3,0]]

#Homogeneous Transformation Matrix Formula
i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

H0_1 = np.matrix(H0_1)
#print("H0_1 = ")
#print(H0_1)

H1_2 = np.matrix(H1_2)
#print("H1_2 = ")
#print(H1_2)

H2_3 = np.matrix(H2_3)
#print("H2_3 = ")
#print(H2_3)

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)
#print("H0_3 = ")
#print(np.matrix(H0_3))
H0_3 = np.matrix(H0_3)

## Jacobian Matrix

#Linear / Translation Vectors
Z_1 = [ [0],
       [0],
       [1]] # [0,0,1] vector

#Row 1 to 3, Column 1
J1a = [[1,0,0],
      [0,1,0],
      [0,0,1]]
J1a = np.dot(J1a,Z_1)

J1b_1 = H0_3[0:3,3:] #d0_3
J1b_1 = np.array(J1b_1)

J1b_2 = H0_1[0:3,3:] #d0_1
J1b_2 = np.array(J1b_2)

J1b= J1b_1 - J1b_2

J1 = [[J1a[1,0]*J1b[2,0] - J1a[2,0]*J1b[1,0]],
      [J1a[2,0]*J1b[0,0] - J1a[0,0]*J1b[2,0]],
      [J1a[0,0]*J1b[1,0] - J1a[1,0]*J1b[0,0]]]

J1 = np.matrix(J1)


#Row 1 to 3, Column 2
J2a = H0_1[0:3,0:3] #R0_1
J2a = np.dot(J2a,Z_1)

J2b_1 = H0_3[0:3,3:] #d0_3
J2b_1 = np.array(J2b_1)

J2b_2 = H0_1[0:3,3:] #d0_1
J2b_2 = np.array(J2b_2)

J2b= J2b_1 - J2b_2

J2 = [[J2a[1,0]*J2b[2,0] - J2a[2,0]*J2b[1,0]],
      [J2a[2,0]*J2b[0,0] - J2a[0,0]*J2b[2,0]],
      [J2a[0,0]*J2b[1,0] - J2a[1,0]*J2b[0,0]]]

J2 = np.matrix(J2)


#Row 1 to 3, Column 3
J3a = H0_2[0:3,0:3] #R0_2
J3a = np.dot(J3a,Z_1)

J3b_1 = H0_3[0:3,3:] #d0_3
J3b_1 = np.array(J3b_1)

J3b_2 = H0_2[0:3,3:] #d0_2
J3b_2 = np.array(J3b_2)

J3b= J3b_1 - J3b_2

J3 = [[J3a[1,0]*J3b[2,0] - J3a[2,0]*J3b[1,0]],
      [J3a[2,0]*J3b[0,0] - J3a[0,0]*J3b[2,0]],
      [J3a[0,0]*J3b[1,0] - J3a[1,0]*J3b[0,0]]]

J3 = np.matrix(J3)

#2. Rotation / Orientation Vectors
#Row 4 to 6, Column 1
J4 = [[0],[0],[1]]
J4 = np.matrix(J4)

#Row 4 to 6, Column 2
J5 = J2a
J5 = np.matrix(J5)

#Row 4 to 6, Column 3
J6 = J3a
J6 = np.matrix(J6)

#3. Concatenated Jacobian Matrix
JM1 = np.concatenate((J1,J2,J3),1)
JM2 = np.concatenate((J4,J5,J6),1)

J = np.concatenate((JM1,JM2),0)
print("J = ")
print(np.around(J,3))


#4. Differential Equations
T1_p, T2_p, T3_p = sp.symbols('θ1* θ2* θ3*')

q = [[T1_p],
     [T2_p],
     [T3_p]]

E = np.dot(J,q)
E = np.matrix(E)

xp = E[0,0]
yp = E[1,0]
zp = E[2,0]
ωx = E[3,0]
ωy = E[4,0]
ωz = E[5,0]

print("xp = ",xp)
print("yp = ",yp)
print("zp = ",zp)
print("ωx = ",ωx)
print("ωy = ",ωy)
print("ωz = ",ωz)

## Singularity
D_J = np.linalg.det(JM1)
print("D_J = ",D_J)

## Inverse Velocity
I_V = np.linalg.inv(JM1)
print("I_v = ",I_V)
