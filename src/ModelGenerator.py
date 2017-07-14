import os
import numpy
import random

def add_box(size):
    box = """<collision name='collision'>
              <geometry>
                <box>
                  <size>"""+str(size[0])+" "+str(size[1])+" "+str(size[2])+"""</size>
                </box>
              </geometry>
            </collision>

            <visual name='visual'>
              <geometry>
                <box>
                  <size>"""+str(size[0])+" "+str(size[1])+" "+str(size[2])+"""</size>
                </box>
              </geometry>
            </visual>"""

    return box

def create_sdf(name, directory):

    elements = ""
    elements+= add_box([random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)])
    elements+= add_box([random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)])

    context = '''<?xml version='1.0'?>
      <sdf version='1.4'>
        <model name="'''+name+'''">
        <static>true</static>
          <link name='chassis'>
            <pose>0 0 .1 0 0 0</pose>

            '''+elements+'''
          </link>
      </model>
    </sdf>'''

    create_file(directory+"/model.sdf", context)

def create_config(name, directory):
    context = """<?xml version="1.0"?>
        <model>
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
    numpy.savetxt(location_name, [context], fmt="%s")

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
