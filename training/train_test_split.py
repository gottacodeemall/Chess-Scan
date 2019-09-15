import os
import os
import cv2
import numpy as np
import argparse
from optparse import OptionParser
import xml.etree.ElementTree as ET

from pathlib import Path


def add_end_slash(path):
    if path[-1] is not '/':
        return path + '/'
    return path


def create_path(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)


def get_file_name(path):
    path = path.split(' \\')
    print(path)
    base_dir = path[:len(path)-1]
    base_dir = '/'.join(str(x) for x in base_dir)
    names = path[-1].split('.')
    file_name = names[0]
    ext = names[1]
    return (base_dir, file_name, ext)


def process_image(file_path, output_path, x, y, save_box_images):
    (base_dir, file_name, ext) = get_file_name(file_path)
    image_path = '{}/{}.{}'.format(base_dir, file_name, ext)
    xml = '{}/{}.xml'.format(base_dir, file_name)
    try:
        print(image_path,xml)
        resize(
            image_path,
            xml,
            (x, y),
            output_path,
            save_box_images=save_box_images,
        )
    except Exception as e:
        print('[ERROR] error with {}\n file: {}'.format(image_path, e))
        print('--------------------------------------------------')

IMAGE_FORMATS = ('.jpeg', '.png', '.jpg','.JPG')
from pathlib import Path
for root, _, files in os.walk('./output'):
        #train_path = os.path.join('./train', root[len('./output'):])
        #print(train_path)
        #test_path = os.path.join('./test', root[len('./output'):])
        train_path = './train'
        test_path = './test'
        create_path(train_path)
        create_path(test_path)
        print(root)

        count = 0
        for file in files:
            if file.endswith(IMAGE_FORMATS):
                    file_path = os.path.join(root, file)
                    spli = file_path.split('\\')
                    file_name = spli[-1]
                    base_dir = 'output'
                    ext = 'JPG'


                    file_name = Path(file_name).stem
                    image_path = '{}/{}.{}'.format(root, file_name, ext)
                    xml = '{}/{}.xml'.format(root, file_name)
                    print(image_path,xml)
                    xmlRoot = ET.parse(xml).getroot()
                    image = cv2.imread(image_path)
                    tree = ET.ElementTree(xmlRoot)
                    if count % 5 == 0:
                        cv2.imwrite(os.path.join(test_path, '.'.join([file_name, ext])), image)
                        tree.write('{}/{}.xml'.format(test_path, file_name, ext))
                    else:
                        cv2.imwrite(os.path.join(train_path, '.'.join([file_name, ext])), image)
                        tree.write('{}/{}.xml'.format(train_path, file_name, ext))
                    count = count + 1