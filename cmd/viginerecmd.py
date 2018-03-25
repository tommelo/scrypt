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

# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# pylint: disable=C0103,C0301,W1202,W0212

import sys
from command import Command
from ciphers.viginerecipher import ViginereCipher
from utils.ioutils import IOUtils

class ViginereCommand(Command):
    """
    The ViginereCommand class.

    This class handles the option -c, --cipher viginere
    It contains the handlers for the operations:
    -e, --encrypt
    -d, --decrypt
    """

    def __init__(self):        
        Command.__init__(self, {
            "encrypt": self.__encrypt,
            "decrypt": self.__decrypt
        })

        self.cipher = ViginereCipher()

    def __encrypt(self, kwargs):
        """
        Handles the operation -e, --encrypt

        Parameters
        ----------
        kwargs: dict
            The dictionary parameter containing the attributes:
            * text - The content to be encrypted
            * key - The encryption key
        
        Returns
        -------
        result: str
            The encryted content
        """

        return self.cipher.encrypt(kwargs["text"], kwargs["key"])

    def __decrypt(self, kwargs):
        """
        Handles the operation -d, --decrypt

        Parameters
        ----------
        kwargs: dict
            The dictionary parameter containing the attributes:
            * text - The content to be decrypted
            * key - The encryption key
        
        Returns
        -------
        result: str
            The decryted content
        """

        return self.cipher.decrypt(kwargs["text"], kwargs["key"])

    def execute(self, args):
        """
        The abstract execute method implementation.
        Validates and executes the given cli arguments.
        """

        if not args.plaintext and not args.input:
            raise ValueError("No content to encrypt/decrypt")

        if not args.key:
            raise ValueError("No encryption key given")

        plaintext = args.plaintext or args.input.read()
        self.command_mode_exec(args, text=plaintext, key=args.key)
