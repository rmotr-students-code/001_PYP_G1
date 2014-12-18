import github3

# Andy: The API provides a few methods related to starring repos
# http://github3py.readthedocs.org/en/latest/search.html?q=star
# However, none of them are directly related to counting the
# numbers of stars the logged user has for their repos.
# Any ideas, guys?
# Jonathan: using iter_repos and then stargazers returns the number of stars a repo has.
# The following code works fine, feel free to optimize it if you like.


from github3 import login

#Login
username = raw_input('Enter username: ')
password = raw_input('Enter password: ')

gh = login(username, password)

global_user = gh.user()

#Check for the most starred repos on an account.
def check_repo():
    star_list = []
    name_list = []
    x_size = 0
    announcer = 0
    for repo in gh.iter_repos():
        star_list.append(repo.stargazers)
        name_list.append(repo)
    for x in star_list:
        if x > x_size:
            x_size = x
    for x in range(len(star_list)):
        if star_list[x] == x_size:
            if announcer == 0:
                print('Most starred repos:')
                announcer += 1
            print(name_list[x])

check_repo()
