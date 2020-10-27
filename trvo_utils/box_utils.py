from typing import Union, Tuple

import numpy as np


def scaleBoxes(boxes, scale):
    if scale == 1:
        return boxes
    return [scaleBox(b, scale) for b in boxes]


def scaleBox(box, scale):
    if scale == 1:
        return box
    if isinstance(box, np.ndarray):
        return box * scale
    x1, y1, x2, y2 = box
    return x1 * scale, y1 * scale, x2 * scale, y2 * scale


def expandBox(srcBox, margin: Union[int, float]):
    srcBox = np.asarray(srcBox)
    if isinstance(margin, int):
        return srcBox + [-margin, -margin, margin, margin]
    else:  # float margin
        marginWH = boxSizeWH(srcBox) * margin
        margins = np.append(-marginWH, marginWH)
        return srcBox + margins


def boxSizeWH(box):
    # p1 - p2
    return box[[2, 3]] - box[[0, 1]]
