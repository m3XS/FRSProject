import seaborn as sns
import os, numpy

from matplotlib import pyplot as plt

local_path = os.getcwd()
impostor_distance_file = os.path.join(local_path, 'impostor_distance.txt')
genuine_distance_file = os.path.join(local_path, 'genuine_distance.txt')

with open(impostor_distance_file, 'r') as f:
    impostor_distance = numpy.asarray(f.read().splitlines(), dtype=float)

with open(genuine_distance_file, 'r') as f:
    genuine_distance = numpy.asarray(f.read().splitlines(), dtype=float)

model = "FaceNet"
sns.distplot(genuine_distance, hist=False, kde=True,
             kde_kws={'shade': False, 'linewidth': 2},
             label="genuine")
sns.distplot(impostor_distance, hist=False, kde=True,
             kde_kws={'shade': False, 'linewidth': 2},
             label="impostor")
plt.legend()
plt.title(model)
plt.xlabel("Score")
plt.savefig("density-%s.png" % model)
plt.show()
