# Steganography

## Binwalk
display and extraction of files
```
binwalk file 
binwalk -e file 
binwalk --dd ".*" 
```

## Foremost
similar like binwalk works well for png

## Exiftool
metadata analyser

## File
file checker

## Strings
strings analyser
```
strings -n 6 file (min lenght of string mentioned)
```

## Steghide
```
steghide info file (check if there any embedded file)
steghide extract -sf file [--passphrase password] (extract file with pass)
```

## Stegsolve
analyse bit planes (hiding in a plainsight)

## Stegsnow
white space steganography (text files only)

## Zsteg
lsb steg (both analyse and extract can be done)

## Pngcheck
check png (useful for header crction challs)

## Stegpy [PNG, BMP, GIF, WebP, WAV]

## ffmpeg
extract info from audio and split audio from video

## Sonic
spectrogram layer analysis (audio only)

## Wavsteg
lsb steg of .wav

## Deepsound
extract hidden files w/wo pass

## DTMF Tones - Dial tones
old phone dial tones (only audio)

## morse
morse code audio

## Digital.jar
extracts circuits from .dig files

## abe 
extracts android backups from .ab files

## Vim encrypted file
extracts files from .vim files

## 4T HIT mail privacy
extracts encoded mails from .bmp files in software


