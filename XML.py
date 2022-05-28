import os
import itertools
import threading
import time
import sys
import xml.etree.ElementTree as ET
from termcolor import colored
ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
ET.register_namespace("","http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
pathM = 'sudo ruby secgen.rb -s scenarios/examples/vulnerability_examples/insecure_web_applications/commando/'
newfile = ("Updated.xml")
tree = ET.parse('impossible.xml')
root = tree.getroot()

def load():
    done = False
    #here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')
        

    t = threading.Thread(target=animate)
    t.start()
    
    #long process here
    time.sleep(2)
    done = True
#!ET

def printAllbyET():
    print('\nAll attributes:')
    for x in tree.findall(".//"):
        print(x.tag,"|--->",x.attrib,x.text)

def vuln():
    print("\n\n******************Vulnerabilities*****************\n\n")
    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}vulnerability"):
        print(x.tag,"--->",x.attrib) 
            
    ch = input('\nEnter Tag you want to change : ')
    for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}vulnerability[@module_path='{ch}']"):
        print("Tag you want to change ",x.tag,"--->",x.attrib) 
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['module_path'] = f'{changes}'
    load()
    tree.write(newfile)
    
def encoders():
    print("\n\n******************Encoders*****************\n\n")
    
    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}encoder"):
        print(x.tag,"--->",x.attrib)
    
    ch = input('\nEnter Tag you want to change : ')
    for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}encoder[@name='{ch}']"):
        print("Tag you want to change ",x.tag,"--->",x.attrib) 
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['name'] = f'{changes}'
    load()
    tree.write(newfile)
 
def generator():
    print("\n\n******************Generator*****************\n\n")
    
    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}generator"):
        print(x.tag,"--->",x.attrib)
    a = None
    a = int(input(" Press 1 to change the attribute type \n Press 2 to change the attribute module_path : "))
    if a == 1 :
        ch = input('\nEnter Tag you want to change : ')
        for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}generator[@type='{ch}']"):
            print("Tag you want to change ",x.tag,"--->",x.attrib) 
            changes = str(input('\nEnter Your changed tag : '))
            x.attrib['type'] = f'{changes}'
        load()  
        tree.write(newfile)
    elif a == 2:
        ch = input('\nEnter Tag you want to change : ')
        for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}generator[@module_path='{ch}']"):
            print("Tag you want to change ",x.tag,"--->",x.attrib) 
            changes = str(input('\nEnter Your changed tag : '))
            x.attrib['module_path'] = f'{changes}'
        load()  
        tree.write(newfile)
    else:
        print(colored("INVALID INPUT",'red', attrs=['bold']))
        mainProg()

def input1():
    print("\n\n******************Input*****************\n\n")
    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}input"):
            print(x.tag,"--->",x.attrib)
    
    a = int(input(" Press 1 to change the attribute into \n Press 2 to change the attribute into_datastore : "))
    if a == 1 :
        ch = input('\nEnter Tag you want to change : ')
        for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}generator[@into='{ch}']"):
            print("Tag you want to change ",x.tag,"--->",x.attrib) 
            changes = str(input('\nEnter Your changed tag : '))
            x.attrib['into'] = f'{changes}'
        load()  
        tree.write(newfile)
    elif a==2:
        ch = input('\nEnter Tag you want to change : ')
        for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}generator[@into_datastore='{ch}']"):
            print("Tag you want to change ",x.tag,"--->",x.attrib) 
            changes = str(input('\nEnter Your changed tag : '))
            x.attrib['into_datastore'] = f'{changes}'
        load()  
        tree.write(newfile)
    else:
        print(colored("INVALID INPUT",'red', attrs=['bold']))
        mainProg()
        
def dataStore():
    print("\n\n******************Input*****************\n\n")
    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}datastore"):
            print(x.tag,"--->",x.attrib,'|-->',x.text)
    
    a = int(input(" Press 1 to change the attribute into \n Press 2 to change the text of DataStore Tag: "))
    if a == 1 :
        ch = input('\nEnter Tag you want to change : ')
        for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}datastore[@access='{ch}']"):
            print("Tag you want to change ",x.tag,"--->",x.attrib) 
            changes = str(input('\nEnter Your changed tag : '))
            x.attrib['access'] = f'{changes}'
        load()
        tree.write(newfile)
    elif a==2:
        for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}datastore"):
            print(x.tag,"--->",x.text) # To display selected Ta
            changes = str(input('\nEnter the value you want to change : '))
            x.text = f'{changes}'
            print(x.text)
            load()
    else:
        print("\nInvalid Choice",'red', attrs=['bold'])
        
def addNetwork():
    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}network"):
            print(x.tag,"--->",x.attrib)
    
    ch = input('\nEnter Tag you want to change : ')
    for x in root.findall(f".//{{http://www.github/cliffe/SecGen/scenario}}network[@type='{ch}']"):
        print("Tag you want to change ",x.tag,"--->",x.attrib) 
        changes = str(input('\nEnter Your changed tag : '))
        x.attrib['type'] = f'{changes}'
    load()    
    tree.write(newfile)
    
def insValue():
    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}value"):
        print(x.tag,"--->",x.text) # To display selected Ta
        changes = str(input('\nEnter the value you want to change : '))
        x.text = f'{changes}'
        print(x.text)
        load()    
    tree.write(newfile)
    
def chngType():
    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}type"):
        print(x.tag,"--->",x.text) # To display selected Ta
        changes = str(input('\nEnter the value you want to change : '))
        x.text = f'{changes}'
        print(x.text)
        load()
    tree.write(newfile)

def difficulty():
    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}difficulty"):
        print(x.tag,"--->",x.text) # To display selected Ta
        changes = str(input('\nEnter the value you want to change : '))
        x.text = f'{changes}'
        print(x.text)
        load()
    tree.write(newfile)
    
def mainProg():
    print(colored("""   
        Enter 1 to Display All TAGS ATTRIBUTES and TEXTS
        Enter 2 for Vulnerabilities
        Enter 3 for Encoders
        Enter 4 for Generators
        Enter 5 for Input
        Enter 6 for Data Stores
        Enter 7 for Networks
        Enter 8 to display all the tree
        Enter 9 for type
        Enter 11 for dificulty
        """,'yellow', attrs=['bold']))
    x = None
    while x!=0:
        x = int(input("\nYour Choice  : "))
        if x==1:
            printAllbyET()
        elif x==2:
            vuln()
        elif x==3:
            encoders()
        elif x==4:
            generator()
        elif x==5:
            input1()
        elif x==6:
             dataStore()
        elif x==7:
            addNetwork()
        elif x==8:
            ET.dump(tree)
        elif x==9:
            chngType()
        elif x==11:
            difficulty()
        else:
            print("\nInvalid Choice",'red', attrs=['bold'])
            

mainProg()
load()
# os.system(pathM+NewFile)
