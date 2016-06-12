'''
Created on 28/03/2016

@author: Jessica
'''

import os



if __name__ == '__main__':
         
    x = 0     
         
    for file in os.listdir("changes"):
        if file.endswith(".java"):
            algorithm, file_extension = os.path.splitext(file)
            print (algorithm)
            
            changedir = "changes\\" + str(x)
            epidir = "changes\\" + str(x) + "\\com\\epi"
            os.makedirs(epidir)
            print ("created dir {0}".format(epidir))
    
            with open(changedir + '\\commit-message.txt', 'w') as f:
                f.write('Algorithm ' + algorithm + ' from Elements of Programming Interviews, for comparison purposes only')
    
            os.system('cp %s %s' % ("changes\\" + file, epidir + "\\" + file))
    
            x=x+1
            
            
            