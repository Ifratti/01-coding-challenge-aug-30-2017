# Coding challenge 01

## The challenge
Use python to solve a scrambled photo puzzle. Simply clone or download this repository to get started.

## Info
Use the python library, Pillow, to solve the image `puzzle-scramble.png`.
For instructions on install Pillow check out the [install instructions](http://pillow.readthedocs.io/en/3.4.x/installation.html).

[The docs for Pillows API are here.](http://pillow.readthedocs.io/en/3.4.x/reference/index.html)

Run your script with either `python script.py` or `python3 script.py` depending on how you have python setup.

If you still need help setting up python 3 for some reason I some tutorials for getting started.
* [Install on Mac](http://jamesolejar.com/setting-up-python3-and-virtualenv-on-mac)
* [Install on Windows](http://jamesolejar.com/setting-up-python3-and-virtualenv-on-windows)

## Tips
You can get the dimensions of an image with Pillow using the following.
```python
from PIL import Image

# Open the image with Pillow.
img = Image.open('puzzle-scramble.png')

# Assign width and height values.
width, height = img.size

# Expected result: (330, 330)
print(width, height)

```

Create some constants for a 3 X 3 grid.
```python
# For this challenge we are going to assume a 3 X 3 grid.
block_length = width / 3
block_rows = 3
```

Without giving away too much, try seperating the image into a `list` of images which should be 110 X 110 each. You will now have 9 list elements. Using the backtrack method you can randomly select 1 block and check for matches along the border inverse. If you get stuck or have any questions [join the palm beach tech slack](https://palmbeachtech.org/slack/). Our channel is `#event-python-meetup`.
