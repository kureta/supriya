# -*- encoding: utf-8 -*-
from supriya.tools import synthdeftools
from supriya.tools.nonrealtimetools.BusGroup import BusGroup


class AudioOutputBusGroup(BusGroup):

    def __init__(
        self,
        session,
        ):
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        bus_count = session.output_count
        BusGroup.__init__(
            self,
            session,
            bus_count=bus_count,
            calculation_rate=calculation_rate,
            )
