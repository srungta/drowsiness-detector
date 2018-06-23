# drowsiness-detector

## Intent
Detecting drowsiness of eyes using open cv :)

## Inspiration
This code is based on the blog post [here](https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/). The inspiration to do this comes from [akshaybahadur21](https://github.com/akshaybahadur21/Drowsiness_Detection)'s github repo.

## Overview

The code flow is simple:
- Get a camera feed.
- In each frame, find the eyes.
- The height to width ratio of the eye tells us whether how open or closed it is.
- If the ratio is `high`, that means the eyes are `more open` and vice versa.
- if the ration goes below a threshold (`EYE_AR_THRESHOLD`), we consider the eyes as closed.
- if the eyes remain closed for `EYE_AR_CONSECUTIVE_FRAMES` number of frames, we sound the alarm.

And that's it.

## How to run
+ Clone the repo.
+ Run ` pip install -r requirements.txt` in the directory.

[_I recommend creating separate environments [like miniconda env] for this installations_]

+ Run `python detector.py`