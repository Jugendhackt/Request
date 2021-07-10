#!/bin/python3
import json

import grequests
import jmespath
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
        self._to_fetch = Stream(10, dict)
        self._to_stop = []

    # Must not block or allocate
    def call(self, call):
        self._call_stream.push(call)

    def _handle_calls(self):
        for call in self._call_stream:
            print("{}".format(call))
            if call.type == CALL_TYPES["FETCH"]:
                self._to_fetch.push(call.args)
            elif call.type == CALL_TYPES["STOP_FETCHING"]:
                self._to_stop.append(call.args)

    def _fetch_current(self):
        for fetch in self._to_fetch:
            self._fetch(fetch)

    def _fetch(self, fetch):
        # Read API specification from file
        with open(f"apis/{fetch['api']}", "r") as file:
            api = json.load(file)
        # Get JSON from server
        res = (
            grequests.get(api["url"], headers={'User-Agent': 'Request'})
            .send()
            .response
            .json()
        )
        # Transform JSON from server to Post objects
        posts = jmespath.search(api["query"], res)

        # Create and push Post objects
        for post in posts:
            self._post_stream.push(Post(post))

        # Push fetch back to stream
        if not fetch["once"] and fetch not in self._to_stop:
            self._to_fetch.push(fetch)

    def run(self):
        while True:
            # Handle outstanding calls
            self._handle_calls()
            # Handle outstanding fetches
            self._fetch_current()
