# Barrel Bot
### [@mlb_barrels](https://twitter.com/mlb_barrels)
A twitter bot that tweets the hardest hit baseball in MLB each day, complete with video and relevent statistics. Created with pybaseball, tweepy, and a Raspberry Pi 3 (formerly on AWS Lambda).

## Project Outline
- The source code is located in ./function, including `send_tweet.py`, the entrypoint for the function.
- `test.py` returns the information in the console, along with video links from Baseball Savant.

## Some Notes
 You'll notice that the source code includes a fork of [pybaseball](https://github.com/jldbc/pybaseball), a great library by James LeDoux. I made a fork because I had to remove a significant portion of its dependencies (matplotlib, pyarrow, scipy), in order to stay within the 250 MB limit. In addition, with Lambda having a read-only filesystem, pybaseball's caching functions would not work.


## Example
<img src="branding/Example Tweet.jpg" alt="Example Tweet" width="400"/>

https://user-images.githubusercontent.com/38846646/173471531-6dd09169-1404-4536-aa03-c71c16944126.mp4
