# kuorderbook
KuCoin Order Book For A Trading Pair

# Install
`pip install requests`

`pip install json`

### For alert sound
`apt-get install alsa-utils`


# Usage
`python kuorderbks coin1 coin2`

```
$ python3 kuorderbks.py --help
usage: kuorderbks.py [-h] [-a amount] [-t target] coin [coin ...]

KuCoin - Order Books for Trading Pair

positional arguments:
  coin

optional arguments:
  -h, --help            show this help message and exit
  -a amount, --amount amount
                        Enter Amount Wanting to Trade
  -t target, --target target
                        Target Amount Wanting to Receive
```

## Alerts

When your target amount is reached **kuorderbks** will loop an alarm sound to notify you.

Requries alsa-utils (aplay).

## Example

`$ python3 kuorderbks.py -a 0.0010000 -t 0.24 XMR BTC`

Output:
```
           ⣴⡄⠀⣴⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⣿⣧⣾⡿⠋⠻⣿⡆⠀⠀⣿⢠⣾⠋⢸⣿⠀⣿⡇⢰⣿⠿⣷⢀⣾⠿⣷⡄⢸⣿⠀⣿⣦⢸⣿
           ⣿⣿⣿⠀⣿⡇⢈⠀⠀⠀⣿⣿⣧⠀⢸⣿⠀⣿⡇⢸⡇⠀⠀⢸⣿⠀⣿⡇⢸⣿⠀⣿⣻⣿⣿
           ⣿⡟⢿⣷⣄⣴⣿⠇⠀⠀⣿⠀⢻⣇⠘⢿⣶⡿⠃⠸⣷⣶⡿⠈⢿⣶⡿⠃⢸⣿⠀⣿⠇⢻⣿
           ⠻⠃⠀⠻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
                           XMR -  BTC                             
_____________BIDS_____________ | _____________ASKS_____________
0.004346      -   0.0067          0.004349      -  13.4779
0.004341      -   1.7000          0.004350      -  15.6838
0.004340      -   0.2200          0.004354      -   0.0012
0.004339      -   1.7000          0.004356      -   0.0823
0.004338      -   1.3000          0.004357      -  31.0047
0.004337      -   0.3737          0.004358      -   1.7000
0.004336      -   7.8172          0.004359      -   0.0244
0.004335      -   1.0800          0.004360      -   0.0129
0.004334      - 198.7435          0.004361      -   0.2472
0.004333      -  22.5365          0.004362      -   0.0596
0.004332      -  13.6840          0.004363      -   6.0111
0.004331      -   0.4600          0.004364      -   0.0100
0.004330      -   3.0000          0.004365      -   0.0523
0.004329      -   2.2719          0.004366      -   0.0067
0.004328      -  61.8879          0.004367      -  10.0092
0.004327      -   1.0800          0.004368      -   0.1707
0.004326      -   0.1100          0.004369      -   0.0734
0.004325      -   0.0276          0.004373      -   1.7242
0.004324      -  10.0379          0.004374      -   0.6106
0.004323      -   1.3013          0.004375      -  61.7046

                   Expected: 0.229937916762

                    Minimum: 0.228571428571

                     Target: 0.004166666667

```

## Useful

Using *watch* to loop the script. 

`watch -n 10 'python3 kuorderbks XMR BTC'`
