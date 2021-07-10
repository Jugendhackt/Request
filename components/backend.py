#!/bin/python3

from streams import Stream
from posts import Post

CALL_TYPES = {
    "FETCH": 1,
    "STOP_FETCHING": 2
}


class Call:
    type: int
    args: dict

    def __init__(self, call_type: int, args: dict):
        if call_type not in CALL_TYPES.values():
            raise ValueError("Invalid call type: {}, supported: {}".format(call_type, CALL_TYPES))
        self.type = call_type
        self.args = args

    def __repr__(self):
        return "Call {{ type: {}, args: {} }}".format(self.type, self.args)


class Backend:
    def __init__(self, post_stream: Stream, call_stream: Stream):
        """
        if issubclass(post_stream.type(), Post):
            raise TypeError("Post Stream is of wrong type: {}, expected {}".format(post_stream.type(), Post))
        if issubclass(call_stream.type(), Call):
            raise TypeError("Call Stream is of wrong type: {}, expected {}".format(call_stream.type(), Call))
"""
        self._post_stream = post_stream
        self._call_stream = call_stream
        self._to_fetch = []

    # Must not block or allocate
    def call(self, call):
        self._call_stream.push(call)

    def _handle_calls(self):
        for call in self._call_stream:
            print("{}".format(call))
            if call.type == CALL_TYPES["FETCH"]:
                self._to_fetch.append(call.args)
            elif call.type == CALL_TYPES["STOP_FETCHING"]:
                self._to_fetch.remove(call.args)

    def _fetch_current(self):
        for fetch in self._to_fetch:
            self._fetch(fetch)

    def _fetch(self, fetch):
        # TODO
        print("_fetch({})".format(fetch))
        if fetch["once"]:
            print("Once")
            self._to_fetch.remove(fetch)

    def run(self):
        while True:
            # Handle outstanding calls
            self._handle_calls()
            # Handle outstanding fetches
            self._fetch_current()
