# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class GrayNoise(UGen):
    r'''A gray noise unit generator.

    ::

        >>> ugentools.GrayNoise.ar()
        GrayNoise.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        ):
        r'''Creates an audio-rate gray noise unit generator.

        ::

            >>> ugentools.GrayNoise.ar()
            GrayNoise.ar()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        ):
        r'''Creates a control-rate gray noise unit generator.

        ::

            >>> ugentools.GrayNoise.kr()
            GrayNoise.kr()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            )
        return ugen