# vault-door-training 
<sub>{Reverse Engineering [Easy] - by Mark E. Haase · picoCTF 2019} </sub>
<br></br>

## Approach
Open the java file, and don't get scared! It doesn't bite :D

## Solution
Grab the password from the password checker:
```
    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_0009yrGMeEp");
    }
```

## Flag
picoCTF{w4rm1ng_Up_w1tH_jAv4_0009yrGMeEp}

## Takeaway
read code gng



