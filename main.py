import os
import shutil
from distutils.dir_util import copy_tree


masterRepo = raw_input("Enter Repository Name: ")


#set up master
masterBranch = masterRepo+"/masterBranch/"
directory = os.path.dirname(masterBranch)
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


#create new branches
def branch(newBranch):

    newBranch = masterRepo+"/"+newBranch+"/"
    directory = os.path.dirname(newBranch)
    os.makedirs(directory)


#creates directories for checking/placing documents
def setUp(thisbranch):
    if(thisbranch != masterBranch):
        thisbranch = masterRepo + "/"+thisbranch
    SRS = thisbranch + "/SRS/"
    dirSRS = os.path.dirname(SRS)
    if not (os.path.exists(dirSRS)):
        os.makedirs(dirSRS)
    SDS = thisbranch + "/SDS/"
    dirSDS = os.path.dirname(SDS)
    if not (os.path.exists(dirSDS)):
        os.makedirs(dirSDS)
    Test = thisbranch + "/Test/"
    dirTest = os.path.dirname(Test)
    if not (os.path.exists(dirTest)):
        os.makedirs(dirTest)

#local repo
def init():
    localRepo = masterRepo+"/localRepo/"
    directory = os.path.dirname(localRepo)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return localRepo
    


#add/commit files
def commit(fileDirectory):
    maindir = masterRepo+"/localRepo/"
    copy_tree(fileDirectory, maindir+"rev/")

def push(thisbranch):
    if (thisbranch == masterBranch):
        branchLoc = thisbranch+"/"
    else:
        branchLoc = masterRepo+"/"+thisbranch+"/"
    maindir = masterRepo+"/localRepo/"
    copy_tree(maindir+"rev/", branchLoc)
    setUp(thisbranch)
    check(thisbranch)

#checks if the documents are there or not.
def check(thisbranch):
    if(thisbranch != masterBranch):
        thisbranch = masterRepo + "/"+thisbranch+"/"
    check = [1,1,1]
    if not os.listdir(thisbranch+"SRS/"):
        print('SRS Remaining')
    else:
        check[0] = 0
    if not os.listdir(thisbranch+"SDS/"):
        print('SDS Remaining')
    else:
        check[1] = 0
    if not os.listdir(thisbranch+"Test/"):
        print('Test Report Remaining')
    else:
        check[2] = 0
    if(check == [0,0,0]):
        print('Everything Done.')

#main function that launches the command line
def commandLine():
   cmd = " "
   while(cmd != "exit" or cmd != "EXIT"):
       cmd = raw_input(" > ") 
       if(cmd == "soft init"):
           maindir = init()
       if(cmd == "soft commit"):
           commit("/Users/aritropaul/Documents/Winter Sem 2017-18/Software/Project/PySoft/Fol 1/")
       if(cmd == "soft push"):
            branchName = raw_input(" > Branch : ")
            if(branchName == "master"):
                push(masterBranch)
            else:
                push(branchName)
       if(cmd == "exit"):
            exit()
       if(cmd == "branch"):
           branchName = raw_input(" > Branch : ")
           branch(branchName)


#runs the program.
commandLine()