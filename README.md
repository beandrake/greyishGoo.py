# greyishGoopy
Uses the Github API and PyGithub to fork a copy of this repository to your Github account.

## Windows Instructions:
1. You'll need a way to authenticate your account with Github; if you don't already have an access token, you can create one with **repo** scope.
See [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

2. Open a command window and make a local clone of this repository:

       git clone https://github.com/beandrake/greyishGoo.py.git

3. In the directory of your local clone, create and activate a virtual environment and install dependencies:

       python -m venv venv
       venv\Scripts\activate.bat
       pip install -r requirements.txt

4. Create a `.env` file that contains your token (replace `abcdefg` with your token):

       echo github_OAuth=abcdefg> .env

5. Run the program:

       python greyishGoo.py
