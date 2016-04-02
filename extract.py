import pygithub3
from pygithub3 import Github
gh = Github()

# lists all the commits that reference data.txt tracy's repo
data_hist = gh.repos.commits.list(user='triketora',repo='women-in-software-eng',sha='master',path='data.txt')
print(data_hist.all())
