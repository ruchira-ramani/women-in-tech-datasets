#TODO: Need to comment out the clone repo command after first run
#TODO: Handle historic data efficiently (right now if I make an update I will pull up all history, tomorrow again if I make an update it will again pull up all of history)

import git
from git import Git
from shutil import copyfile

# Cloning Tracy's repo (One time clone)
#git.Git().clone("https://github.com/triketora/women-in-software-eng.git", "/women-in-tech-datasets/triketora")

# Git pull (cron job)
cloned_repo = git.cmd.Git("/women-in-tech-datasets/triketora")
cloned_repo1 = Git("/women-in-tech-datasets/triketora")

# Getting sha for historic commits
loginfo = cloned_repo.log('--format=format:%H', '--', '--', 'data.txt') 
# Converting it into an array
loginfo_array = loginfo.split('\n')

for hexsha in loginfo_array:
	cloned_repo1.checkout(hexsha)
	copyfile("/women-in-tech-datasets/triketora/data.txt", "/datasets/company_coder_gender_stats/data_%s.txt" % hexsha)	
