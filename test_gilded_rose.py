import pytest

import gilded_rose


quality_test_cases = (
    ('expected_quality', 'item', 'comment'),
    [
        (0, gilded_rose.Item('foo', 10, 0), "idk what i'm doing"),
        (99, gilded_rose.Item('foo', 10, 100), ''),
        (99, gilded_rose.Item('foo', 50, 100), ''),
        (100, gilded_rose.Item('Aged Brie', 50, 100), ''),
        (100, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 100), ''),
        (25, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 25), ''),
        (26, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 50, 25), ''),
    ]
)

sell_in_test_cases = (
    ('expected_sell_in', 'item', 'comment'),
    [
        (9, gilded_rose.Item('foo', 10, 0), 'cool item'),
        (9, gilded_rose.Item('foo', 10, 100), ''),
        (100, gilded_rose.Item('foo', 101, 100), ''),
        (49, gilded_rose.Item('Aged Brie', 50, 100), ''),
        (50, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 100), ''),
        (50, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 25), ''),
    ]
)


@pytest.mark.parametrize(*quality_test_cases)
def test_quality_after_update_quality(expected_quality, item, comment):
    items = [item]
    inn = gilded_rose.GildedRose(items)
    inn.update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(*sell_in_test_cases)
def test_sell_in_after_update_quality(expected_sell_in, item, comment):
    items = [item]
    inn = gilded_rose.GildedRose(items)
    inn.update_quality()
    assert item.sell_in == expected_sell_in
