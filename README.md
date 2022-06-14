# Barrel Bot
### [@mlb_barrels](https://twitter.com/mlb_barrels)
A twitter bot that tweets the hardest hit baseball in MLB each day, complete with video and relevent statistics. Created with pybaseball, tweepy, and AWS Lambda.

## Project Outline
- The source code is located in ./lambda_deploy, including `lambda_function.py`, the entrypoint for .
- `test.py` returns the information in the console, along with video links from Baseball Savant.

## Some Notes
 You'll notice that [pybaseball](https://github.com/jldbc/pybaseball), a great library by James LeDoux, is not a dependency but a part of the source code. This was done because I had to remove a significant portion of its dependencies (matplotlib, pyarrow), in order to stay within the 250 MB limit. In addition, with Lambda having a read-only filesystem, pybaseball's caching functions and multiprocessing model would not work.


## Example
<img src="branding/Example Tweet.jpg" alt="Example Tweet" width="400"/>

https://user-images.githubusercontent.com/38846646/173471531-6dd09169-1404-4536-aa03-c71c16944126.mp4
