import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8,10,15])
y=np.array([3,8,1,10,6,1])
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,'o--r')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y, marker='o',ms=20)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y, marker='o',ms=20,mec='r')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,8,1,10])

plt.plot(y, marker='o',ms=20, mfc='r')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,8,12,20,26,38])

plt.scatter(x,y)
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,0,5,5])
y=np.array([0,35,35,0])

plt.scatter(x,y)
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,0,5,5])
y=np.array([0,35,35,0])
mycolor=['red','green','yellow','lime']

plt.scatter(x,y,color=mycolor)
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,0,5,5])
y=np.array([0,35,35,0])
mycolor=['red','green','yellow','lime']
size=[10,60,120,80]

plt.scatter(x,y,color=mycolor,s=size)
plt.show()