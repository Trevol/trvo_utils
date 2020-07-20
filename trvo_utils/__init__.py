from glob import glob


def toInt(*args):
    return toInt_array(args)


def toInt_array(args):
    return map(int, args)


def glob_files(patterns):
    for p in patterns:
        for f in sorted(glob(p)):
            yield f
