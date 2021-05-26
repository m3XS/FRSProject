import os, numpy

local_path = os.getcwd()
impostor_distance_file = os.path.join(local_path, 'impostor_distance.txt')
genuine_distance_file = os.path.join(local_path, 'genuine_distance.txt')

with open(impostor_distance_file, 'r') as f:
    impostor_distance = numpy.asarray(f.read().splitlines(), dtype=float)

with open(genuine_distance_file, 'r') as f:
    genuine_distance = numpy.asarray(f.read().splitlines(), dtype=float)

#Threshold for calculating
#DeepFace Threshold for: VGG-Face: 0.4, FaceNet: 0.4, OpenFace 0.1
t = 0.08
model = "OpenFace"

print("------%s------" % model)
print("threshold: " + str(t))
print("-------------------------")
print("Impostor Count < %s:\t\t" % t + str((impostor_distance < t).sum()))
print("Genuine Count < %s:\t\t" % t + str((genuine_distance < t).sum()))
print("-------------------------")
print("FMR ((impostor sum < t) / impostor total * 100):\t\t" + str((impostor_distance < t).sum() / impostor_distance.shape[0] * 100))
print("FNMR 100 - ((genuine sum < t) / genuine total * 100)):\t" + str(100 - ((genuine_distance < t).sum() / genuine_distance.shape[0] * 100)))
print("-------------------------")