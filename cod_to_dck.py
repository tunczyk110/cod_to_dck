#!/usr/bin/env python3

import sys
import json
import xml.etree.ElementTree as et

if __name__ == "__main__":
    files = sys.argv[1:]
    print(f"Got {len(files)} decks to convert")

    print("Parsing scryfall database...")
    with open('scryfall-default-cards.json', encoding='utf8') as card_db_file:
        card_db = json.load(card_db_file)

    for fname in files:
        print(f"Converting {fname}...")
        tree = et.parse(fname)

        with open(fname.replace('cod', 'dck'), 'w') as new_file:
            for zone in tree.getroot().iter('zone'):
                zone_name = zone.attrib.get('name')
                for card in zone:
                    cardname = card.attrib.get('name')
                    count = card.attrib.get('number')
                    for i in card_db:
                        if i['name'] == cardname and i['promo'] == False:
                            set_code = i['set'].upper()
                            collector_number = i['collector_number']
                            break
                    line = f"{count} [{set_code}:{collector_number}] {cardname}"
                    if zone_name == 'side':
                        line = f"SB: {line}"
                    new_file.write(f"{line}\n")

    print(f"Done!")
