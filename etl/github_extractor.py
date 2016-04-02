import git
from git import Git
from shutil import copyfile
import datetime

# Grab todays date
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d")

# Git pull (cron job)
cloned_repo = git.cmd.Git("/women-in-tech-datasets/triketora")
cloned_repo1 = Git("/women-in-tech-datasets/triketora")

# Getting sha for historic commits since last successfull run
loginfo = cloned_repo.log('--format=format:%H', '--since=%s' % now, '--', 'data.txt')
# Converting it into an array
loginfo_array = loginfo.split('\n')

# Run only if there have been commits
ntp = open("/datasets/tracy_data/new_to_parse.txt")
if len(loginfo_array) > 1:
	for hexsha in loginfo_array:
		cloned_repo1.checkout(hexsha)
		copyfile("/women-in-tech-datasets/triketora/data.txt", "/datasets/company_coder_gender_stats/data_%s.txt" % hexsha)
		ntp.append("data_%s.txt" % hexsha)
ntp.close()

f = open("/datasets/tracy_data/success_runDate.txt", "w+")
f.write(now)
f.close()
