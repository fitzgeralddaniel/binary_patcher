# Binary Patcher

Basic binary patcher in Python to add arguments (up to 6) to my external C2 clients.
This assumes the clients have their args set to 50 A's for the first arg and so on up to 5 args.
This script will look for those bytes and replace them with your args.
Usage:
>bipa.py [input filename] [output filename] [-a arg1] [-b arg2] [-c arg3] [-d arg4] [-e arg5] [-f arg6]
