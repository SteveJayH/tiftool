<div align="center"><img src="images/bannertiftoo.png" height="150px"/></div>

<h2 align="center">tiftool: A Python package for Microscopy tif images</h2>

The package for dealing tif stack image. Oriented for Microscopy image, offering useful processing. **Under construction, I'll make description site and more functions, maybe for 2020.08.**

<div align="center">
    <a href="https://pypi.org/project/tiftool/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/tiftool?color=blue">
    </a>
</div>

## Concept

### Stack object

Main concept of tiftool is **Stack object**. This object carries your 3d data from .tif file as 'torch.Tensor' or 'numpy.ndarray'. By using stack object, you can conduct numerous processes; MIP(Maximum Intensity Projection), Find center z-plane, etc. This package is made to help research, Fluorescent Microscopy(WideField, XLFM(eXtended field of view LFM), etc).

### HyperStack object

**Under construction** Similar as ImageJ, I'll make HyperStack object which can consider 'time'. It will contain 4-D data, (T, X, Y, Z).

## Installation

### pip

tiftool can installed via pip. Simply run this code by terminal.
```bash
pip install tiftool
```
Latest version is **0.2.1**. If you have older version of tiftool, run this code to update. I strongly recommend to use latest version.
```bash
pip install tiftool -U
```
***not recommended*** If you want to force ignore all dependencies, you can use --no-dependencies switch of pip [stackoverflow](https://stackoverflow.com/questions/12759761/python-pip-force-install-ignoring-dependencies).
```bash
pip install --no-dependencies tiftool
```
tiftool might not work well if your environment doesn't have requirements...

### wheel

If upper method does not work, you can install tiftool via wheel(.whl) file. Install wheel from this [.whl](https://files.pythonhosted.org/packages/c9/6d/d8650651863d369bdf1e66b6d77b3ba8974ae30e93638d7c2457f7563f7c/tiftool-0.2.1-py3-none-any.whl) link.
```bash
pip install yourpath/...whl
```

## Running tiftool

### Basic things using stack object

```python
import tiftool.stack as st

larva = st.Stack().open("larva.tif").to_tensor()  # Change to torch.tensor, default data is numpy array.
raw_data = larva._data  # You can access the raw data inside Stack() object.
print(raw_data.size())  # torch.size([1098, 890, 64]) (x, y, z)

MIP = larva.mip_3d()  # Return Maximum Intensity Project for x, y, z axis
MIP.show()  # Show image using matplotlib
MIP.write("mip_larva.tif")  # write at your input path
```
See [tiftool docs](https://stevejayh.github.io/tiftool/) for more details.  (**Not constructed**)

## Issues & Contribution

I appreciate for all [issues](https://github.com/SteveJayH/tiftool/issues) and contributions. You can use 'issues' tab, 'Pull request' tab, or [e-mail](mailto:jay0118@yonsei.ac.kr) me! I want to develop this package as a **powerful toolkit for microscopy data researcher** and if you mind, contribute with me! :smiley:

## LICENSE

This package follows MIT LICENSE.
