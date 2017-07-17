import os
import numpy
import random
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET


def add_box(size, position, link_name):
    link = Element("link")
    link.set("name", link_name)
    #pose = ET.SubElement(link, "pose")
    #pose.text = " ".join(str(round(e, 2)) for e in position)

    geometry = Element("geometry")
    box = ET.SubElement(geometry, "box")
    size_element = ET.SubElement(box, "size")
    size_element.text = " ".join(str(round(e, 2)) for e in size)

    visual = ET.SubElement(link, "visual")
    visual.set("name", "visual")
    visual.append(geometry)

    collision = ET.SubElement(link, "collision")
    collision.set("name", "collision")
    collision.append(box)

    return link

def create_sdf(name, directory):

    sdf = Element("sdf")
    sdf.set("version", "1.4")
    model = ET.SubElement(sdf, "model")
    model.set("name", name)
    static = ET.SubElement(model, "static")

    for i in range(2):
        box = add_box([random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)], [0, 0, .5*i], str(i))
        model.append(box)

    create_file(directory+"/model.sdf", ET.tostring(sdf))

def create_config(name, directory):
    context = """<model>
          <name>"""+name.replace("_", " ")+"""</name>
          <version>1.0</version>
          <sdf version='1.4'>model.sdf</sdf>
          <author>
           <name>Adam Kantorik</name>
           <email>me@my.email</email>
          </author>
          <description>
            Automatically created description.
          </description>
        </model>
        """
    create_file(directory+"/model.config", context)


def create_file(location_name, context):
    numpy.savetxt(location_name, ["""<?xml version="1.0"?>
    """, context], fmt="%s")

def create_model(name):

    directory = "../Models/" + name
    if not os.path.exists(directory):
        os.makedirs(directory)

    create_config(name, directory)
    create_sdf(name, directory)

def main():
    print("running model creator")
    name = input("Enter a robot name (lowercase without spaces): ")

    create_model(name)
if __name__ == "__main__": main()
