If you are looking for something to check if you can hear differences between music files in the way that you can provide feedback in the blinded experiment, then this scipt is for you.

Tested on Linux, but should work also for macOS and Windows if you provide a playera working from a command line using `-p player_name`.

Help message:
```
usage: main.py [-h] -f FILES [FILES ...] [-p PLAYER] [-r [REPETITION]] [-e]

Blinded experiment of playing music files.

options:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        files to be played
  -p PLAYER, --player PLAYER
                        player command
  -r [REPETITION], --repeat [REPETITION]
                        how many times files should be played
  -e, --expose          expose file names during playing
```

Example of an usage:
```
--- Round 1 of 2 ---
Playing file 1 of 4... done. Please provide feedback: good
Playing file 2 of 4... done. Please provide feedback: quite good
Playing file 3 of 4... done. Please provide feedback: so so
Playing file 4 of 4... done. Please provide feedback: bad
--- Round 2 of 2 ---
Playing file 1 of 4... done. Please provide feedback: fine
Playing file 2 of 4... done. Please provide feedback: super
Playing file 3 of 4... done. Please provide feedback: could be better
Playing file 4 of 4... done. Please provide feedback: trash

### YOUR FEEDBACK ###

For: 01_-_Marcin_Przybylowicz_-_The_Trail.flac, you've provided:
        good
        super

For: 01_-_Marcin_Przybylowicz_-_The_Trail_lame.mp3, you've provided:
        bad
        trash

For: 01_-_Marcin_Przybylowicz_-_The_Trail.mp3, you've provided:
        so so
        could be better

For: 01_-_Marcin_Przybylowicz_-_The_Trail.ogg, you've provided:
        quite good
        fine
```
