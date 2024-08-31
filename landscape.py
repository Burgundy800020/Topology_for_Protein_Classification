import numpy as np
import matplotlib.pyplot as plt
from gudhi.representations import Landscape
import gudhi as gd

#A single diagram with 4 points
D = np.array([[0, 10], [2, 8], [3, 10],[7, 10]])

diags = [D]
l=Landscape(num_landscapes=2,resolution=20).fit_transform(diags)

X = np.linspace(np.min(D), np.max(D), 20)
plt.plot(X, l[0][0:20], color="blue")
plt.plot(X, l[0][20:], color="yellow")
plt.title("Persistence Landscape")
plt.xlabel("Time")
plt.ylabel("Landscape value")
plt.show()