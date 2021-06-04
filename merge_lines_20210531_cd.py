#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
#/Users/cdavie/miniconda3/bin/python3
# file **filename**.py

""" description
.. module:: **filename**.py
    :members:
    :platform: Unix, OS X
    :synopsis: **synopsis here**
.. moduleauthor:: Author Name <chrisdphd@gmail.com>
"""

__author__ = "Christopher Davies"
__copyright__ = "Copyright 2020, ChrisD"
__credits__ = ["FirstName LastName"]
__license__ = "Copyright"
__version__ = "0.1"
__maintainer__ = "Christopher Davies"
__email__ = "chrisdphd@gmail.com"
__status__ = "Development"

from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from os.path import exists, isfile
import sys
from collections import defaultdict
import csv


def method_1b(verbose, fh):  ###  for n-col (>2) table.

    data = {}
    for line in fh:
        line = line.strip('\n')
        l0 = line.split('\t')
        key = l0[0]
        vals = l0[1:]
        valdictlist = []

        if not key in data:
            for val in vals:
                valdictlist.append(val)  ### add each element to the list
            data[key] = valdictlist

        else:
            zipped = zip(vals,data[key])
            zipped_list = list(zipped)
            if verbose:
                print ("zipped list:", zipped_list)

            zip_items = []
            for thing in zipped_list:
                joined_thing = "|".join(thing)
                zip_items.append(joined_thing)
                data[key] = zip_items
            if verbose:
                print ("ZIP items:", zip_items)

        if verbose:
            print ("CURRANT:",key,data[key])

    if verbose:
        print ("\nTHE PRINTOUT:")
    for k in sorted(data):
        if verbose:
            print ()
            print (k, data[k])
        printlist = []
        #printlist.append("OUTPUT:")
        printlist.append(k)
        test = (data[k])
        for item in test:
            if verbose:
                print ("item", item)
                print ("length:", len(item))

            l1 = item.split('|')
            if verbose:
                print ("was able to split")   ### therefore its a string, not a list already

            item1 = list(set(l1))  ### remove redundancy
            if verbose:
                print ("Redundancy removed:", item1)
            item2 = "|".join(item1)
            item_string = item2

            printlist.append(item_string)
        print('\t'.join(printlist))



def workflow(verbose, fh):
    """description of workflow
    
    :param <parameter name>: <parameter description>
    :type <parameter name>: <parameter type>
    :returns: <what function returns>
    """

    method_1b(verbose, fh)


def parseCmdlineParams(arg_list=argv):
    """Parses commandline arguments.
    
    :param arg_list: Arguments to parse. Default is argv when called from the
    command-line.
    :type arg_list: list.
    """
    #Create instance of ArgumentParser
    argparser = ArgumentParser(formatter_class=\
        ArgumentDefaultsHelpFormatter, description='cat ~/resource/keep_me_here.tmp1.tab | ~/bin/templates.dir/find_field_headers.py -c -v | less')
    # Script arguments.  Use:
    # argparser.add_argument('--argument',help='help string')
    argparser.add_argument('-f', '--file', help='file to analyse. Format ID<tab>ACTGTGCATGC...etc, on 1 line.', type=str, required=False)
    argparser.add_argument('-c', '--stdin', help='(Flag) info on STDIN to analyse', action="store_true", required=False)
    argparser.add_argument('-v', '--verbose', help='(Flag) verbose output for errror checking', action="store_true", required=False)


    return argparser.parse_args()

def main(args,args_parsed=None):

    #If parsed arguments is passed in, do not parse command-line arguments
    if args_parsed is not None:
        args = args_parsed
    #Else, parse arguments from command-line
    else:
        args = parseCmdlineParams(args)

    fh = None
    if args.stdin:
        fh = sys.stdin
    elif args.file:   ### the mRNA file
        filename = args.file
        if not exists(filename):
            sys.stderr.write('ERROR: file {} does not exist'.format(filename))
            exit(1)
        if not isfile(filename):
            sys.stderr.write('ERROR: file {} is not a file'.format(filename))
            exit(1)
        fh = open(filename, 'r')
    else:
        raise Exception("INPUT source not specified as -c or -f")

    if args.verbose:
        verbose = True
        print("input FILE?:", args.file)
        print("input STDIN?", args.stdin)
        print("actual input:", fh)
    else:
        verbose = False

    #Call workflow for script after parsing command line parameters.
    workflow(verbose, fh)

if __name__ == "__main__":
    main(argv)
