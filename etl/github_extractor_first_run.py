# PATCH script - first time run

import git
from git import Git
from shutil import copyfile

# Grab todays date
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d")

# Cloning Tracy's repo
git.Git().clone("https://github.com/triketora/women-in-software-eng.git", "/women-in-tech-datasets/triketora")

# Our repo
cloned_repo = git.cmd.Git("/women-in-tech-datasets/triketora")
cloned_repo1 = Git("/women-in-tech-datasets/triketora")

# Getting sha for historic commits
loginfo = cloned_repo.log('--format=format:%H', '--', '--', 'data.txt') 
# Converting it into an array
loginfo_array = loginfo.split('\n')

ntp = open("/datasets/tracy_data/new_to_parse.txt")
for hexsha in loginfo_array:
	cloned_repo1.checkout(hexsha)
	copyfile("/women-in-tech-datasets/triketora/data.txt", "/datasets/tracy_data/data_%s.txt" % hexsha)
	ntp.append("data_%s.txt" % hexsha)
ntp.close()

f = open("/datasets/tracy_data/success_runDate.txt")
f.write(now)
f.close()
