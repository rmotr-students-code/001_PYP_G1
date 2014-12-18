# GITHUB
from github3 import login

def main():
    print "enter name"
    username = raw_input()
    print "enter password"
    password = raw_input()
    gh = login(username, password)
    
    repos = []
    for repo in gh.iter_repos():
        repos.append(repo)
    
    for repo in sorted(repos, key=lambda x: x.stargazers, reverse=True):
        print repo.name
    
if __name__=="__main__":
    main()