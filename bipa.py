#!/usr/bin/env python
import argparse

def patch_file(args):
    """
    Patches binary file
    :param args: args variable from argparse
    """
    print("Begin patching...")
    with open(args.infile, 'r+b') as f:
        buffer = f.read()
        with open(args.outfile, 'w+b') as o:
            o.write(buffer)
    with open(args.outfile, 'r+b') as o:
        buffer = o.read()
        if args.a:
            print("Patching first arg..")
            arg1 = buffer.find(b"A"*50)
            if (arg1 == -1):
                print("First arg not found.")
            else:
                print("Arg found.")
                o.seek(arg1)
                length = len(args.a)
                o.write((args.a).encode() + b'\x00'*(50-length))
        if args.b:
            print("Patching second arg..")
            arg2 = buffer.find(b"B"*50)
            if (arg2 == -1):
                print("Second arg not found.")
            else:
                print("Arg found.")
                o.seek(arg2)
                length = len(args.b)
                o.write((args.b).encode() + b'\x00'*(50-length))
        if args.c:
            print("Patching third arg..")
            arg3 = buffer.find(b"C"*50)
            if (arg3 == -1):
                print("Third arg not found.")
            else:
                print("Arg found.")
                o.seek(arg3)
                length = len(args.c)
                o.write((args.c).encode() + b'\x00'*(50-length))
        if args.d:
            print("Patching fourth arg..")
            arg4 = buffer.find(b"D"*50)
            if (arg4 == -1):
                print("Fourth arg not found.")
            else:
                print("Arg found.")
                o.seek(arg4)
                length = len(args.d)
                o.write((args.d).encode() + b'\x00'*(50-length))
        if args.e:
            print("Patching fifth arg..")
            arg5 = buffer.find(b"E"*50)
            if (arg5 == -1):
                print("Fifth arg not found.")
            else:
                print("Arg found.")
                o.seek(arg5)
                length = len(args.e)
                o.write((args.e).encode() + b'\x00'*(50-length))

    print("End of patching...")

def main():
    parser = argparse.ArgumentParser(description='Program to patch arguments (up to 5) into executables.',
                                    usage="\n"
                                        "%(prog)s [input filename] [output filename] [-a arg1] [-b arg2] [-c arg3] [-d arg4] [-e arg5]"
                                        "\nUse '%(prog)s -h' for more information.")
    parser.add_argument('infile', help="Full path to input exe file.")
    parser.add_argument('outfile', help="Full path to output exe file.")
    parser.add_argument('--a', '-a', help="First arg.")
    parser.add_argument('-b', help="Second arg.")
    parser.add_argument('-c', help="Third arg.")
    parser.add_argument('-d', help="Fourth arg.")
    parser.add_argument('-e', help="Fifth arg.")
    args = parser.parse_args()
    
    # patch_file(FILENAME, PATCHES)
    patch_file(args)

if __name__ == '__main__':
    main()