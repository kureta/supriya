# -*- encoding: utf-8 -*-
from supriya.tools import osctools


class RequestManager(object):

    ### PUBLIC METHODS ###

    @staticmethod
    def make_node_map_to_control_bus_message(node_id, **settings):
        r'''Makes a /n_map message.

        ::

            >>> from supriya.tools import requesttools
            >>> from supriya.tools import servertools
            >>> manager = requesttools.RequestManager
            >>> message = manager.make_node_map_to_control_bus_message(
            ...     1000,
            ...     frequency=servertools.Bus(9, 'control'),
            ...     phase=servertools.Bus(10, 'control'),
            ...     amplitude=servertools.Bus(11, 'control'),
            ...     )
            >>> message
            OscMessage(14, 1000, 'amplitude', 11, 'frequency', 9, 'phase', 10)

        ::

            >>> message.address == \
            ...     requesttools.RequestId.NODE_MAP_TO_CONTROL_BUS
            True

        Returns OSC message.
        '''
        from supriya.tools import requesttools
        request_id = requesttools.RequestId.NODE_MAP_TO_CONTROL_BUS
        request_id = int(request_id)
        node_id = int(node_id)
        contents = []
        for name, bus in sorted(settings.items()):
            contents.append(name)
            contents.append(int(bus))
        message = osctools.OscMessage(
            request_id,
            node_id,
            *contents
            )
        return message

    @staticmethod
    def make_node_map_to_audio_bus_message(node_id, **settings):
        r'''Makes a /n_mapa message.

        ::

            >>> from supriya.tools import requesttools
            >>> from supriya.tools import servertools
            >>> manager = requesttools.RequestManager
            >>> message = manager.make_node_map_to_audio_bus_message(
            ...     1000,
            ...     frequency=servertools.Bus(9, 'audio'),
            ...     phase=servertools.Bus(10, 'audio'),
            ...     amplitude=servertools.Bus(11, 'audio'),
            ...     )
            >>> message
            OscMessage(60, 1000, 'amplitude', 11, 'frequency', 9, 'phase', 10)

        ::

            >>> message.address == \
            ...     requesttools.RequestId.NODE_MAP_TO_AUDIO_BUS
            True

        Returns OSC message.
        '''
        from supriya.tools import requesttools
        request_id = requesttools.RequestId.NODE_MAP_TO_AUDIO_BUS
        request_id = int(request_id)
        node_id = int(node_id)
        contents = []
        for name, bus in sorted(settings.items()):
            contents.append(name)
            contents.append(int(bus))
        message = osctools.OscMessage(
            request_id,
            node_id,
            *contents
            )
        return message
