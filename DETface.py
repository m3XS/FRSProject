import numpy
import os

from DET import DET

from matplotlib import pyplot as plt

local_path = os.getcwd()

genuine_distance_file_facenet = os.path.join(local_path, 'distance/FaceNet/genuine_distance.txt')
impostor_distance_file_facenet = os.path.join(local_path, 'distance/FaceNet/impostor_distance.txt')

genuine_distance_file_vgg = os.path.join(local_path, 'distance/VGG-Face/genuine_distance.txt')
impostor_distance_file_vgg = os.path.join(local_path, 'distance/VGG-Face/impostor_distance.txt')

genuine_distance_file_openface = os.path.join(local_path, 'distance/OpenFace/genuine_distance.txt')
impostor_distance_file_openface = os.path.join(local_path, 'distance/OpenFace/impostor_distance.txt')

# Read scores we saved
#FaceNet
with open(genuine_distance_file_facenet, 'r') as f:
    genuine_distance_facenet = numpy.asarray(f.read().splitlines())

with open(impostor_distance_file_facenet, 'r') as f:
    impostor_distance_facenet = numpy.asarray(f.read().splitlines())
#VGG-Face
with open(genuine_distance_file_vgg, 'r') as f:
    genuine_distance_vgg = numpy.asarray(f.read().splitlines())

with open(impostor_distance_file_vgg, 'r') as f:
    impostor_distance_vgg = numpy.asarray(f.read().splitlines())
#OpenFace
with open(genuine_distance_file_openface, 'r') as f:
    genuine_distance_openface = numpy.asarray(f.read().splitlines())

with open(impostor_distance_file_openface, 'r') as f:
    impostor_distance_openface = numpy.asarray(f.read().splitlines())

# Create and configure figure
det = DET(biometric_evaluation_type='algorithm', plot_title='FMR-FNMR')

det.x_limits = numpy.array([1e-4, .5])
det.y_limits = numpy.array([1e-4, .5])
det.x_ticks = numpy.array([1e-3, 1e-2, 5e-2, 20e-2, 40e-2])
det.x_ticklabels = numpy.array(['0.1', '1', '5', '20', '40'])
det.y_ticks = numpy.array([1e-3, 1e-2, 5e-2, 20e-2, 40e-2])
det.y_ticklabels = numpy.array(['0.1', '1', '5', '20', '40'])

det.create_figure()
det.plot(tar=impostor_distance_facenet, non=genuine_distance_facenet, label='FaceNet')
det.plot(tar=impostor_distance_vgg, non=genuine_distance_vgg, label='VGG-Face')
det.plot(tar=impostor_distance_openface, non=genuine_distance_openface, label='OpenFace')
det.legend_on()

# Save DET plot
det.save('DET', 'png')
det.show()


