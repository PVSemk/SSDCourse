import os
import xml.etree.ElementTree as ET

CLASS_DICT = {}
HOME_DIR = os.path.expanduser('~/CourseWork/data/FlickrLogos_47/VOC2007')
ANNOTATIONS_PATH = os.path.join(HOME_DIR, 'Annotations')

#Remove xml files which were creater in previous trials
os.system('cd Annotations; rm *.xml')

with open(HOME_DIR + '/className2ClassID.txt') as file:
    for line in file:
        line = line.split()
        CLASS_DICT[line[1]] = line[0]

# create the file structure
# Здесь теряю закрытие файла, мб переделать
size_file = open(HOME_DIR + '/ImageSize.txt').read().split('\n') # fmt: ['name width height',]
# File fmt: <x1> <y1> <x2> <y2> <class_id> <dummy_value> <mask> <difficult> <truncated>
for idx, file in enumerate(os.listdir(ANNOTATIONS_PATH)): # индекс нужен для поиска размера картинки
    file_path = os.path.join(ANNOTATIONS_PATH, file)
    annotation_file = open(file_path, 'r')
    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = 'VOC2007'
    ET.SubElement(annotation, 'filename').text = file[:7] + 'jpg' # Берем из названия цифры без расширения
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = size_file[idx].split()[1]
    ET.SubElement(size, 'height').text = size_file[idx].split()[2]
    ET.SubElement(size, 'depth').text = '3' # RGB
    ET.SubElement(annotation, 'segmented').text = '0'
    for line in annotation_file: # Создаем столько объектов, сколько в txt файле строк
        line = line.split()
        object = ET.SubElement(annotation, 'object')
        ET.SubElement(object, 'name').text = CLASS_DICT[line[4]] # Находим название класса по class_id
        ET.SubElement(object, 'pose').text = 'Unspecified'
        ET.SubElement(object, 'truncated').text = line[8]
        ET.SubElement(object, 'difficult').text = line[7]

        bbox = ET.SubElement(object, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = line[0]
        ET.SubElement(bbox, 'ymin').text = line[1]
        ET.SubElement(bbox, 'xmax').text = line[2]
        ET.SubElement(bbox, 'ymax').text = line[3]

    # create a new XML file with the results
    mydata = ET.tostring(annotation, encoding='unicode', method='xml')
    myfile = open(os.path.join(ANNOTATIONS_PATH, '{}.xml'.format(file[:6])), "w")
    myfile.write(mydata)
    myfile.close()
