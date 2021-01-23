from trvo_utils.core.rect import Rect


def main():
    r1 = Rect.fromXyxy([1, 1, 3, 3])
    r2 = Rect.fromXyxy([2, 2, 5, 4])
    assert r1.intersection(r2).xyxy == [2, 2, 3, 3]

    r3 = Rect.fromXyxy([3, 3, 5, 4])
    assert r1.intersection(r3).xyxy == [0, 0, 0, 0]

    r4 = Rect.fromXyxy([4, 3, 5, 4])
    assert r1.intersection(r4).xyxy == [0, 0, 0, 0]



if __name__ == '__main__':
    main()
