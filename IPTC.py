#pip3 install iptcinfo3

from iptcinfo3 import IPTCInfo
import glob
import argparse
import os
from os.path import join
import pandas as pd
''''''

def main():
    f = open('changedIPTCmeta.txt', 'w')

    parser = argparse.ArgumentParser()
    parser.add_argument("-image_path", help='path to jpg images', type=str, required=True)
    image_path = parser.parse_args()

    data = pd.read_csv('iptcmeta.csv')
    i = 0

    for filename in data['fileName']:
        info = IPTCInfo(join(image_path.image_path, filename))
        oldKeywords = info['keywords']
        oldObjName = info['object name']
        oldCaption = info['caption/abstract']
        newkey = data.at[i,'keywords'].split(',')
        info['object name'] = data.at[i, 'obj_name']
        info['caption/abstract'] = data.at[i, 'caption']
        info['keywords'] = newkey
        f.write('В файле ' + str(filename) + ' значения keywords изменились с ' + str(oldKeywords) + ' на ' + str(newkey) + ' значения object_name изменились с ' + str(oldObjName) + ' на ' + str(info['object name'])  + ' значения caption изменились с ' + str(oldCaption) + ' на ' + str(info['caption/abstract']) + '\n')
        info.save()
        print(filename)
        i = i + 1

    f.close()

main()
