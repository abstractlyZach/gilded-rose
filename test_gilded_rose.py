import pytest

import gilded_rose


quality_test_cases = (
    ('expected_quality', 'item', 'comment'),
    [
        (0, gilded_rose.Item('foo', 10, 0), "idk what i'm doing"),
        (49, gilded_rose.Item('foo', 10, 50), ''),
        (49, gilded_rose.Item('foo', 50, 50), ''),
        (50, gilded_rose.Item('Aged Brie', 50, 50), ''),
        (80, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 80), ''),
        (25, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 25), ''),
        (26, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 50, 25), ''),
        (11, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 50, 10), ''),
        (12, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 10, 10), ''),
        (41, gilded_rose.Item('Aged Brie', 50, 40), ''),
        (50, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 10, 49), ''),
        (50, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 5, 49), ''),
        (48, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 5, 45), ''),
        (48, gilded_rose.Item('foo', 0, 50), ''),
        (42, gilded_rose.Item('Aged Brie', 0, 40), ''),
        (50, gilded_rose.Item('Aged Brie', 0, 50), ''),
        (0, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 0, 45), ''),
        (0, gilded_rose.Item('foo', 0, 0), ''),
        (80, gilded_rose.Item('Sulfuras, Hand of Ragnaros', -1, 80), ''),
    ]
)

sell_in_test_cases = (
    ('expected_sell_in', 'item', 'comment'),
    [
        (9, gilded_rose.Item('foo', 10, 0), 'cool item'),
        (9, gilded_rose.Item('foo', 10, 50), ''),
        (100, gilded_rose.Item('foo', 101, 50), ''),
        (49, gilded_rose.Item('Aged Brie', 50, 50), ''),
        (50, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 50), ''),
        (50, gilded_rose.Item('Sulfuras, Hand of Ragnaros', 50, 25), ''),
        (49, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 50, 25), ''),
        (49, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 50, 10), ''),
        (9, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 10, 10), ''),
        (49, gilded_rose.Item('Aged Brie', 50, 40), ''),
        (9, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 10, 49), ''),
        (4, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 5, 49), ''),
        (4, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 5, 45), ''),
        (-1, gilded_rose.Item('foo', 0, 50), ''),
        (-1, gilded_rose.Item('Aged Brie', 0, 40), ''),
        (-1, gilded_rose.Item('Aged Brie', 0, 50), ''),
        (-1, gilded_rose.Item('Backstage passes to a TAFKAL80ETC concert', 0, 45), ''),
        (-1, gilded_rose.Item('foo', 0, 0), ''),
        (-1, gilded_rose.Item('Sulfuras, Hand of Ragnaros', -1, 80), ''),
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
