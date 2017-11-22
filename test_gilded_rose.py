import pytest

import gilded_rose


quality_test_cases = (
    ('expected_quality', 'item', 'comment'),
    [
        (0, gilded_rose.Item('foo', 10, 0), "idk what i'm doing")
    ]
)


@pytest.mark.parametrize(*quality_test_cases)
def test_gilded_rose_quality(expected_quality, item, comment):
    items = [item]
    inn = gilded_rose.GildedRose(items)
    inn.update_quality()
    assert item.quality == expected_quality