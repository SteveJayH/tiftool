import copy
import numpy as np
import torch
from PIL import Image
from tifffile import imwrite
import matplotlib.pyplot as plt
from .functional import mip_x, mip_y, mip_z
from .sub_classes.IndexTracker import IndexTracker


class Stack:
    def __init__(self):
        """
        self._data will contain data.
        Stack object works as "Rocket".
        Stack object allows you to conduct many things
        with carrying your data.
        """
        self._data = None

    def __add__(self, other):
        """
        To allow object add as adding data inside
        """
        if isinstance(other, type(self)):
            self._data = self._data + other._data
        else:
            self._data = self._data + other

    def __mul__(self, other):
        """
        To allow object muliplication as data inside
        """
        if isinstance(other, type(self)):
            self._data = self._data * other._data
        else:
            self._data = self._data * other

    def open(self, path):
        if not isinstance(path, str):
            raise ValueError("path need to be string")
        if any(path.split(".")[-1] in s for s in [".tif", ".tiff"]):
            pic = Image.open(path)
            w, h = pic.size
            np_array = np.zeros((w, h, pic.n_frames))
            for i in range(pic.n_frames):
                pic.seek(i)
                np_array[:, :, i] = np.array(pic).astype(np.double).T
            self._data = np_array
        else:
            raise ValueError("Only accept .tif, .tiff files. Check path.")

        return self

    def data(self):
        return self._data

    """
    **Deprecated**
    def _data(self, data):
        self._data = data
        return self
    """

    def data_(self, data):
        self._data = data

    def to_tensor(self):
        self._data = torch.as_tensor(self._data).float()
        return self

    def to_tensor_(self):
        self._data = torch.as_tensor(self._data).float()

    def to_numpy(self):
        self._data = self._data.numpy()
        return self

    def to_numpy_(self):
        self._data = self._data.numpy()

    def mip_3d(self, z_exp=1, padding=10):
        new = copy.deepcopy(self)

        flag = False
        if isinstance(self._data, np.ndarray):
            flag = True
            self.to_tensor_()

        def tile(a, dim, n_tile):
            init_dim = a.size(dim)
            repeat_idx = [1] * a.dim()
            repeat_idx[dim] = n_tile
            a = a.repeat(*(repeat_idx))
            order_index = torch.LongTensor(np.concatenate([init_dim * np.arange(n_tile) + i for i in range(init_dim)]))
            return torch.index_select(a, dim, order_index)

        x = self._data.size(0) + padding + self._data.size(2) * z_exp
        y = self._data.size(1) + padding + self._data.size(2) * z_exp
        tmp = torch.zeros(x, y, 1)

        tmp.fill_(self._data.max())

        tmp[0:self._data.size(0), 0:self._data.size(1), :] = mip_z(self).data()
        tmp[0:self._data.size(0), self._data.size(1)+padding:tmp.size(1), :] = tile(mip_x(self).data().squeeze(2), 1, z_exp).unsqueeze(2)
        tmp[self._data.size(0)+padding:tmp.size(0), 0:self._data.size(1), :] = tile(mip_y(self).data().squeeze(2), 0, z_exp).unsqueeze(2)

        new.data_(tmp)

        if flag:
            new.to_numpy_()

        return new

    def xlfm_encoding(self, impulses, x_l, y_l, z_l):
        new = copy.deepcopy(self)
        flag = False
        if isinstance(self._data, np.ndarray):
            flag = True
            self.to_tensor_()

        tmp = torch.zeros(x_l, y_l, z_l)
        q = 0

        for i in range(impulses.data().size(0)):
            for j in range(impulses.data().size(1)):
                if impulses.data()[i, j, 0] != 0:
                    tmp[:, :, q] = self.data()[i-x_l//2:i+(x_l-x_l//2), j-y_l//2:j+(y_l-y_l//2), 0]
                    q += 1
        new.data_(tmp)

        if flag:
            new.to_numpy_()

        return new

    def write(self, path, imagej=False):
        if isinstance(self._data, torch.Tensor):
            imwrite(path, self._data.permute(2, 1, 0).cpu().numpy(), dtype='f2', imagej=imagej)
        elif isinstance(self._data, np.ndarray):
            imwrite(path, np.transpose(self._data.astype('float32'), [2, 1, 0]), dtype='f2', imagej=imagej)
            # TODO permute???
        else:
            raise ValueError("Check type of stack")

    def show(self):
        if isinstance(self._data, torch.Tensor):
            thickness = self._data.size(2)
            if thickness == 1:
                plt.imshow(self._data.permute(1, 0, 2).squeeze(2), cmap='gray')
                plt.show()
            else:
                fig, ax = plt.subplots(1, 1)
                tracker = IndexTracker(ax, self._data.permute(1, 0, 2))
                fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
                plt.show()
        elif isinstance(self._data, np.ndarray):
            # TODO need to change x and y
            thickness = self._data.shape[2]
            if thickness == 1:
                plt.imshow(self._data.squeeze(2).T, cmap='gray')
                plt.show()
            else:
                fig, ax = plt.subplots(1, 1)
                print(self._data.shape)
                tracker = IndexTracker(ax, self._data)
                fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
                plt.show()
        else:
            raise ValueError("Check type of stack, need to be np.ndarray or torch.Tensor")
