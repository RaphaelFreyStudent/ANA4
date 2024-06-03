import numpy as np
import matplotlib.pyplot as plt

f = lambda z: np.exp(np.conj(z)*z)

dxf = lambda z,h: (f(z+h)-f(z))/h
dyf = lambda z,h: (f(z+1j*h)-f(z))/h

dcomplex = lambda dfx,dfy: 0.5*(dfx-1j*dfy)
wirtinger = lambda dxf,dyf: 0.5*(dxf+1j*dyf)

# Create a range of values
z = 2+1j

# acceptable tangent h
h = 1e-10

# Create a figure with 2 subplots
fig, ax = plt.subplots(1,3, figsize=(15,5))
plt.subplots_adjust(wspace=0.5)
ax[0].scatter(z.real, z.imag, facecolors="none", edgecolors='r')
ax[0].axis('equal')
ax[0].grid(True)
ax[0].set_title('z = '+str(z))
ax[0].set_xlabel('Re')
ax[0].set_ylabel('Im')

ax[1].scatter(f(z).real, f(z).imag, facecolors="none", edgecolors='r')
ax[1].axis('equal')
ax[1].grid(True)
ax[1].set_title('f(z)')
ax[1].set_xlabel('Re')
ax[1].set_ylabel('Im')

ax[2].scatter(dxf(z,h).real, dxf(z,h).imag,facecolors="none", edgecolors='b', label=f'dxf = {np.round(dxf(z,h),1)}')
ax[2].scatter(dyf(z,h).real, dyf(z,h).imag,facecolors="none", edgecolors='g', label=f'dyf = {np.round(dyf(z,h),1)}')
ax[2].scatter(dcomplex(dxf(z,h),dyf(z,h)).real, dcomplex(dxf(z,h),dyf(z,h)).imag,facecolors="none", edgecolors='y', label= f"dfdz = {np.round(dcomplex(dxf(z,h),dyf(z,h)),1)}")
ax[2].scatter(wirtinger(dxf(z,h),dyf(z,h)).real, wirtinger(dxf(z,h),dyf(z,h)).imag,facecolors="none", edgecolors='k', label= f"wirtinger = {np.round(wirtinger(dxf(z,h),dyf(z,h)),1)}")

ax[2].axis('equal')
ax[2].grid(True)
ax[2].set_title('df(z)')
ax[2].set_xlabel('Re')
ax[2].set_ylabel('Im')
ax[2].legend()





# Show the plots
plt.show()