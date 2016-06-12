'''
Created on 28/03/2016

@author: Jessica
'''

import os




if __name__ == '__main__':
         
    package_name = "\\com\\treasures"    
    commit_message = "Committing file "
         
    x = 0     
         
    for file in os.listdir("changes"):
        if file.endswith(".java"):
            file_name, file_extension = os.path.splitext(file)
            print (file_name)
            
            changedir = "changes\\" + str(x)
            packagedir = "changes\\" + str(x) + package_name
            os.makedirs(packagedir)
            print ("created dir {0}".format(packagedir))
    
            with open(changedir + '\\commit-message.txt', 'w') as f:
                f.write(commit_message + file_name)
    
            os.system('cp %s %s' % ("changes\\" + file, packagedir + "\\" + file))
    
            x=x+1
            
            
            