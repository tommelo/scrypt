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

class VigenereCipher(object):
    """
    The VigenereCipher class.

    This class contains the encrypt and decrypt 
    implementation of the Vigenere's Cipher algorithm.
    """

    ASCII_CHARS = [c for c in (chr(i) for i in xrange(32, 127))]
    ASCII_CHARS_LENGTH = len(ASCII_CHARS)

    def __cipher(self, text, key, decrypt=False):
        """
        Encrypts/Decrypts the given content.

        Parameters
        ----------
        text: str
            The text content to encrypt/decrypt
        key: str
            The encryption key
        decrypt: Bool
            Enables/Disables the decrypt mode

        Returns
        -------
        result: str
            The encrypted/decrypted content
        """

        result = []
        key_length = len(key)

        for index, letter in enumerate(text):
            if letter in self.ASCII_CHARS:
                char_index = self.ASCII_CHARS.index(letter)

                key_char = key[index % key_length]
                key_index = self.ASCII_CHARS.index(key_char)
                
                if decrypt:
                    key_index *= -1

                code = self.ASCII_CHARS[(char_index + key_index) % self.ASCII_CHARS_LENGTH]
                result.append(code)
            else:
                result.append(letter)

        return "".join(result)

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

        return self.__cipher(text, key, decrypt=True)
