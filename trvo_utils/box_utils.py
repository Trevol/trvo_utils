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


def expandBox(srcBox, xMargin: Union[int, float], yMargin: Union[int, float] = None,
              relative: bool = False):
    srcBox = np.asarray(srcBox)
    if yMargin is None:
        yMargin = xMargin
    if not relative:
        return srcBox + [-xMargin, -yMargin, xMargin, yMargin]
    else:  # float margin
        marginWH = boxSizeWH(srcBox) * [xMargin, yMargin]
        margins = np.append(-marginWH, marginWH)
        return srcBox + margins


def boxSizeWH(box):
    # p1 - p2
    return box[[2, 3]] - box[[0, 1]]


def pointInBox(box, pt):
    # pt_is_in_box = x1 <= x <= x2 and y1 <= y <= y2
    return box[0] <= pt[0] <= box[2] and box[1] <= pt[1] <= box[3]
