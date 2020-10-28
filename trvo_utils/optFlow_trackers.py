import cv2
import numpy as np


class PointTrackerLK:
    __optflow = cv2.SparsePyrLKOpticalFlow_create()

    def track(self, prevImg, nextImg, prevPts):
        pts, status, err = self.__optflow.calc(prevImg, nextImg, prevPts, None)
        return pts, status


class PointTrackerFarneback:
    params__ = dict(pyrScale=0.5,
                    numLevels=3,
                    winSize=15,
                    numIters=3,
                    polyN=5,
                    polySigma=1.2,
                    flags=0,
                    fastPyramids=True)
    __optflow = cv2.FarnebackOpticalFlow_create(**params__)

    def track(self, prevImg, nextImg, prevPts):
        flow = self.__optflow.calc(prevImg, nextImg, None)
        pointsAtPixels = prevPts.round().astype(np.int32)
        x = pointsAtPixels[:, 0]
        y = pointsAtPixels[:, 1]
        ptsFlow = flow[(y, x)]
        pts = np.add(prevPts, ptsFlow)
        status = np.ones(len(pts), np.uint8)
        return pts, status


class RectTracker:
    def __init__(self):
        self.pointTracker = PointTrackerLK()

    def track(self, prevImg, nextImg, prevBoxes):
        tl_br = prevBoxes.reshape(-1, 2)  # box to top-left and bottom-right
        pts, status = self.pointTracker.track(prevImg, nextImg, tl_br)
        status = status.reshape(-1, 2)
        status = np.logical_and(status[:, 0], status[:, 1])
        nextBoxes = pts.reshape(-1, 4)
        nextBoxes = nextBoxes[status]  # filter by status - drop boxes with forgotten corners
        return nextBoxes
