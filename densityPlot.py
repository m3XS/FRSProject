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

plt.legend(prop={'size': 3}, title='type')
sns.distplot(genuine_distance, hist=False, kde=True,
             kde_kws={'shade': True, 'linewidth': 2},
             label="genuine")
sns.distplot(impostor_distance, hist=False, kde=True,
             kde_kws={'shade': False, 'linewidth': 3},
             label="impostor")

plt.show()
