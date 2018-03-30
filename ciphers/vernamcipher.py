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

import binascii

class VernamCipher(object):
    """
    The VernamCipher class.

    This class contains the encrypt and decrypt 
    implementation of the Vernam's Cipher algorithm.
    """

    def __cipher(self, text, key):
        """
        Encrypts/Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt/decrypt
        key: str
            The encryption key

        Returns
        -------
        result: str
            The encrypted/decrypted content
        """

        key_index = 0
        key_length = len(key)
        xored = []

        for letter in text:
            key_mod = key_index % key_length
            xor = ord(key[key_mod]) ^ ord(letter)
            xored.append(chr(xor))
            key_index += 1

        return "".join(xored)

    def encrypt(self, text, key):
        """
        Encrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt
        key: str
            The encryption key

        Returns
        -------
        result: str
            The encrypted content        
        """

        return self.__cipher(text, key)

    def encrypt_hex(self, text, key):
        """
        Encrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt
        key: str
            The encryption key

        Returns
        -------
        result: str
            The hex encrypted content        
        """

        encrypted = self.__cipher(text, key)
        return binascii.hexlify(encrypted)

    def decrypt(self, text, key):
        """
        Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to decrypt
        key: str
            The encryption key

        Returns
        -------
        result: str
            The decrypted content        
        """

        return self.__cipher(text, key)

    def decrypt_hex(self, text, key):
        """
        Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to decrypt
        key: str
            The encryption key

        Returns
        -------
        result: str
            The decrypted content        
        """
        unhex = binascii.unhexlify(text)
        return self.__cipher(unhex, key)