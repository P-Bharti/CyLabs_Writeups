# EVEN RSA CAN BE BROKEN???
<sub>{Cryptography [Easy] - by Michael Crotty · picoCTF 2025} </sub>
<br></br>

## Approach
Given N,e,C of a RSA, we can find the plaintext trivially using tools like dcode IF one of the primes is weak (as N = pq, one being weak means both are weak)

## Solution
Submit the N, C, E to [Dcode](https://www.dcode.fr/rsa-cipher) and let it figure out that p=2:

## Flag
picoCTF{tw0_1$_pr!m31c9046c4}

## Takeaway
this only works if we're lucky with the prime being so weak.. worth a hail mary at the start though



