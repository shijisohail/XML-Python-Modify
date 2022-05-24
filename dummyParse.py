import xml.etree.ElementTree as ET
import os
ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
ET.register_namespace("","http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
pathM = 'sudo ruby secgen.rb -s scenarios/examples/vulnerability_examples/insecure_web_applications/commando/'
NewFile = 'updatedDummy.xml'
tree = ET.parse('dummy.xml')
root  = tree.getroot()


def parse():
    for x in root:
        print(x.tag,x.attrib,x.text)
      
    
def findElements(): 
     for x in root.iter('vulnerability'):
        print(x.attrib)

def findAll():
    for x in root.findall('vulnerability'):
        gener = x.find('generator').text  
        type1 = x.get('type')
        print(type1, gener)
   


def Modify():
    for x in root.iter('input'):
        new_input = str(input("Enter new tag :"))
        x.text = str(new_input)
        x.set('updated', 'yes')
        
    tree.write(NewFile)

 
print("""        Press 1 to Parse the Tags (XML File)
        Press 2 to to Find Elements
        Press 3 to Find All
        Press 4 to Modify Elements
""") 

""" ****Children are nested, and we can access specific child nodes by index: such as x.tag[0][1]**** """

x = int(input("Your Choice :"))
if x==1:
    parse()
    print("THis is 1")
if x==2:
    findElements()
    print("THis is 2 ")

if x==3:
    findAll()
    print("THis is 3")

if x==4:
    Modify()
    print("THis is 4")

# os.system(pathM+" run")
