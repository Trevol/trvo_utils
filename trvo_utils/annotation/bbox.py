class BBox:
    @staticmethod
    def yolo2voc(cx_norm, cy_norm, w_norm, h_norm, imgSize):
        imH, imW = imgSize
        cx = cx_norm * imW
        cy = cy_norm * imH
        w = w_norm * imW
        h = h_norm * imH

        pt1 = _round(cx - w / 2), _round(cy - h / 2)
        pt2 = _round(cx + w / 2), _round(cy + h / 2)
        return pt1, pt2

    @staticmethod
    def voc2yolo(vocBox, imgSize):
        x1, y1, x2, y2 = vocBox
        imgH, imgW = imgSize
        cxNorm = (x1 + x2) / 2 / imgW  # cx / imgW
        cyNorm = (y1 + y2) / 2 / imgH  # cx / imgW
        wNorm = (x2 - x1) / imgW
        hNorm = (y2 - y1) / imgH
        return cxNorm, cyNorm, wNorm, hNorm


def _round(arg):
    return int(round(arg))