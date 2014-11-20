# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.PV_MagAbove import PV_MagAbove


class PV_MagClip(PV_MagAbove):
    r'''

    ::

        >>> pv_mag_clip = ugentools.PV_MagClip.(
        ...     buffer_id=None,
        ...     threshold=0,
        ...     )
        >>> pv_mag_clip

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        'threshold',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        threshold=0,
        ):
        PV_MagAbove.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            threshold=threshold,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        buffer_id=None,
        threshold=0,
        ):
        r'''Constructs a PV_MagClip.

        ::

            >>> pv_mag_clip = ugentools.PV_MagClip.new(
            ...     buffer_id=None,
            ...     threshold=0,
            ...     )
            >>> pv_mag_clip

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            threshold=threshold,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        r'''Gets `buffer_id` input of PV_MagClip.

        ::

            >>> pv_mag_clip = ugentools.PV_MagClip.ar(
            ...     buffer_id=None,
            ...     threshold=0,
            ...     )
            >>> pv_mag_clip.buffer_id

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def threshold(self):
        r'''Gets `threshold` input of PV_MagClip.

        ::

            >>> pv_mag_clip = ugentools.PV_MagClip.ar(
            ...     buffer_id=None,
            ...     threshold=0,
            ...     )
            >>> pv_mag_clip.threshold

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('threshold')
        return self._inputs[index]