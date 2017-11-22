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
    if item.name == SULFURAS:
        return
    if item.name not in SPECIAL_ITEMS:
        update_normal_item(item)
    else:
        update_special_item(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        update_expired_item(item)


def update_sulfuras(item):
    return

def update_etc_tickets(item):
    if item.sell_in < 11:
        if item.quality < 50:
            item.quality = item.quality + 1
    if item.sell_in < 6:
        if item.quality < 50:
            item.quality = item.quality + 1

def update_special_item(item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == ETC_TICKETS:
            update_etc_tickets(item)

def update_normal_item(item):
    if item.quality > 0:
        item.quality = item.quality - 1

def update_expired_item(item):
    if item.name != "Aged Brie":
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                item.quality = item.quality - 1
        else:
            item.quality = item.quality - item.quality
    else:
        if item.quality < 50:
            item.quality = item.quality + 1


