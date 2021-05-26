import os

path = "C:/Users/Max/PycharmProjects/frProject/pic"

listDir = os.listdir(path)

print(listDir)

for dir in listDir:
    for i in os.listdir(os.path.join(path, dir)):
        print(i)
        tmp = i.split('.')
        tmp[1] = ".png"
        os.rename(os.path.join(path, dir + "/" + i), os.path.join(path, dir + "/" + tmp[0] + tmp[1]))
