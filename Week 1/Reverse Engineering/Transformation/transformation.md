# Transformation 
<sub>{Reverse Engineering [Easy] - by madStacks · picoCTF 2021} </sub>
<br></br>

## Approach
This one was quite fun, it makes you think about the logic quite a bit:
```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

What does this code do? Its quite big and scary no?

First, let us examine from the start, so here, that would be the ''.join() function
This _concatinates_ whatever charecters is present in the list within

[...] <- this is equivalent to list(...)

Now, instead of trying to figure out the operation first, instead look at the parameters of the for function:
```
for i in range(0, len(flag), 2)
```
It iterates over every _other_ charecter in the flag. Logically, if we have the output of this function and its recoverable, this implies both the i and the i+1 charectors are being used to calculate the resulting text

We see chr(...) function, which turns numberical numbers into ascii charecters if the number is equivalent to any ascii code (For instance, chr(65) is "A"; The opposite of chr(...) is ord(...) -> ord("A") = 65)

Inside chr(...),
```
(ord(flag[i]) << 8) + ord(flag[i + 1])
```
The simpler expression  `ord(flag[i + 1])` just means adding the ascii number code associated with the i + 1 charecter

The other expression `ord(flag[i]) << 8)` uses **BITWISE SHIFT** 8 bits to the left

Although intimidating at first, it is a very simple operation:

Let A be a number who's binary looks like: 10100101
Then A << 8 is simply 1010010100000000

With 8 additional zeros to the right

you can also shift this new number to the left,
Then 1010010100000000 >> 8 is simple 10100101 aka A again

But notice that if you shift it to the left, the bits of A are preserved on the left, whereas when you shift to the right the bits vanish away

This would be important if say, you _added_ a 8 bit number (ascii code) of a charecter to it

(I hope its clear, adding bits to 0 in binary gives those bits themself)

By extracting the last 8 bits of every charector in the given data string we get the i + 1 charecter and by right shifting it we get the i charecter, repeat for all charecters

## Solution
Refer solver.py; 

## Flag
picoCTF{16_bits_inst34d_of_8_b7f62ca5}

## Takeaway
int function is the goat, it can convert bits written in string to integer representation; Also bin(...) returns a string in format "0b10100101" for bin(A) for example



