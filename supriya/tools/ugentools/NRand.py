# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class NRand(UGen):
    r'''A sum of `n` uniform distributions.

    ::

        >>> n_rand = ugentools.NRand.ir(
        ...     minimum=-1,
        ...     maximum=1,
        ...     n=1,
        ...     )
        >>> n_rand
        NRand.ir()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Noise UGens'

    __slots__ = ()

    _ordered_input_names = (
        'minimum',
        'maximum',
        'n',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        minimum=0.,
        maximum=1.,
        n=1,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            minimum=minimum,
            maximum=maximum,
            n=n,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ir(
        cls,
        maximum=1,
        minimum=0,
        n=1,
        ):
        r'''Constructs a scalar-rate sum of `n` uniform distributions.

        ::

            >>> n_rand = ugentools.NRand.ir(
            ...    minimum=-1.,
            ...    maximum=1.,
            ...    n=[1, 2, 3],
            ...    )
            >>> n_rand
            UGenArray({3})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            n=n,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def maximum(self):
        r'''Gets `maximum` input of NRand.

        ::

            >>> n_rand = ugentools.NRand.ir(
            ...     minimum=-1.0,
            ...     maximum=1.0,
            ...     )
            >>> n_rand.maximum
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('maximum')
        return self._inputs[index]

    @property
    def minimum(self):
        r'''Gets `minimum` input of NRand.

        ::

            >>> n_rand = ugentools.NRand.ir(
            ...     minimum=-1.0,
            ...     maximum=1.0,
            ...     )
            >>> n_rand.minimum
            -1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('minimum')
        return self._inputs[index]
