# -*- encoding: utf-8 -*-
from supriya.tools import synthdeftools
from supriya.tools.nonrealtimetools.SessionObject import SessionObject


class BusGroup(SessionObject):
    """
    A non-realtime bus group.

    ::

        >>> session = nonrealtimetools.Session()
        >>> bus_group = session.add_bus_group(3)
        >>> print(bus_group)
        <BusGroup(
            bus_count=3,
            calculation_rate=CalculationRate.CONTROL
            )>

    ::

        >>> with session.at(1):
        ...     bus_group[0].set_(0.333)
        ...
        >>> with session.at(3):
        ...     bus_group.fill(0.5)
        ...
        >>> with session.at(5):
        ...     bus_group[1].set_(0.666)
        ...     bus_group[2].set_(0.75)
        ...

    ::

        >>> for offset in range(7):
        ...     with session.at(offset):
        ...         values = bus_group.get()
        ...         print(offset, values)
        ...
        0 [0.0, 0.0, 0.0]
        1 [0.333, 0.0, 0.0]
        2 [0.333, 0.0, 0.0]
        3 [0.5, 0.5, 0.5]
        4 [0.5, 0.5, 0.5]
        5 [0.5, 0.666, 0.75]
        6 [0.5, 0.666, 0.75]

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_buses',
        '_calculation_rate',
        '_session',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        session,
        bus_count=1,
        calculation_rate=None,
        ):
        from supriya.tools import nonrealtimetools
        SessionObject.__init__(self, session)
        assert calculation_rate is not None
        calculation_rate = synthdeftools.CalculationRate.from_expr(
            calculation_rate)
        self._calculation_rate = calculation_rate
        bus_count = int(bus_count)
        assert 0 < bus_count
        self._buses = tuple(
            nonrealtimetools.Bus(
                session,
                bus_group=self,
                calculation_rate=self.calculation_rate,
                )
            for _ in range(bus_count)
            )

    ### SPECIAL METHODS ###

    def __contains__(self, item):
        return self.buses.__contains__(item)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._buses[item]
        elif isinstance(item, slice):
            return tuple(self._buses[item])

    def __iter__(self):
        return iter(self.buses)

    def __len__(self):
        return len(self._buses)

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        from abjad.tools import systemtools
        from supriya.tools import nonrealtimetools
        agent = systemtools.StorageFormatAgent(self)
        names = agent.signature_positional_names
        values = (agent._get(_) for _ in names)
        values = [
            _ for _ in values
            if not isinstance(_, nonrealtimetools.Session)
            ]
        return systemtools.FormatSpecification(
            client=self,
            repr_is_indented=True,
            repr_is_bracketed=True,
            storage_format_is_bracketed=True,
            storage_format_args_values=values,
            )

    ### PUBLIC METHODS ###

    def fill(self, value):
        assert self.session._active_moments
        offset = self.session._active_moments[-1].offset
        for bus in self:
            bus._set_at_offset(offset, value)

    def get(self):
        assert self.session._active_moments
        offset = self.session._active_moments[-1].offset
        values = [bus._get_at_offset(offset) for bus in self]
        return values

    def get_map_symbol(self, bus_id):
        from supriya.tools import synthdeftools
        if self.calculation_rate == synthdeftools.CalculationRate.AUDIO:
            map_symbol = 'a'
        else:
            map_symbol = 'c'
        map_symbol += str(bus_id)
        return map_symbol

    def index(self, item):
        return self.buses.index(item)

    ### PUBLIC PROPERTIES ###

    @property
    def bus_count(self):
        return len(self._buses)

    @property
    def buses(self):
        return self._buses

    @property
    def calculation_rate(self):
        return self._calculation_rate
