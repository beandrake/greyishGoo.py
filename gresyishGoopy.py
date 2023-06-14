from github import Github
import os


def replicate(login_or_token):
	"""
	Makes a copy of the original greyishGoopy repo so you can have one in your repo too.
	:login_or_token: Your access for github.Github (see https://pypi.org/project/PyGithub/)
	"""
	gData = Github(login_or_token=login_or_token)
	currentUser = gData.get_user()
	repoToFork = gData.get_repo(r'beandrake/greyishGoopy')

	# Just to be explicit, check if the user already has a greyishGoopy
	for repo in currentUser.get_repos():
		if repo.name == repoToFork.name:
			print(f"User {currentUser.name} already has a repo named {repo.name}.")
			print(f"All is right with the world and no further replication is needed.")
			return repo

	# Make the fork
	newRepo = currentUser.create_fork(repoToFork)
	print(f"User {currentUser.name} has received the gift of a {newRepo.name} repo!")
	return newRepo


if __name__ == "__main__":
	myOAuth = os.environ['github_OAuth']	# Gets OAuth from environment variable
	newRepo = replicate(login_or_token=myOAuth)
	input(r"Press Enter to continue...")
