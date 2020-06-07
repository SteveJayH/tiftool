<div align="center"><img src="https://github.com/SteveJayH/tiftool/blob/master/images/bannertiftoo.png" height="150px"/></div>

<h2 align="center">tiftool: A Python package for Microscopy tif images</h2>

The package for dealing tif stack image. Oriented for Microscopy image, offering useful processing. **Under construction, I'll make description site and more functions, maybe for 2020.07.**

## Installation

### pip

tiftool can installed via pip. Simply run this code by terminal.
```
pip install tiftool
```
Latest version is **0.1.4**. If you have older version of tiftool, run this code to update. I strongly recommend to use latest version.
```
pip install tiftool -U
```

## Running tiftool

### Basic things using stack object

```python
import tiftool.stack as st

larva = st.Stack().open("larva.tif").to_tensor()  # Change to torch.tensor, default data is numpy array.
raw_data = larva._data  # You can access the raw data inside Stack() object.
print(raw_data.size())  # torch.size([1098, 890, 64]) (x, y, z)

MIP = a.mip_3d()  # Return Maximum Intensity Project for x, y, z axis
MIP.show()  # Show image using matplotlib
MIP.write("mip_larva.tif")  # write at your input path
```
See [tiftool docs](https://github.com/SteveJayH/tiftool/) for more details.  (**Not constructed**)

## LICENSE
