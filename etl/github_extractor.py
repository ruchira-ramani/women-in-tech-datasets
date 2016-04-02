#TODO: Need to comment out the clone repo command after first run

import git

# Cloning Tracy's repo (One time clone)
git.Git().clone("https://github.com/triketora/women-in-software-eng.git", "/women-in-tech-datasets/triketora")

# Git pull (cron job)
cloned_repo = git.cmd.Git("/women-in-tech-datasets/triketora")

# Getting historic commit information for data.txt
loginfo = cloned_repo.log('--', '-p', '--', 'data.txt')