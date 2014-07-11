# -*- encoding: utf-8 -*-
from supriya.tools.osctools.OscCallback import OscCallback


class SynthDefResponseCallback(OscCallback):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_server',
        )

    ### INITIALIZER ###

    def __init__(self, server):
        from supriya.tools import servertools
        OscCallback.__init__(
            self,
            address_pattern='/d_removed',
            procedure=self.__call__,
            )
        assert isinstance(server, servertools.Server)
        self._server = server

    ### SPECIAL METHODS ###

    def __call__(self, message):
        from supriya.tools import responsetools
        response = responsetools.ResponseManager.handle_message(message)
        if not isinstance(response, tuple):
            response = (response,)
        for x in response:
            synthdef_name = x.synthdef_name
            synthdef = self._server._synthdefs.get(synthdef_name)
            if synthdef is None:
                return
            synthdef.handle_response(x)