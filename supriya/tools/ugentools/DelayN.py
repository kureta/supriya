# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.PureUGen import PureUGen


class DelayN(PureUGen):
    r'''Non-interpolating delay line unit generator.

    ::

        >>> from supriya.tools import ugentools
        >>> source = ugentools.In.ar(bus=0)
        >>> ugentools.DelayN.ar(source=source)
        DelayN.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Delay UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'maximum_delay_time',
        'delay_time',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        rate=None,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        PureUGen.__init__(
            self,
            rate=rate,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        r'''Create an audio-rate non-interpolating delay line.

        ::

            >>> from supriya.tools import ugentools
            >>> source = ugentools.In.ar(bus=0)
            >>> ugentools.DelayN.ar(
            ...     delay_time=0.5,
            ...     maximum_delay_time=1.0,
            ...     source=source,
            ...     )
            DelayN.ar()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        rate = synthdeftools.Rate.AUDIO
        source = cls.as_audio_rate_input(source)
        ugen = cls._new_expanded(
            rate=rate,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        ):
        r'''Create a control-rate non-interpolating delay line.

        ::

            >>> from supriya.tools import ugentools
            >>> source = ugentools.In.kr(bus=0)
            >>> ugentools.DelayN.kr(
            ...     delay_time=0.5,
            ...     maximum_delay_time=1.0,
            ...     source=source,
            ...     )
            DelayN.ar()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        rate = synthdeftools.Rate.AUDIO
        ugen = cls._new_expanded(
            rate=rate,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def delay_time(self):
        r'''Gets `delay_time` input of DelayN.

        ::

            >>> delay_time = None
            >>> delay_n = ugentools.DelayN.ar(
            ...     delay_time=delay_time,
            ...     )
            >>> delay_n.delay_time

        Returns input.
        '''
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        r'''Gets `maximum_delay_time` input of DelayN.

        ::

            >>> maximum_delay_time = None
            >>> delay_n = ugentools.DelayN.ar(
            ...     maximum_delay_time=maximum_delay_time,
            ...     )
            >>> delay_n.maximum_delay_time

        Returns input.
        '''
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of DelayN.

        ::

            >>> source = None
            >>> delay_n = ugentools.DelayN.ar(
            ...     source=source,
            ...     )
            >>> delay_n.source

        Returns input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]