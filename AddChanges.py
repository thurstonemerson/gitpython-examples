'''
Created on 28/03/2016

@author: Jessica
'''

import os
from datetime import time, date, datetime, timedelta
from random import randint
from utils import copytree
import git

class AddChanges:

    def __init__(self, first_date=date.today(),
                last_date=date.today(), change_directory="changes",
                 number_of_changes=1):
        self.first_date = first_date
        self.last_date = last_date
        self.number_of_changes = number_of_changes
        self.repo_path = os.getcwd()
        self.change_directory = change_directory
        self.changes_file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), self.change_directory)

        self.changes = self._load_changes()
        
    def _load_changes(self):
        
        changes = []
        
        for change in range(self.number_of_changes):
            change_file_dir = os.path.join(self.changes_file_path, str(change))
            print("The change file directory is {0}".format(change_file_dir))
            with open(os.path.join(change_file_dir, "commit-message.txt")) as f:
                message = f.read()
            changes.append((message, change_file_dir))
             
        print(changes)
        return changes     
            
    def _edit_and_commit(self, commit_date, message, change_file_dir):
        #for every file in the change directory, copy to the new place
        print("copytree {0} {1}".format(change_file_dir, os.getcwd()))
     
        new_files = copytree(change_file_dir, os.getcwd() + "\\algorithms")
        
        new_files = [file for file in new_files if not file.endswith("commit-message.txt")]
        
        for file in new_files:
            print ("Adding file {0}".format(file))  
              
        self.repo.index.add(new_files)
        date_in_iso = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        self.repo.index.commit(message, author_date=date_in_iso, commit_date=date_in_iso)
        print("{0}{1}".format(commit_date, message))

    def _get_random_time(self):
        return time(hour=randint(0, 23), minute=randint(0, 59),
                    second=randint(0, 59), microsecond=randint(0, 999999))

    def _get_dates_list(self):
        dates = []
        day_num = 0
        
        for change in range(self.number_of_changes):
            #increment by one day
            dates.append(self.first_date + timedelta(days=day_num))
            day_num = day_num + 1
            
        return [datetime.combine(d, self._get_random_time()) for d in dates]

    def make_changes(self):
        print('Making changes')
        self.repo = git.Repo(self.repo_path + "\\algorithms")
           
        dates = self._get_dates_list()
        dates.sort()
        for commit_date in dates:
            self._edit_and_commit(commit_date, *self.changes.pop(0))
        print('\nCompleted making changes!')

    
if __name__ == '__main__':
    magic = AddChanges(number_of_changes=4, first_date=datetime.strptime('10 Jun 2016', '%d %b %Y'),
                     last_date=datetime.strptime('13 Jun 2016', '%d %b %Y'))
    magic.make_changes()