'''
`genesis` will firstly install `homebrew` and then `git` in order to clone this repo 
and retrieve everything needed to install a general new macOS einvironment
'''

# os.system('')
# os.system('echo ""')

import os

homeDir = os.system('cd ~')

os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')

if os.system('python3 --version'):

	os.system('echo "I did not find python3, let me install it"')
	os.system('brew install python3')

os.system('echo "Installing git"')
os.system('brew install git')



os.system('git config --global user.name "marcobarilari"')

githubUserName = os.system('git config --global user.name')

os.system('echo "your git is set with %s"', githubUserName)
