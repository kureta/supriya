# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.UGen import UGen


class Dust2(UGen):
    """
    A bipolar random impulse generator.

    ::

        >>> dust_2 = ugentools.Dust2.ar(
        ...    density=23,
        ...    )
        >>> dust_2
        Dust2.ar()

    """


    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    _ordered_input_names = (
        'density',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        density=0.,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            density=density,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        density=0,
        ):
        """
        Constructs an audio-rate bipolar random impulse generator.

        ::

            >>> ugentools.Dust2.ar(
            ...     density=[1, 2],
            ...     )
            UGenArray({2})

        Returns unit generator graph.
        """
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            density=density,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        density=0,
        ):
        """
        Constructs a control-rate bipolar random impulse generator.

        ::

            >>> ugentools.Dust2.kr(
            ...     density=[1, 2],
            ...     )
            UGenArray({2})

        Returns unit generator graph.
        """
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            density=density,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def density(self):
        """
        Gets `density` input of Dust2.

        ::

            >>> density = 0.25
            >>> dust_2 = ugentools.Dust2.ar(
            ...     density=density,
            ...     )
            >>> dust_2.density
            0.25

        Returns input.
        """
        index = self._ordered_input_names.index('density')
        return self._inputs[index]
