#TODO: Need to delete the repo first before cloning it

import git

# Cloning Tracy's repo
git.Git().clone("https://github.com/triketora/women-in-software-eng.git", "/women-in-tech-datasets/triketora")

# Our cloned repo
cloned_repo = git.Git("/Users/rramani/rramani/women-in-tech-datasets/dataSet")

# Getting historic commit information for data.txt
loginfo = cloned_repo.log('--', '-p', '--', 'data.txt')
print loginfo
