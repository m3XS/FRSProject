import numpy
import os

from DET import DET

from matplotlib import pyplot as plt

#Files
base = 'C:/Users/Max/PycharmProjects/frProject'

genuine_distance_file = os.path.join(base, 'genuine_scores_1vs1.txt')
impostor_distance_file = os.path.join(base, 'impostor_scores_1vs1.txt')

# Read scores we saved
with open(genuine_distance_file, 'r') as f:
    genuine_scores = numpy.asarray(f.read().splitlines())

with open(impostor_distance_file, 'r') as f:
    impostor_scores = numpy.asarray(f.read().splitlines())

# Create and configure figure
det = DET(biometric_evaluation_type='algorithm', plot_title='FMR-FNMR')

#det.x_limits = numpy.array([1e-4, .5])
#det.y_limits = numpy.array([1e-4, .5])
#det.x_ticks = numpy.array([1e-3, 1e-2, 5e-2, 20e-2, 40e-2])
#det.x_ticklabels = numpy.array(['0.1', '1', '5', '20', '40'])
#det.y_ticks = numpy.array([1e-3, 1e-2, 5e-2, 20e-2, 40e-2])
#det.y_ticklabels = numpy.array(['0.1', '1', '5', '20', '40'])

det.create_figure()
det.plot(tar=genuine_scores, non=impostor_scores, label='distance')
det.legend_on()

# Save DET plot
det.save('example','png')




