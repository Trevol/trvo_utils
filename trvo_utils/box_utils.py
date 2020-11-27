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


def boxCenter(xyxyBox):
    # pt = (x2+x1)/2, (y2+y1)/2
    return (xyxyBox[2] + xyxyBox[0]) / 2, (xyxyBox[3] + xyxyBox[1]) / 2


def xyxy2xywh(xyxy):
    x1 = xyxy[0]
    y1 = xyxy[1]
    x2 = xyxy[2]
    y2 = xyxy[3]
    w = x2 - x1
    h = y2 - y1
    xywh = np.empty_like(xyxy)
    xywh[0] = x1
    xywh[1] = y1
    xywh[2] = w
    xywh[3] = h
    return xywh


def xywh2xyxy(xywh):
    x = xywh[0]
    y = xywh[1]
    w = xywh[2]
    h = xywh[3]
    xyxy = np.empty_like(xywh)
    xyxy[0] = x
    xyxy[1] = y
    xyxy[2] = x + w
    xyxy[3] = y + h
    return xyxy
