# Set up oif a new mac step by step

## ERASE

check this:

- [What to do before you sell, give away or trade in your Mac](https://support.apple.com/en-au/HT201065)
- [Erase your Mac and reset it to factory settings](https://support.apple.com/en-us/HT212749)
- [Reinstall macOS](https://support.apple.com/en-au/guide/mac-help/mchlp1599/13.0/mac/13.0)

## BACKUP from `HD_HOME`

- startup matlab
- mendeley
- zotero
- photos
- onetab
- bear
- logitech mouse
- dock composition
- finder tricks (3 fingers, path at bottom, drag and drop)
  - 3 finger <https://support.apple.com/en-us/HT204609>
  - path at bottom <https://support.apple.com/en-au/guide/mac-help/mchlp1774/mac#:~:text=On%20your%20Mac%2C%20click%20the,bottom%20of%20the%20Finder%20window>.
- github folders

## Priority 1

### oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### htop

```bash
brew install htop
```

### tree

```
brew install tree
```

### chrome

```bash
brew install --cask google-chrome
```

### git

```bash
git --version

brew install git
```

set up git/github (config + ssh)



### get this repo locally ;)

```bash
mkdir ~/GitHub && cd ~/GitHub && git clone https://github.com/marcobarilari/newMacSetup.git
```

### xcode

```bash
xcode-select --install
```

### xquartz

```bash
brew install --cask xquartz
```

:bangbang: better to `sudo reboot` now :bangbang:

### VIM

```bash
brew install vim
```

### VScode (check set up below)

```bash
brew install --cask visual-studio-code
```

- Set the schortcut 'option' + 'cmd' + 'enter' to run the selected/line at cursos code in the terminal see [here](https://stackoverflow.com/questions/49085609/visual-studio-code-shortcut-run-command-in-terminal)

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

## Priority 2

<<<<<<< HEAD
- FileZilla

[link](https://filezilla-project.org/download.php?show_all=1)

- Xcode compiler 
=======
### Xcode compiler 
>>>>>>> 29bf3bb (add vscode extensions)

https://apps.apple.com/it/app/xcode/id497799835?l=en&mt=12

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

https://download01.logi.com/web/ftp/pub/techsupport/options/options_installer.zip

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
brew install --cask grammarly
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
