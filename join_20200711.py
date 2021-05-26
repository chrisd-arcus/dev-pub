#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# /Users/cdavie/miniconda3/bin/python3

# file join_YYYYMMDD.py

""" description
.. module:: **filename**.py
    :members:
    :platform: Unix, OS X
    :synopsis: **synopsis here**
.. moduleauthor:: Author Name <chrisdphd@gmail.com>
"""

__author__ = "Christopher Davies"
__copyright__ = " "
__credits__ = ["FirstName LastName"]
__license__ = " "
__version__ = "0.1"
__maintainer__ = "Christopher Davies"
__email__ = "chrisdphd@gmail.com"
__status__ = "Development"

from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from os.path import exists, isfile
import sys


def workflow(verbose, fh1, fh2):
    """description of workflow
    
    :param <parameter name>: <parameter description>
    :type <parameter name>: <parameter type>
    :returns: <what function returns>
    """

    f2_dict = {}
    f2_list = []
    for line2 in fh2:
        line2 = line2.strip('\n')
        l2 = line2.split('\t')
        join_field2 = l2[0]  ### the key
        if not join_field2 in f2_dict.keys():
            f2_list.append(join_field2)
            f2_dict[join_field2] = line2  ### make the assignment of whole line to the key

    #printlist = []
    for item in f2_list:
        print(item, f2_dict.get(item))
    #    printlist.append(item[f2_dict.get(item)])
    #print('\t'.join(printlist))


def parseCmdlineParams(arg_list=argv):
    """Parses commandline arguments.
    
    :param arg_list: Arguments to parse. Default is argv when called from the command-line.
    :type arg_list: list.
    """
    ## Create instance of ArgumentParser
    argparser = ArgumentParser(formatter_class=\
        ArgumentDefaultsHelpFormatter, description='~/bin/join_20200711.py -f1 tmp88 -f2 tmp99 | less')
    # argparser.add_argument('--argument',help='help string')
    argparser.add_argument('-f1', '--file1', help='file to analyse - tsv', type=str, required=False)
    argparser.add_argument('-f2', '--file2', help='file to analyse - tsv', type=str, required=False)
    argparser.add_argument('-v', '--verbose', help='(Flag) verbose output for error checking', action="store_true", required=False)

    return argparser.parse_args()

def main(args,args_parsed=None):

    ## If parsed arguments are passed in, then do not parse CL arguments
    if args_parsed is not None:
        args = args_parsed
    ## else, parse arguments from command-line
    else:
        args = parseCmdlineParams(args)


    if args.file1:   ### the input tsv file we are pulling columns from
        filename1 = args.file1
        if not exists(filename1):
            sys.stderr.write('ERROR: file {} does not exist'.format(filename1))
            exit(1)
        if not isfile(filename1):
            sys.stderr.write('ERROR: file {} is not a file'.format(filename1))
            exit(1)
        fh1 = open(filename1, 'r')

    if args.file2:   ### the input tsv file we are pulling columns from
        filename2 = args.file2
        if not exists(filename2):
            sys.stderr.write('ERROR: file {} does not exist'.format(filename2))
            exit(1)
        if not isfile(filename2):
            sys.stderr.write('ERROR: file {} is not a file'.format(filename2))
            exit(1)
        fh2 = open(filename2, 'r')

    if args.verbose:
        verbose = True
        print("input FILE? :", args.file1)
        print("input FILE? :", args.file2)
    else:
        verbose = False


    #Call workflow for script after parsing command line parameters.
    workflow(verbose, fh1, fh2)

if __name__ == "__main__":
    main(argv)
