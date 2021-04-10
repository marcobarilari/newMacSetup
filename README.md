# MacSetup
Collection of info, app and script to automate the setup of my Macintosh in a new or semi-new machine

## Step 1 - Clean install of the chosen MacOs

### Download the macOs

[Yosemite](http://updates-http.cdn-apple.com/2019/cert/061-41343-20191023-02465f92-3ab5-4c92-bfe2-b725447a070d/InstallMacOSX.dmg) downloader through Safari

### Prepare the bootable USB

see [here](https://bootableinstaller.com/macos/#macos)


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
