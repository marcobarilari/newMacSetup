# MacSetup
Collection of info, app and script to automate the setup of my mac pc in a new or renewed machine

## Step 1 - Clean install of the chosen MacOs

### Download and prepare for new installation

see [here](https://bootableinstaller.com/macos/#macos)

## Step 2 - Prepare for the automatic set up with basic tools 

### XCode

It is necessary for eg octave, probably not possible to install it via the terminal (maybe with `mas` but it itself needs it so... but see [here](https://apple.stackexchange.com/questions/75684/installing-xcode-via-command-line))

If you need an older version which is not the one on the mac app store (eg Sierra needs 9.2), check [here](https://developer.apple.com/download/more/)

### Homebrew

[homebrew](https://brew.sh/) (will install the `Command Line Tools`)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

mac settings

git and clone this repo



pip3

python3



########################### OLD ###########################

## Manual installation

- [ ]

## Automatic installation

running `BarcoMacSetup.tool` on the terminal it will install:

- [ ]


## to add with automatic installation

- [ ] homebrew  

https://thehomeofthefuture.com/how-to/use-homebrew-for-macos/

## to add with manual installation

- [ ] Matlab


---

## list of the stuff installed before the 29th aug 2020 on my computer

### general list
- git

### JustMac

#### via homebrew

- tree `brew install tree` [more info here](List A Directory With Tree Command On Mac OS X)


## list of the stuff I am installing since 29th aug 2020 on my computer

### JustMac

### NeuroMac

#### via homebrew

- git-annex `brew install git-annex`

#### via pip3 (dependency: 'python')

- data-lad `pip3 install datalad~=0.12` (dependency: 'git', 'git-annex')

> If this results in a permission denied error, install DataLad into a user’s home directory: `$ pip3 install --user datalad~=0.12`
