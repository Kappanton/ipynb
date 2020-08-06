from PIL import Image
from statistics import median
import glob
import argparse
import os
from os.path import join

def main():
    f = open('meanRGB.csv', 'w')
    ff = open('medianRGB.csv', 'w')

    parser = argparse.ArgumentParser()
    parser.add_argument("-image_path", help='path to png images', type=str, required=True)
    image_path = parser.parse_args()

    for filename in glob.glob(join(image_path.image_path, '*.png')):   #проходим по всем файлам в папке, у которых расширение "png"
        image = Image.open(filename)
        image = image.convert('RGBA')
        pix = image.load()

        width, height = image.size
        totalR = []
        totalG = []
        totalB = []
        totalRez = width * height

        for i in range(width):
            for j in range(height):
                if pix[i, j][3] == 0:
                    totalRez = totalRez - 1    #если есть прозрачные пиксели, то отбрасываем их
                else:
                    r = pix[i, j][0]
                    g = pix[i, j][1]
                    b = pix[i, j][2]
                    totalR.append(r)
                    totalG.append(g)
                    totalB.append(b)

        meanR = sum(totalR) / totalRez
        meanG = sum(totalG) / totalRez
        meanB = sum(totalB) / totalRez
        medianR = median(totalR)
        medianG = median(totalG)
        medianB = median(totalB)

        f.write(str(filename[image_path.image_path.__len__()+1:]) + ';' + str(round(meanR)) + ';' + str(round(meanG)) + ';' + str(round(meanB)) + '\n')
        ff.write(str(filename[image_path.image_path.__len__()+1:]) + ';' + str(round(medianR)) + ';' + str(round(medianG)) + ';' + str(round(medianB)) + '\n')

    ff.close()
    f.close()


main()
