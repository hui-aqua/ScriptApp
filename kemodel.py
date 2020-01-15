import sys
import numpy as np

U = float(sys.argv[1]); # inlet velocity
print("incoming velocity is "+str(U))

td=float(sys.argv[2])  #mm  twine diameter
print("Twine diameter is "+str(td))
# Constant in the model
C_u = 0.09;
# Calculation

Re = U*td*10**6;
print("Reynold number is  "+ str(Re));
I = 0.16*Re**(-0.125); # turbulence intensity. for fully developed pipe flow

k = 1.5*(U*I)**2;  # for isotropic turbulence the turbulent kinetic energy

epsilon = C_u**0.75*k**1.5/td;

omega = np.sqrt(k)/td/C_u;

print("k is "+str(k));
print("epsilon is "+str(epsilon));
print("omega is "+str(omega))
