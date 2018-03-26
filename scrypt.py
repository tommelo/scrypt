# MIT License
#
# Copyright (c) 2018 Tom Melo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# pylint: disable=C0103,C0301,W1202,W0212

"""
Simple Crypt
This is a small cli tool that implements the classical cipher 
algorithms such as Caesar, Vigenere and Vernam.
"""

import sys
import argparse
from cmd.cmdstrategy import CommandStrategy
from utils.ioutils import IOUtils
from utils.clihelpformatter import CliHelpFormatter

parser = argparse.ArgumentParser(
    prog="scrypt.py",
    usage="python scrypt.py <options>",
    formatter_class=CliHelpFormatter
)

parser.add_argument(
    "plaintext",
    nargs="?",
    help="the plain text to encrypt/decrypt"
)

parser.add_argument(
    "-c",
    "--cipher",
    metavar="",
    help="the cipher(caesar, vigenere or vernam)"
)

parser.add_argument(
    "-e",
    "--encrypt",
    action="store_true",
    help="encrypts the given content"
)

parser.add_argument(
    "-d",
    "--decrypt",
    action="store_true",
    help="decrypts the given content"
)

parser.add_argument(
    "-k",
    "--key",
    metavar="",
    help="the encryption key"
)

parser.add_argument(
    "-i",
    "--input",
    metavar="",
    type=argparse.FileType('r'),
    help="the text file to encrypt/decrypt"
)

parser.add_argument(
    "-o",
    "--output",
    metavar="",
    type=argparse.FileType('w'),
    help="the output file"
)

parser.add_argument(
    "--rot",
    metavar="",
    type=int,
    help="the Caesar cipher offset to rotate(default 13)"
)

parser.add_argument(
    "--brute-force",
    action="store_true",
    help="Caesar cipher brute force mode"
)

parser.add_argument(
    "--version",
    action="version",
    version="v1.0.0"
)

parser.set_defaults(rot=13)

def main(args):
    """
    Executes the Simple Crypt CLI Tool
    """

    try:

        executor = CommandStrategy.resolve(args.cipher)
        executor.execute(args)
        
        sys.stdout.close()
        sys.stderr.close()

    except KeyError:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    except ValueError as error:
        sys.stderr.write("{}\n".format(str(error)))        
        sys.exit(1)

if __name__ == "__main__":
    
    try:

        plaintext = None

        if IOUtils.is_piped_input():
            plaintext = IOUtils.read_piped_input()

        cli_args = parser.parse_args()
        cli_args.plaintext = cli_args.plaintext or plaintext

        main(cli_args)

    except KeyboardInterrupt:
        sys.exit(1)
