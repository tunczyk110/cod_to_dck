# Cockatrice to Xmage deck converter

Requires Python 3 and [Scryfall database](https://archive.scryfall.com/json/scryfall-default-cards.json) (Xmage uses set code and card's number in set). Place it where the script is located.

Some card sets present in the database may not be implemented in Xmage. In that case, it will show a warning when loading the deck, but will replace offending cards with an implemented version and the deck will work just fine.

## Usage

`./cod_to_dck.py [deck]...`

For example, to convert all decks in directory, simply do `./cod_to_dck.py *.cod`