"""
Notes: =========================================================================
Notes: Argument parser module - argparse
Notes:      ArgumentParser Class
Notes:          add_argument() method for adding arguments syntax.
Notes:          parse_args()   method for parsing arguments.
Notes: 
Notes:      add_mutually_exclusive_group Class
Notes: 
"""

import argparse

def fib(n, prin):
    a, b = 0,1
    for i in range(n):
        a,b = b, a+b
        if prin:
            print a
    return a


def Main():
    parser = argparse.ArgumentParser()


    # Create mutually exclusive arguments group and add arguments.
    group = parser.add_mutually_exclusive_group()

    # store_true gives boolean value.
    group.add_argument("-v", "--verbose", help="Verbose output",
                       action="store_true")

    group.add_argument("-q", "--quiet", help="Quiet output",
                       action="store_true")



    # Add non-mutually explusive arguments.
    parser.add_argument("num", help="The fibonacci number that you wish to "+\
                                    "calculate", type=int)

    parser.add_argument("-o", "--output", dest='fname',
                        help="Output the result to a file")

    parser.add_argument("-a", "--all", action="store_true", dest='prin',
                        default=False, help="Print all numbers upto n")


    # Parge arguments.
    args = parser.parse_args()

    result = fib(args.num, args.prin)
    

    if args.verbose:
        print "The %dth fibonacci number is %d"%(args.num, result)
    elif args.quiet:
        print result
    else:
        print "Fib(%dth) = %d"%(args.num, result)

    if args.fname is not None:
        with open(args.fname, "a") as f:
            f.write(str(result) + "\n")


#===============================================================================
if __name__ == "__main__":
    Main()
