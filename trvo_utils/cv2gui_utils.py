import itertools

import cv2


def imshow(*unnamedMat, **namedMat):
    for name, matOrMatWithTitle in itertools.chain(enumerate(unnamedMat), namedMat.items()):
        if matOrMatWithTitle is None:
            try:
                cv2.destroyWindow(name)
            except:
                pass
            continue
        if isinstance(matOrMatWithTitle, (tuple, list)) and len(matOrMatWithTitle) == 2:
            mat, title = matOrMatWithTitle
        else:
            mat, title = matOrMatWithTitle, None
        winName = str(name)
        cv2.imshow(winName, mat)
        if title is not None:
            cv2.setWindowTitle(winName, str(title))


def imshowWait(*unnamedMat, **namedMat):
    waitForKeys = None
    kbdKeysParam = 'waitForKeys'
    if kbdKeysParam in namedMat:
        waitForKeys = namedMat[kbdKeysParam]
        del namedMat[kbdKeysParam]
    imshow(*unnamedMat, **namedMat)
    return waitKeys(waitForKeys)


def __ensureKeyCodes(keys):
    return [__ensureKeyCode(k) for k in keys]


def __ensureKeyCode(key):
    if isinstance(key, str):
        return ord(key)
    if isinstance(key, int):
        return key
    raise Exception(f'Unexpected type of key: {key} {type(key)}')


def waitKeys(keys):
    if keys is None or keys == [] or keys == ():
        return cv2.waitKey()
    if not isinstance(keys, (list, tuple)):
        keys = [keys]
    keys = __ensureKeyCodes(keys)
    while True:
        key = cv2.waitKey()
        if key in keys:
            return key
