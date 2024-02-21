import criba from "./Criba.js"

export default function goldbach(number) {
  const primes = criba(number)
  const result = []

  for(let i = 0; i < primes.length; i++) {
    for(let j = 0; j < primes.length; j++) {
      if(primes[i] + primes[j] == number) result.push([primes[i],  primes[j]])
    }
  }

  return result
}