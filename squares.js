function checkeredBoard(dimension) {
  const whiteSquare = '\u25A0'
  const blackSquare = '\u25A1'
  const totalOfSquares = dimension * dimension
  const isEven = dimension % 2 == 0
  var auxIsEven = Boolean(isEven)
  var superString = ''
  var auxCounter = 1
  for (var counter = 1; counter <= totalOfSquares; counter++) {
    superString += auxIsEven ? blackSquare : whiteSquare
    auxIsEven = !auxIsEven
    if (auxCounter == dimension && counter != totalOfSquares) {
      superString += '\n'
      if(isEven){
        auxIsEven = !auxIsEven
      }
      auxCounter = 1
    } else if (counter != totalOfSquares) {
      superString += ' '
      auxCounter ++
    }
  }
  return superString
}

try{
  console.log(checkeredBoard(parseInt(process.argv[2])))
}catch(error){
  console.log('Um número inteiro deve ser passado como parâmetro')
}



