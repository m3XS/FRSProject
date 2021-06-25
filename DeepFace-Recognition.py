#Libraries
from deepface import DeepFace
import os as os

# Files
path = 'C:/Users/Max/PycharmProjects/FRSProject/pic'
base = 'C:/Users/Max/PycharmProjects/FRSProject'

# Model
models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
selected_model = models[2]
model = DeepFace.build_model(selected_model)
print("Selected model: " + selected_model)
# Impostor and Genuie
total_number_subjects = 20     # 100 subjects for CasiaV5
# total_number_sessions = 1       # only 1 session in CasiaV5
total_number_face = 4           # four faces for one session each subject CasiaV5
extension = ".png"

genuine_distance = []
impostor_distance = []
genuine_distance_file = os.path.join(base, 'genuine_distance.txt')
impostor_distance_file = os.path.join(base, 'impostor_distance.txt')
step = 0

# r = reference, p = probe
for subject_number_r in range(total_number_subjects):
    for face_number_r in range(total_number_face):

        reference_name = ""
        if subject_number_r < 10:
            filename = "00" + str(subject_number_r) + "_" + str(face_number_r)
            reference_name = path + "/" + filename + extension
        elif subject_number_r < 100:
            filename = "0" + str(subject_number_r) + "_" + str(face_number_r)
            reference_name = path + "/" + filename + extension
        else:
            filename = str(subject_number_r) + "_" + str(face_number_r)
            reference_name = path + "/" + filename + extension

        for subject_number_p in range(subject_number_r, total_number_subjects):
            for face_number_p in range(face_number_r, total_number_face):
                probe_name = ""
                if subject_number_p < 10:
                    filename = "00" + str(subject_number_p) + "_" + str(face_number_p)
                    probe_name = path + "/" + filename + extension
                elif subject_number_p < 100:
                    filename = "0" + str(subject_number_p) + "_" + str(face_number_p)
                    probe_name = path + "/" + filename + extension
                else:
                    filename = str(subject_number_p) + "_" + str(face_number_p)
                    probe_name = path + "/" + filename + extension

                step = step + 1
                print(str(step) + "/2100")
                print(reference_name)
                print(probe_name)


                verify = DeepFace.verify(probe_name, reference_name, model_name=selected_model, model=model)
                #print(verify)

                if subject_number_r == subject_number_p:
                    genuine_distance.append(verify['distance'])
                    #print("genuine")
                else:
                    impostor_distance.append(verify['distance'])
                    #print("impostor!")

# Save distance to files
with open(genuine_distance_file, 'w') as f:
    for sc in genuine_distance:
        f.write("%s\n" % sc)

with open(impostor_distance_file, 'w') as f:
    for sc in impostor_distance:
        f.write("%s\n" % sc)

print("Done!")