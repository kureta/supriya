# -*- encoding: utf-8 -*-
import abc
from supriya.tools.ugentools.PseudoUGen import PseudoUGen


class LinLin(PseudoUGen):

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Line Utility UGens'

    __slots__ = ()

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    ### PUBLIC METHODS ###

    @staticmethod
    def ar(
        source=None,
        input_minimum=0.0,
        input_maximum=1.0,
        output_minimum=1.0,
        output_maximum=2.0,
        ):
        from supriya.tools import ugentools
        input_minimum = float(input_minimum)
        input_maximum = float(input_maximum)
        output_minimum = float(output_minimum)
        output_maximum = float(output_maximum)
        scale = (output_maximum - output_minimum) / (input_maximum - input_minimum)
        offset = output_minimum - (scale * input_minimum)
        ugen = ugentools.MulAdd.new(
            source=source,
            multiplier=scale,
            addend=offset,
            )
        return ugen

    @staticmethod
    def kr(
        source=None,
        input_minimum=0.0,
        input_maximum=1.0,
        output_minimum=1.0,
        output_maximum=2.0,
        ):
        from supriya.tools import ugentools
        input_minimum = float(input_minimum)
        input_maximum = float(input_maximum)
        output_minimum = float(output_minimum)
        output_maximum = float(output_maximum)
        scale = (output_maximum - output_minimum) / (input_maximum - input_minimum)
        offset = output_minimum - (scale * input_minimum)
        ugen = ugentools.MulAdd.new(
            source=source,
            multiplier=scale,
            addend=offset,
            )
        return ugen
