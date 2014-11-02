# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class MulAdd(UGen):

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Basic Operator UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'multiplier',
        'addend',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        addend=0.0,
        multiplier=1.0,
        rate=None,
        source=None,
        ):
        UGen.__init__(
            self,
            addend=addend,
            multiplier=multiplier,
            rate=rate,
            source=source,
            )

    ### PRIVATE METHODS ###

    @staticmethod
    def _inputs_are_valid(
        source,
        multiplier,
        addend,
        ):
        from supriya.tools import synthdeftools
        Rate = synthdeftools.Rate
        if source.rate == Rate.AUDIO:
            return True
        if source.rate == Rate.CONTROL:
            if multiplier.rate in (Rate.CONTROL, Rate.SCALAR):
                if addend.rate in (Rate.CONTROL, Rate.SCALAR):
                    return True
        return False

    @classmethod
    def _new_single(
        cls,
        addend=None,
        multiplier=None,
        rate=None,
        source=None,
        ):
        from supriya.tools import synthdeftools
        if multiplier == 0.0:
            return addend
        minus = multiplier == -1
        no_multiplier = multiplier == 1
        no_addend = addend == 0
        if no_multiplier and no_addend:
            return source
        if minus and no_addend:
            return synthdeftools.Op.negative(source)
        if no_addend:
            return source * multiplier
        if minus:
            return addend - source
        if no_multiplier:
            return source + addend
        if cls._inputs_are_valid(source, multiplier, addend):
            return cls(
                addend=addend,
                multiplier=multiplier,
                rate=rate,
                source=source,
                )
        if cls._inputs_are_valid(multiplier, source, addend):
            return cls(
                addend=addend,
                multiplier=source,
                rate=rate,
                source=multiplier,
                )
        return (source * multiplier) + addend

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        source=None,
        multiplier=1.0,
        addend=0.0,
        ):
        from supriya.tools import synthdeftools
        rate = synthdeftools.Rate.from_input((source, multiplier, addend))
        ugen = cls._new_expanded(
            addend=addend,
            multiplier=multiplier,
            rate=rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def addend(self):
        r'''Gets `addend` input of MulAdd.

        ::

            >>> addend = 0.5
            >>> multiplier = 1.5
            >>> source = ugentools.SinOsc.ar()
            >>> mul_add = ugentools.MulAdd.new(
            ...     addend=addend,
            ...     multiplier=multiplier,
            ...     source=source,
            ...     )
            >>> mul_add.addend
            0.5

        Returns input.
        '''
        index = self._ordered_input_names.index('addend')
        return self._inputs[index]

    @property
    def multiplier(self):
        r'''Gets `multiplier` input of MulAdd.

        ::

            >>> addend = 0.5
            >>> multiplier = 1.5
            >>> source = ugentools.SinOsc.ar()
            >>> mul_add = ugentools.MulAdd.new(
            ...     addend=addend,
            ...     multiplier=multiplier,
            ...     source=source,
            ...     )
            >>> mul_add.multiplier
            1.5

        Returns input.
        '''
        index = self._ordered_input_names.index('multiplier')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of MulAdd.

        ::

            >>> addend = 0.5
            >>> multiplier = 1.5
            >>> source = ugentools.SinOsc.ar()
            >>> mul_add = ugentools.MulAdd.new(
            ...     addend=addend,
            ...     multiplier=multiplier,
            ...     source=source,
            ...     )
            >>> mul_add.source
            OutputProxy(
                source=SinOsc(
                    rate=<Rate.AUDIO: 2>,
                    frequency=440.0,
                    phase=0.0
                    ),
                output_index=0
                )

        Returns input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]