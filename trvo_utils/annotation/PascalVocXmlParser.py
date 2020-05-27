import os
import numpy as np
from xml.etree.ElementTree import parse


class PascalVocXmlParser(object):
    """Parse annotation for 1-annotation file """

    def __init__(self, annFile):
        self._root = parse(annFile).getroot()

    def filename(self):
        """
        # Args
            annotation_file : str
                annotation file including directory path

        # Returns
            filename : str
        """
        return self._root.find("filename").text

    def labels(self):
        """
        # Args
            annotation_file : str
                annotation file including directory path

        # Returns
            labels : list of strs
        """
        labels = []
        obj_tags = self._root.findall("object")
        for t in obj_tags:
            labels.append(t.find("name").text)
        return labels

    def boxes(self):
        """
        # Args
            annotation_file : str
                annotation file including directory path

        # Returns
            bbs : 2d-array, shape of (N, 4)
                (x1, y1, x2, y2)-ordered
        """
        bbs = []
        obj_tags = self._root.findall("object")
        for t in obj_tags:
            box_tag = t.find("bndbox")
            x1 = box_tag.find("xmin").text
            y1 = box_tag.find("ymin").text
            x2 = box_tag.find("xmax").text
            y2 = box_tag.find("ymax").text
            box = np.float32([x1, y1, x2, y2])
            bbs.append(box)
        return bbs

    def annotation(self):
        return self.boxes(), self.labels()
