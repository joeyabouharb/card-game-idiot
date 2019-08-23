const deckData = require('./deck.json')

const loadDeck = () => {
  return deckData.deck
}

module.exports = {
  loadDeck
}
