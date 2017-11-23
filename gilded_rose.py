MIN_QUALITY = 0
MAX_QUALITY = 50
SULFURAS = 'Sulfuras, Hand of Ragnaros'
BRIE = 'Aged Brie'
ETC_TICKETS = 'Backstage passes to a TAFKAL80ETC concert'

SPECIAL_ITEMS = [SULFURAS, BRIE, ETC_TICKETS]


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update(item)


# DO NOT MODIFY THIS CLASS.
# I assume that also means you can't extend or inherit from it either
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self): # pragma: no cover
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def update(item):
    if item.name in SPECIAL_ITEMS:
        update_special_item(item)
    else:
        update_normal_item(item)

def update_special_item(item):
    if item.name == SULFURAS:
        update_sulfuras(item)
    elif item.name == BRIE:
        update_aged_brie(item)
    elif item.name == ETC_TICKETS:
        update_etc_tickets(item)

def update_sulfuras(item):
    return

def update_aged_brie(item):
    item.sell_in -= 1
    item.quality = get_new_brie_quality(item)

def get_new_brie_quality(item):
    quality_to_add = 1
    if is_expired(item):
        quality_to_add = 2
    return min(item.quality + quality_to_add, MAX_QUALITY)

def update_etc_tickets(item):
    item.quality = get_new_etc_tickets_quality(item)
    # updating sell_in happens at a different phase here because of the original logic of
    # arriving concerts. change that function if you want to move this statement up.
    item.sell_in -= 1
    if is_expired(item):
        item.quality = 0

def get_new_etc_tickets_quality(item):
    quality_to_add = 1
    if item.sell_in < 6:
        quality_to_add = 3
    elif item.sell_in < 11:
        quality_to_add = 2
    new_quality = item.quality + quality_to_add
    return min(new_quality, MAX_QUALITY)

def update_normal_item(item):
    item.sell_in -= 1
    item.quality = get_new_normal_item_quality(item)

def get_new_normal_item_quality(item):
    quality_to_lose = 1
    if is_expired(item):
        quality_to_lose = 2
    new_quality = item.quality - quality_to_lose
    return max(new_quality, MIN_QUALITY)


def is_expired(item):
    return item.sell_in < 0

