# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.WidthFirstUGen import WidthFirstUGen


class IFFT(WidthFirstUGen):
    r'''An inverse fast Fourier transform.

    ::

        >>> buffer_id = ugentools.LocalBuf(2048)
        >>> ifft = ugentools.IFFT.ar(
        ...     buffer_id=buffer_id,
        ...     window_size=0,
        ...     window_type=0,
        ...     )
        >>> ifft
        IFFT.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        'window_type',
        'window_size',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        window_size=0,
        window_type=0,
        ):
        WidthFirstUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            window_size=window_size,
            window_type=window_type,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        window_size=0,
        window_type=0,
        ):
        r'''Constructs an audio-rate IFFT.

        ::

            >>> buffer_id = ugentools.LocalBuf(2048)
            >>> ifft = ugentools.IFFT.ar(
            ...     buffer_id=buffer_id,
            ...     window_size=0,
            ...     window_type=0,
            ...     )
            >>> ifft
            IFFT.ar()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            window_size=window_size,
            window_type=window_type,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        window_size=0,
        window_type=0,
        ):
        r'''Constructs a control-rate IFFT.

        ::

            >>> buffer_id = ugentools.LocalBuf(2048)
            >>> ifft = ugentools.IFFT.kr(
            ...     buffer_id=buffer_id,
            ...     window_size=0,
            ...     window_type=0,
            ...     )
            >>> ifft
            IFFT.kr()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            window_size=window_size,
            window_type=window_type,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        r'''Gets `buffer_id` input of IFFT.

        ::

            >>> buffer_id = ugentools.LocalBuf(2048)
            >>> ifft = ugentools.IFFT.ar(
            ...     buffer_id=buffer_id,
            ...     window_size=0,
            ...     window_type=0,
            ...     )
            >>> ifft.buffer_id
            OutputProxy(
                source=LocalBuf(
                    frame_count=2048.0,
                    calculation_rate=<CalculationRate.SCALAR: 0>,
                    channel_count=1.0
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def window_size(self):
        r'''Gets `window_size` input of IFFT.

        ::

            >>> buffer_id = ugentools.LocalBuf(2048)
            >>> ifft = ugentools.IFFT.ar(
            ...     buffer_id=buffer_id,
            ...     window_size=0,
            ...     window_type=0,
            ...     )
            >>> ifft.window_size
            0.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('window_size')
        return self._inputs[index]

    @property
    def window_type(self):
        r'''Gets `window_type` input of IFFT.

        ::

            >>> buffer_id = ugentools.LocalBuf(2048)
            >>> ifft = ugentools.IFFT.ar(
            ...     buffer_id=buffer_id,
            ...     window_size=0,
            ...     window_type=0,
            ...     )
            >>> ifft.window_type
            0.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('window_type')
        return self._inputs[index]