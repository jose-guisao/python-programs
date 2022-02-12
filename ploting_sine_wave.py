##import matplotlib.pyplot as plt
##import numpy as np
##
##x = np.arange(0,2*(np.pi),0.1)
##y = np.sin(x)
##plt.plot(x,y)
##plt.show()


### importing required modules
##from mpl_toolkits.mplot3d import axes3d
##import matplotlib.pyplot as plt
##from matplotlib import style
##import numpy as np
##
### setting a custom style to use
##style.use('ggplot')
##
### create a new figure for plotting
##fig = plt.figure()
##
### create a new subplot on our figure
##ax1 = fig.add_subplot(111, projection='3d')
##
### get points for a mesh grid
##u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
##
### setting x, y, z co-ordinates
##x=np.cos(u)*np.sin(v)
##y=np.sin(u)*np.sin(v)
##z=np.cos(v)
##
### plotting the curve
##ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1)
##
##plt.show()


import numpy as np
import matplotlib.pyplot as plt
import math
x = np.arange(100)
##y1 = np.random.randint(10, size=100)
y1 = np.tan(np.arange(100))
##y2 = np.random.randint(10, size=100)*100
y2 = np.sin(np.arange(100))
fig, ax = plt.subplots()
ax.plot(x, y1, label='first')
ax2 = ax.twinx()
ax2._get_lines.get_next_color()
# ax2.plot([], [])
ax2.plot(x,y2, label='second')

handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax.legend(handles1+handles2, labels1+labels2, loc='best')  

plt.show()
