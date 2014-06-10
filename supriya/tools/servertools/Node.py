# -*- encoding: utf-8 -*-
import abc
from supriya.tools.servertools.ServerObjectProxy import ServerObjectProxy


class Node(ServerObjectProxy):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_is_playing',
        '_is_running',
        '_node_id',
        '_parent_group',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self):
        ServerObjectProxy.__init__(self)
        self._parent_group = None
        self._is_playing = False
        self._is_running = False
        self._node_id = None

    ### PUBLIC METHODS ###

    @staticmethod
    def expr_as_node_id(expr):
        from supriya.tools import servertools
        if isinstance(expr, servertools.Server):
            return 0
        elif isinstance(expr, Node):
            return expr.node_id
        elif expr is None:
            return None
        elif isinstance(expr, int):
            return expr
        raise TypeError(expr)

    @staticmethod
    def expr_as_target(expr):
        from supriya.tools import servertools
        if expr is None:
            return Node.expr_as_target(servertools.Server())
        elif isinstance(expr, Node):
            return expr
        elif isinstance(expr, int):
            return servertools.Group(
                node_id=expr,
                server=servertools.Server(),
                send_to_server=True,
                )
        elif isinstance(expr, servertools.Server):
            return expr.default_group
        raise TypeError(expr)

    def free(self, send_to_server=True):
        message = self.make_free_message()
        if send_to_server:
            self.server.send_message(message)
        self._is_playing = False
        self._is_running = False
        self._node_id = None
        self._parent_group = None

    def make_free_message(self):
        message = (11, self.node_id)
        return message

    def make_query_message(self):
        message = (46, self.node_id)
        return message

    def make_run_message(self, should_run=True):
        message = (12, self.node_id, int(should_run))
        return message

    def make_set_message(self, **kwargs):
        message = (15, self.node_id)
        for key, value in kwargs.items():
            message += (key, value)
        return message

    def make_trace_message(self):
        message = (10, self.node_id)
        return message

    def query(self):
        message = self.make_query_message()
        self.server.send_message(message)

    def run(self, should_run=True):
        message = self.make_run_message(should_run=should_run)
        self.server.send_message(message)

    def set(self, **kwargs):
        message = self.make_set_message(**kwargs)
        self.server.send_message(message)

    def trace(self):
        message = self.make_trace_message()
        self.server.send_message(message)

    ### PUBLIC PROPERTIES ###

    @property
    def is_playing(self):
        return self._is_playing

    @property
    def is_running(self):
        return self._is_running

    @property
    def node_id(self):
        return self._node_id

    @property
    def parent_group(self):
        return self._parent_group