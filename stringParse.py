import os
import pdb 
import xml.etree.ElementTree as ET

pathM = 'sudo ruby secgen.rb -s scenarios/examples/vulnerability_examples/insecure_web_applications/commando/'
tree = ET.parse('dummy.xml')
root = tree.getroot()

#!ET

def printAllbyET():
    print('\nAll attributes:')
    for x in tree.findall(".//"):
        print(x.tag,"|--->",x.attrib,x.text)
   
   
def vuln():
    
    print("\n\n******************Vulnerabilities*****************\n\n")
    for x in root.findall(".//vulnerability"):
        print(x.tag,"--->",x.attrib) 
            
    ch = input('\nEnter Tag you want to display : ')
    for x in root.findall(f'.//vulnerability[@type="{ch}"]'):
        print(x.tag,"--->",x.attrib) # To display selected Ta
        
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['type'] = f'{changes}'
        
    tree.write("Updated.xml")
def encoders():
    print("\n\n******************Encoders*****************\n\n")
    
    for x in tree.findall(".//encoder"):
        print(x.tag,"--->",x.attrib)
    
    ch = input('\nEnter Tag you want to display : ')
    for x in root.findall(f'.//encoder[@type="{ch}"]'):
        print(x.tag,"--->",x.attrib) # To display selected Ta
        
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['type'] = f'{changes}'
        
    tree.write("Updated.xml")

def value():
    print("\n\n******************Values*****************\n\n")
    
    for x in tree.findall(".//value"):
        print(x.tag,"--->",x.text)
    
    ch = input('\nEnter Tag you want to display : ')
    for x in root.findall(f'.//value[@type="{ch}"]'):
        print(x.tag,"--->",x.attrib) # To display selected Ta
        
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['type'] = f'{changes}'
        
    tree.write("Updated.xml")
    
def input1():
    print("\n\n******************Input*****************\n\n")
    for x in tree.findall(".//input"):
            print(x.tag,"--->",x.attrib)
    
    ch = input('\nEnter Tag you want to display : ')
    for x in root.findall(f'.//input[@into="{ch}"]'):
        print(x.tag,"--->",x.attrib) # To display selected Ta
        
        changes = str(input('\nEnter the tag you want to change : '))
        x.attrib['into'] = f'{changes}'
        
    tree.write("Updated.xml")

def valuetag():
    for x in root.findall(".//value"):
        print(x.tag,"--->",x.text) # To display selected Ta
        changes = str(input('\nEnter the tag you want to change : '))
        x.text = f'{changes}'
        print(x.text)

# print("""   
#     Enter 1 to Display All TAGS ATTRIBUTES and TEXTS
#     Enter 2 for Vulnerabilities
#     Enter 3 for Encoders
#     Enter 4 for Values
#     Enter 5 for Input
#     Enter 6 to display all the tree
#     """)

# x = 1000

# while x!=0:
#     x = int(input("\nYour Choice  : "))
#     if x==1:
#         printAllbyET()
#     elif x==2:
#         vuln()
#     elif x==3:
#         encoders()
#     elif x==4:
#         value()
#     elif x==5:
#         input1()
#     elif x==6:
#         ET.dump(tree)
#     else:
#         print("\nInvalid Choice")
        
# os.write(pathM)
valuetag()
tree.write("Updated.xml")
