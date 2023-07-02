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

## P1

- homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- htop

```bash
brew install htop
```

- chrome

```bash
brew install --cask google-chrome
```

- git

```bash
git --version

brew install git
```

- get this repo locally ;)

```bash
mkdir ~/GitHub && cd ~/GitHub && git clone https://github.com/marcobarilari/newMacSetup.git
```

- xcode

```bash
xcode-select --install
```

- xquartz

```bash
brew install --cask xquartz
```

:bangbang: better to `sudo reboot` now :bangbang:

- VIM

```bash
brew install vim
```

- VScode (check set up below)

```bash
brew install --cask visual-studio-code
```

- dropbox

```bash
brew install --cask dropbox
```

- python

consider [to set up a virtual env for python3](https://matt-wxw.medium.com/setup-python-3-on-macos-cf48f30bec3b#:~:text=The%20default%20Python%20version%20on,is%20also%20on%20the%20system.&text=However%2C%20it%20is%20not%20recommended.)

```bash
# check if python 3 is installed
python3
```

- datalad

```bash
brew install datalad
```

## P2

- afni [installation guide](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/steps_macOS_12_Intel.html)
  - this also installs R

- R (if not installed by afni)
  - via afni... at the moment the latest version is 4.x.x but afni seems to prefer `R-3.6.3`

  - OR

```bash
brew install r
```

OR for afni at this [link](https://cran-archive.r-project.org/bin/macosx/el-capitan/base/R-3.6.3.nn.pkg)

- Rstudio

```bash
brew install --cask rstudio
```

- matlab (from ...)

- git kraken

```bash
brew install --cask gitkraken
```

- discord

```bash
brew install --cask discord
```

- onedrive brew install --cask onedrive

- googledrive brew install --cask google-drive

- openVPN Connect brew install --cask openvpn-connect

- MacsFanControl brew install --cask macs-fan-control

- copyclip <https://apps.apple.com/it/app/copyclip-clipboard-history/id595191960?l=en&mt=12>

- monitor display lite <https://apps.apple.com/it/app/monitorcontrol-lite/id1595464182?l=en&mt=12>

- docker brew install docker
- virtual box brew install --cask virtualbox
- anaconda brew install --cask anaconda
- audacity brew install --cask audacity
- logi options <https://download01.logi.com/web/ftp/pub/techsupport/options/options_installer.zip>
- itksnap <http://www.itksnap.org/download/snap/register.php?link=13393&root=nitrc>
- freesurfer <https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads>
  - video tutorial <https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall?action=AttachFile&do=view&target=installFS_demo.mp4>
- fsl <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation>
- laynii <https://github.com/layerfMRI/LAYNII>
- ants
  - precompiled <https://github.com/stnava/ANTs/zipball/master>
  - to compile <https://github.com/ANTsX/ANTs/wiki/Compiling-ANTs-on-Linux-and-Mac-OS>
- caffeine brew install --cask caffeine
- magnet <https://apps.apple.com/it/app/magnet/id441258766?l=en&mt=12>

## P3

- timerRH [appstore](https://apps.apple.com/it/app/timer-rh/id929960914?l=en&mt=12)

- todoist brew install --cask todoist
- Microsoft NTFS Tuxera brew install --cask tuxera-ntfs
- pomodone brew install --cask pomodone
- firefox brew install --cask firefox
- spotify brew install --cask spotify
- whatsapp brew install --cask whatsapp
- telegram brew install --cask telegram
- teams brew install --cask microsoft-teams
- 365 office brew install --cask microsoft-office
- zoom brew install --cask zoom
- zotero brew install --cask zotero
- grammarly brew install --cask grammarly
- nordvpn brew install --cask nordvpn
- trashme (from ...)
- fig brew install --cask fig
- latek brew install --cask mactex
- octave brew install octave
- psychopy brew install --cask psychopy
- spyder brew install --cask spyder
- ibettercharge brew install --cask ibettercharge
- printers at uclouvain

## P4

- obsedian brew install --cask obsidian
- boinc manager brew install --cask boinc
- photoshop (from ...)
- illustrator (from ...)
- gimp brew install --cask gimp
- mattermost brew install --cask mattermost
- studio lego brew install --cask bricklink-studio
- inkscape brew install --cask inkscape
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
