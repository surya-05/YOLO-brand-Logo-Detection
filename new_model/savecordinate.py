import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
def write_xml(folder,img,objects,tl,br,savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)


    image=cv2.imread(img.path)
    height,width,depth=image.shape
    annotation=ET.Element('annotation')
    ET.SubElement(annotation,'folder').text=folder
    ET.SubElement(annotation,'filename').text=img.name
    ET.SubElement(annotation,'segmented').text='0'
    size=ET.SubElement(annotation,'size')
    ET.SubElement(size,'width').text=str(width)
    ET.SubElement(size,'height').text=str(height)
    ET.SubElement(size,'depth').text=str(depth)
    for obj,topl,botr in zip(objects,tl,br):
        ob=ET.SubElement(annotation,'object')
        ET.SubElement(ob,'name').text=obj
        ET.SubElement(ob,'pose').text='Unspecified'
        ET.SubElement(ob,'truncated').text='0'
        ET.SubElement(ob,'difficult').text='0'
        bbox=ET.SubElement(ob,'bnbbox')
        ET.SubElement(bbox,'xmin').text=str(topl[0])
        ET.SubElement(bbox,'xmin').text=str(topl[1])
        ET.SubElement(bbox,'xmin').text=str(topl[0])
        ET.SubElement(bbox,'xmin').text=str(topl[1])
    xml_str=ET.tostring(annotation)
    root=etree.fromstring(xml_str)
    xml_str=etree.tostring(root,pretty_print=True)
    save_path=os.path.join(savedir,img.name.replace('png','xml'))
    with open(save_path,'wb') as temp_xml:
        temp_xml.write(xml_str)
   # return xml_str;
if __name__=='__main__':
    folder='Samsung_Store'
    img=[im for im in os.scandir('Samsung_Store') if '1. 2017-03-29-image-9' in im.name][0]
    objects=['samsung_store']
    tl=[(10,10)]
    br=[(100,100)]
    savedir='annotation'
    write_xml(folder,img,objects,tl,br,savedir)
    
