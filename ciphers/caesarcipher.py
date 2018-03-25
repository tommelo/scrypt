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

import string

class CaesarCipher(object):
    """
    The CaesarCipher class.

    This class contains the encrypt and decrypt 
    implementation of the Caesar's Cipher algorithm.
    """

    ALPHABET_LENGTH = len(string.ascii_lowercase)

    def __init__(self):
        self.alphabet = string.ascii_lowercase

    def __cipher(self, text, rot, decrypt=False):
        """
        Encrypts/Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt/decrypt
        rot: int
            The offset to rotate
        decrypt: Bool
            Enables/Disables the decrypt mode

        Returns
        -------
        result: str
            The encrypted/decrypted content
        """

        result = []

        for letter in text:

            if letter.lower() in self.alphabet:
                unicode_point = ord("a") if letter.islower() else ord("A")
                start = ord(letter) - unicode_point
                
                if decrypt:
                    offset = ((start - rot) % len(self.alphabet)) + unicode_point
                else:
                    offset = ((start + rot) % len(self.alphabet)) + unicode_point

                result.append(chr(offset))

            else:
                result.append(letter)

        return "".join(result)

    def encrypt(self, text, rot):
        """
        Encrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt
        rot: int
            The offset to rotate

        Returns
        -------
        result: str
            The encrypted content        
        """

        return self.__cipher(text, rot)

    def decrypt(self, text, rot):
        """
        Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to decrypt
        rot: int
            The offset to rotate

        Returns
        -------
        result: str
            The decrypted content        
        """

        return self.__cipher(text, rot, decrypt=True)
