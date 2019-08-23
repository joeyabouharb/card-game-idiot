const readwrite = require('../fs/readwrite')

function * shuffleDeck () {
  const cards = readwrite.loadDeck()
  let currentIndex = cards.length
  while (currentIndex !== 0) {
    const randomVal = Math.floor(Math.random() * currentIndex)
    --currentIndex
    const tempVal = cards[currentIndex]
    yield cards[randomVal]
    cards[randomVal] = tempVal
  }
}

console.log(shuffleDeck().next().value)
