
import sys
import functools
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

trees = []
with open(sys.argv[1]) as f:
  for line in f:
    trees.append([int(x) for x in list(line.strip())])

trees = np.array(trees)
nx, ny = trees.shape

def distance_to_edge(i, j):
  if i == 0 or i == nx-1 or j == 0 or j == ny-1:
    return 0
  dists = []
  if all([trees[k][j] < trees[i][j] for k in range(0, i)]):
    dists.append(i)
  else:
    dists.append(-1)
  if all([trees[k][j] < trees[i][j] for k in  range(i+1, nx)]):
    dists.append(nx-i+1)
  else:
    dists.append(-1)
  if all([trees[i][k] < trees[i][j] for k in range(0, j)]):
    dists.append(j)
  else:
    dists.append(-1)
  if all([trees[i][k] < trees[i][j] for k in range(j+1, ny)]):
    dists.append(ny-j+1)
  else:
    dists.append(-1)
  if all([d == -1 for d in dists]):
    return -1
  else:
    return max([d for d in dists if d != -1])

distance = np.zeros_like(trees)
for i in range(nx):
  for j in range(ny):
    distance[i,j] = distance_to_edge(i, j)

plt.figure(figsize=(8,8))

if False:
  plt.title("Tree heights")
  heights = np.arange(1, 10)
  cmap0 = matplotlib.cm.get_cmap('viridis')
  cmap = mcolors.ListedColormap([cmap0(x) for x in np.arange(9)/8])
  im = plt.imshow(trees, cmap=cmap)
  ax = plt.gca()
  ax.axis("off")
  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="3%", pad=0.05)
  cb = plt.colorbar(im, cax=cax)
  cb.ax.set_yticks(np.arange(9)+0.5, heights)
  plt.tight_layout()
  # plt.savefig("heights.png")

if True:
  plt.title("Max visible distance from any edge")
  cmap = matplotlib.cm.get_cmap('inferno').copy()
  cmap.set_bad("black")
  # distance[distance == -1] = None
  im = plt.imshow(distance, cmap=cmap)
  ax = plt.gca()
  ax.axis("off")
  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="3%", pad=0.05)
  cb = plt.colorbar(im, cax=cax)
  plt.tight_layout()
  plt.savefig("distance.png")

plt.show()