import itertools

import cv2


def tryDestroyWindow(name):
    try:
        cv2.destroyWindow(name)
        return True
    except:
        return False


def imshow(*unnamedMat, **namedMat):
    for name, matOrMatWithTitle in itertools.chain(enumerate(unnamedMat), namedMat.items()):
        name = str(name)
        if matOrMatWithTitle is None:
            tryDestroyWindow(name)
            continue
        if isinstance(matOrMatWithTitle, (tuple, list)) and len(matOrMatWithTitle) == 2:
            mat, title = matOrMatWithTitle
        else:
            mat, title = matOrMatWithTitle, None
        cv2.imshow(name, mat)
        if title is not None:
            cv2.setWindowTitle(name, str(title))


# def imshowWait(*unnamedMat, **namedMat):
#     waitForKeys = None
#     kbdKeysParam = 'waitForKeys'
#     if kbdKeysParam in namedMat:
#         waitForKeys = namedMat[kbdKeysParam]
#         del namedMat[kbdKeysParam]
#     imshow(*unnamedMat, **namedMat)
#     return waitKeys(waitForKeys)


def imshowWait(*unnamedMat, waitForKeys=None, **namedMat):
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
