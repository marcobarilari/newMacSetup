# Set up of a new mac step by step

- [Set up of a new mac step by step](#set-up-of-a-new-mac-step-by-step)
  - [BACKUP to a HD](#backup-to-a-hd)
  - [ERASE](#erase)
  - [INSTALL Priority 1](#install-priority-1)
    - [oh-my-zsh](#oh-my-zsh)
    - [homebrew](#homebrew)
    - [htop](#htop)
    - [chrome](#chrome)
    - [xcode](#xcode)
    - [xquartz](#xquartz)
    - [git](#git)
    - [get this repo locally if not copied from the previous mac `github` folder ;)](#get-this-repo-locally-if-not-copied-from-the-previous-mac-github-folder-)
    - [VScode (check set up below)](#vscode-check-set-up-below)
    - [dropbox](#dropbox)
    - [python](#python)
    - [datalad](#datalad)
    - [UCLouvain openVPN](#uclouvain-openvpn)
    - [FileZilla](#filezilla)
    - [Xcode compiler](#xcode-compiler)
    - [setups](#setups)
      - [finder](#finder)
      - [ssh](#ssh)
      - [git/github/gin](#gitgithubgin)
      - [](#)
  - [Priority 2](#priority-2)
    - [tree](#tree)
    - [git kraken](#git-kraken)
    - [discord](#discord)
    - [googledrive](#googledrive)
    - [openVPN Connect](#openvpn-connect)
    - [MacsFanControl](#macsfancontrol)
    - [copyclip](#copyclip)
    - [monitor display lite](#monitor-display-lite)
    - [docker](#docker)
    - [anaconda](#anaconda)
    - [audacity](#audacity)
    - [caffeine (maybe not necessary)](#caffeine-maybe-not-necessary)
    - [magnet](#magnet)
    - [logi options](#logi-options)
    - [todoist](#todoist)
    - [pomodone](#pomodone)
    - [spotify](#spotify)
    - [teams](#teams)
    - [365 office (installs: Excel, Word, Powerpoint, OneNote, OneDrive)](#365-office-installs-excel-word-powerpoint-onenote-onedrive)
    - [zoom](#zoom)
    - [zotero](#zotero)
    - [grammarly](#grammarly)
    - [nordvpn](#nordvpn)
    - [timerRH](#timerrh)
    - [disk inventory x](#disk-inventory-x)
  - [Priority 3](#priority-3)
    - [VIM](#vim)
    - [itksnap http://www.itksnap.org/download/snap/register.php?link=13393\&root=nitrc](#itksnap-httpwwwitksnaporgdownloadsnapregisterphplink13393rootnitrc)
    - [freesurfer https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads](#freesurfer-httpssurfernmrmghharvardedufswikirel7downloads)
    - [fsl](#fsl)
    - [laynii https://github.com/layerfMRI/LAYNII](#laynii-httpsgithubcomlayerfmrilaynii)
    - [ants](#ants)
    - [afni installation guide](#afni-installation-guide)
    - [R (if not installed by afni)](#r-if-not-installed-by-afni)
    - [OR](#or)
    - [Rstudio](#rstudio)
    - [matlab (from ...)](#matlab-from-)
    - [Microsoft NTFS Tuxera](#microsoft-ntfs-tuxera)
    - [tor-browser](#tor-browser)
    - [firefox](#firefox)
    - [whatsapp](#whatsapp)
    - [telegram](#telegram)
    - [spyder](#spyder)
    - [inkscape](#inkscape)
    - [gimp](#gimp)
    - [fig](#fig)
    - [vlc](#vlc)
    - [trashme (from ...)](#trashme-from-)
    - [printers at uclouvain](#printers-at-uclouvain)
  - [P4](#p4)
    - [octave](#octave)
    - [psychopy](#psychopy)
    - [ibettercharge](#ibettercharge)
    - [visrtual box](#visrtual-box)
  - [In-App setup](#in-app-setup)
    - [VScode](#vscode)
      - [Extensions](#extensions)
    - [matlab](#matlab)
  - [EXTRA](#extra)

## BACKUP to a HD

- startup matlab file `startup.m`
- mendeley
- zotero (not necessary anymore since I pay for extra space)
- photos (not necessary since it is synced via iCloud)
- onetab 
- logitech mouse (screenshots of configurations)
- dock composition (screenshot)
- github folders
- `~/.ssh`
- `~/.zshrc`
- stickyes contents
- music folder 
- download folder
  
## ERASE

check this:

- [What to do before you sell, give away or trade in your Mac](https://support.apple.com/en-au/HT201065)
- [Erase your Mac and reset it to factory settings](https://support.apple.com/en-us/HT212749)
- [Reinstall macOS](https://support.apple.com/en-au/guide/mac-help/mchlp1599/13.0/mac/13.0)

## INSTALL Priority 1

### oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

then close and reopen the terminal

### homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### htop

```bash
brew install htop
```

### chrome

```bash
brew install --cask google-chrome
```

### xcode

```bash
xcode-select --install
```

### xquartz

```bash
brew install --cask xquartz
```

### git

```bash
git --version

brew install git
```

### get this repo locally if not copied from the previous mac `github` folder ;)

```bash
mkdir ~/GitHub && cd ~/GitHub && git clone https://github.com/marcobarilari/newMacSetup.git
```

:bangbang: better to `sudo reboot` now :bangbang:

### VScode (check set up below)

```bash
brew install --cask visual-studio-code
```

check below in `EXTRA` a list of extensions to install, to install them automatically you only need to sign in.

- Set the schortcut 'option' + 'cmd' + 'enter' to run the selected/line at cursos code in the terminal see [here](https://stackoverflow.com/questions/49085609/visual-studio-code-shortcut-run-command-in-terminal)

### dropbox

```bash
brew install --cask dropbox
```

### python

consider [to set up a virtual env for python3](https://matt-wxw.medium.com/setup-python-3-on-macos-cf48f30bec3b#:~:text=The%20default%20Python%20version%20on,is%20also%20on%20the%20system.&text=However%2C%20it%20is%20not%20recommended.)

```bash
# check if python 3 is installed
python3
```

### datalad

```bash
brew install datalad
```

### UCLouvain openVPN

Check [here](https://uclouvain.atlassian.net/servicedesk/customer/article/564985915)

### FileZilla

[link](https://filezilla-project.org/download.php?show_all=1)

### Xcode compiler 

https://apps.apple.com/it/app/xcode/id497799835?l=en&mt=12

### setups

#### finder

  - [3 finger drag and drop](https://support.apple.com/en-us/HT204609)
  - [path at bottom](https://support.apple.com/en-au/guide/mac-help/mchlp1774/mac#:~:text=On%20your%20Mac%2C%20click%20the,bottom%20of%20the%20Finder%20window)

#### ssh

run this to create a new `.ssh` directory and add ssh addresses to it

```bash
ssh-keygen
```

#### git/github/gin

- https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git

- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

#### 

## Priority 2

### tree

```
brew install tree
```

### git kraken

```bash
brew install --cask gitkraken
```

### discord

```bash
brew install --cask discord
```

### googledrive

```bash  
brew install --cask google-drive
```

### openVPN Connect

```bash  
brew install --cask openvpn-connect
```

### MacsFanControl

```bash
brew install --cask macs-fan-control
```

### copyclip
  
https://apps.apple.com/it/app/copyclip-clipboard-history/id595191960?l=en&mt=12

### monitor display lite
  
<https://apps.apple.com/it/app/monitorcontrol-lite/id1595464182?l=en&mt=12>

### docker 

```bash 
brew install --cask docker
```

### anaconda 

```bash
brew install --cask anaconda
```

### audacity 

```bash
brew install --cask audacity
```

### caffeine (maybe not necessary)

```bash
brew install --cask caffeine
```

### magnet 

https://apps.apple.com/it/app/magnet/id441258766?l=en&mt=12


### logi options 

https://download01.logi.com/web/ftp/pub/techsupport/optionsplus/logioptionsplus_installer.zip

### todoist 

```bash
brew install --cask todoist
```

### pomodone 

```bash
brew install --cask pomodone
```

### spotify 

```bash
brew install --cask spotify
```

### teams 

```bash
brew install --cask microsoft-teams
```

### 365 office (installs: Excel, Word, Powerpoint, OneNote, OneDrive)

```bash
brew install --cask microsoft-office
```

### zoom 

```bash
brew install --cask zoom
```

### zotero 

```bash
brew install --cask zotero
```

### grammarly 

```bash
brew install --cask grammarly-desktop
```

### nordvpn 

```bash 
brew install --cask nordvpn
```

### timerRH 

[appstore](https://apps.apple.com/it/app/timer-rh/id929960914?l=en&mt=12)

### disk inventory x

```bash
brew install --cask disk-inventory-x
```

## Priority 3


### VIM

```bash
brew install vim
```


### itksnap <http://www.itksnap.org/download/snap/register.php?link=13393&root=nitrc>
  
### freesurfer <https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads>
  - video tutorial <https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall?action=AttachFile&do=view&target=installFS_demo.mp4>

### fsl 

https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation

### laynii <https://github.com/layerfMRI/LAYNII>

### ants
  - precompiled <https://github.com/stnava/ANTs/zipball/master>
  - to compile <https://github.com/ANTsX/ANTs/wiki/Compiling-ANTs-on-Linux-and-Mac-OS>


### afni [installation guide](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/steps_macOS_12_Intel.html)

  - this also installs R

### R (if not installed by afni)
  - via afni... at the moment the latest version is 4.x.x but afni seems to prefer `R-3.6.3`

  ### OR

```bash
brew install r
```

OR for afni at this [link](https://cran-archive.r-project.org/bin/macosx/el-capitan/base/R-3.6.3.nn.pkg)

### Rstudio

```bash
brew install --cask rstudio
```

### matlab (from ...)

- set up bash fucntion (see [here](https://github.com/cpp-lln-lab/labMONSTER?tab=readme-ov-file#matlab-2018a))

### Microsoft NTFS Tuxera 

```bash
brew install --cask tuxera-ntfs
```

### tor-browser

```bash
brew install --cask tor-browser
```

### firefox 

```bash
brew install --cask firefox
```

### whatsapp 

```bash
brew install --cask whatsapp
```

### telegram

```bash
brew install --cask telegram
```

### spyder 

```bash
brew install --cask spyder
```

### inkscape 

```bash
brew install --cask inkscape
```

### gimp 

```bash
brew install --cask gimp
```

### fig 

```bash
brew install --cask fig
```

### vlc 

```bash
brew install --cask vlc
```

### trashme (from ...)

### printers at uclouvain

## P4

 latek 

```bash
brew install --cask mactex
```

### octave 

```bash
brew install octave
```

### psychopy 

```bash
brew install --cask psychopy
```

### ibettercharge 

```bash 
brew install --cask ibettercharge
```

### visrtual box

```bash
brew install --cask virtualbox
```

- obsedian brew install --cask obsidian
- boinc manager brew install --cask boinc
- photoshop (from ...)
- illustrator (from ...)
- mattermost brew install --cask mattermost
- studio lego brew install --cask bricklink-studio



- mendely brew install --cask mendeley
- bear <https://apps.apple.com/it/app/bear-markdown-notes/id1091189122?l=en&mt=12>
- slack brew install --cask slack
- selfcontrol brew install --cask selfcontrol
- folx go + brew install --cask folx
- torbrowser brew install --cask tor-browser
- ink2go (from ...)
- element brew install --cask element
- mricron <https://github.com/neurolabusc/MRIcron>
- jasp brew install --cask jasp
- freespace tab <https://macdownload.informer.com/freespace-tab/>
- praat brew install --cask praat

## In-App setup

### VScode

#### Extensions

### matlab

bspmview
cosmomvpa
spm12
fraridge
libsvm_325
PTB
tapas

## EXTRA

- Extension to install:
  - Auto-Open Markdown Preview
  - Color Highlight
  - Excel Viewer
  - Git Graph
  - GitHub Copilot
  - GitHub Copilot C
  - Git Lens
  - json
  - Jupiter
  - Markdown All in One
  - MATLAB
  - NeuroViewer
  - Pretier - Code formatter
  - Prettify JSON
  - Pylance
  - Python
  - Python Debugger
  - R
  - R Markdown All in One
  - Remote SSH
  - Sublime VSCode Theme
  - Power Mode
  - Vim