class BBox:
    @staticmethod
    def yolo2voc(cx_norm, cy_norm, w_norm, h_norm, imgSize):
        imH, imW = imgSize
        cx = cx_norm * imW
        cy = cy_norm * imH
        w = w_norm * imW
        h = h_norm * imH

        x1 = cx - w / 2
        y1 = cy - h / 2
        x2 = cx + w / 2
        y2 = cy + h / 2
        return x1, y1, x2, y2

    @staticmethod
    def yolo2voc_box(yoloBox, imgSize):
        cx_norm, cy_norm, w_norm, h_norm = yoloBox
        return BBox.yolo2voc(cx_norm, cy_norm, w_norm, h_norm, imgSize)

    @staticmethod
    def yolo2voc_boxes(yoloBoxes, imgSize):
        toVoc = BBox.yolo2voc_box
        return [toVoc(b, imgSize) for b in yoloBoxes]

    @staticmethod
    def voc2yolo(vocBox, imgSize):
        x1, y1, x2, y2 = vocBox
        imgH, imgW = imgSize
        cxNorm = (x1 + x2) / 2 / imgW  # cx / imgW
        cyNorm = (y1 + y2) / 2 / imgH  # cx / imgW
        wNorm = (x2 - x1) / imgW
        hNorm = (y2 - y1) / imgH
        return cxNorm, cyNorm, wNorm, hNorm

    @staticmethod
    def voc2yolo_boxes(vocBoxes, imgSize):
        toYolo = BBox.voc2yolo
        return [toYolo(b, imgSize) for b in vocBoxes]


def _round(arg):
    return int(round(arg))
