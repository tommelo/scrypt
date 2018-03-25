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

import abc
import sys
from utils.ioutils import IOUtils

class Command(object):
    """
    The abstract Command class.

    All command handlers should inherit this class.
    This class has a default command execution
    based on the given cli arguments. It also handles
    the piped/output option.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, mode):
        """
        Initiates the class.

        Parameters
        ----------
        mode: dict
            The commands to be executed based on the given cli args.
        """

        self.mode = mode

    def command_mode_exec(self, args, **kwargs):
        """
        Executes the command based on the given cli args.

        Parameters
        ----------
        args: Namespace
            The argparse cli arguments
        kwargs: dict
            The arguments to be passed to the handler
        """

        mode = "".join([key for key in vars(args) if getattr(args, key) is True])
        cipher_exec = self.mode[mode]

        result = cipher_exec(kwargs)
        result_std = "{}\n".format(result)

        if args.output:
            out = args.output
            out.write(result)
            out.close()

        if not args.output or IOUtils.is_piped_output():
            sys.stdout.write(result_std)

    @abc.abstractmethod
    def execute(self, args):
        """
        Handles the command execution.
        """

        raise NotImplementedError('The execute method must be implemented')
