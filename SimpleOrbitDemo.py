import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle

#The following program is an n-body simulation which simulates the orbits of planets by plotting their positions
# on a scatterplot


# Initializes instances of a Particle. These particles have fields pertaining to their mass, x-position, y-position,
# x-velocity, and y-velocity. 
HR_8799 = Particle(1.9885e30*1.47, 0, 0, 0, 0)
HR_8799_e = Particle(1.8982e27*7.4, 2.43097e+12, 0, 0, 8957.6116)
HR_8799_d = Particle(1.8982e27*9.1, 3.98978e+12, 0, 0 , 6992.0987)
HR_8799_c = Particle(1.8982e27*7.8, 6.19186e+12, 0, 0, 5612.695)
HR_8799_b = Particle(1.8982e27*5.7, 1.0711e+13, 0, 0, 4267.436)


# # nsteps represents the number of points plotted for each planet in the simulation
# trun = 9.145e8*2
# tstep = trun/(1e6)
# # #tstep is the time step between points on the scatterplot. Essentially, between each point on the plot, the number
# # of seconds that have elapsed is equal to the numerical value of tstep
# nsteps = int(trun/tstep)
# 
# # The following arrays contain the x position and y position of each object at each time step. These arrays
# # store the positional data required to plot the orbits of the objects.
# Planet1XPos = np.full(nsteps, np.nan)
# Planet1YPos = np.full(nsteps, np.nan)
# 
# Planet2XPos = np.full(nsteps, np.nan)
# Planet2YPos = np.full(nsteps, np.nan)
# 
# StarXPos = np.full(nsteps, np.nan)
# StarYPos = np.full(nsteps, np.nan)
# 
# # The following for-loop is the simulation process itself. The objects involved first exert forces on one another
# # and then update their velocities and positions based on those forces and their masses. Then, the positions are recorded
# # in the arrays for each object to be plotted.
# 
# bodies = (Planet1, Star)
# XPosArr = (Planet1XPos, StarXPos)
# YPosArr = (Planet1YPos, StarYPos)
# 
# 
# for steps in range(nsteps):
#     for i in range(len(bodies)):
#         for j in range(len(bodies)):
#             if i!=j:
#                 bodies[i].getForce(bodies[j])
#                 bodies[j].getForce(bodies[i])
#         bodies[i].update(tstep)
#     for l in range(len(bodies)):
#         bodies[l].resetForce()
#         XPosArr[l][steps] = bodies[l].x
#         YPosArr[l][steps] = bodies[l].y
# 
# plt.ion()
# plt.plot(Planet1XPos, Planet1YPos, "o", label='planet 1', color = "blue")
# plt.plot(Planet2XPos, Planet2YPos, label='planet 2', color = "black")
# plt.plot(StarXPos, StarYPos, "-o",label='star', color = "green")
# 
# 
# 
# # Tasks:
# # 1)Simulate 4-body system
# # 2)Simulate HR-8799 exoplanetary system
# # 3)Learn Github
