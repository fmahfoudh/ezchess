import matplotlib.pyplot as plt
import numpy as np
import pandas

from matplotlib.table import Table


# Make a 9x9 grid...
nrows, ncols = 8,8
image = np.zeros(nrows*ncols)

# Set every other cell to a random number (this would be your data)
image[::2] = np.random.random(nrows*ncols //2 )

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

row_labels = [8,7,6,5,4,3,2,1]
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()