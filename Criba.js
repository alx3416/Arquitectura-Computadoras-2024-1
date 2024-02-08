/*
  Criba de Eratóstenes
  Algoritmo el cual permite hallar todos los números primos menores que un numero natural dado, N.

  Para i desde 2 hasta parte entera raíz de N hacer lo siguiente:
    Si i no ha sido marcado entonces:
      Para j desde i hasta n / i hacer lo siguiente:
        Poner una marca en i x j
*/

function criba(number) {
  if(number <= 1) return []
  
  const limit = Math.trunc(Math.sqrt(number))
  const numbersNotPrime = []
  const result = []
  
  for(let i = 2; i <= limit; i++) {
    if(!numbersNotPrime.includes(i)) {
      for(j = i; j <= number / i; j++) numbersNotPrime.push(i * j)
    }
  }
  
  for (let i = 2; i < number; i++) {
			if (!numbersNotPrime.includes(i)) result.push(i)
	}
  
  return result
}