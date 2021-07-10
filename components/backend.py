#!/bin/python3
import json

import grequests
import jmespath

from components.posts import Post
from components.streams import Stream

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
    def __init__(self, post_streams: dict):
        """
        if issubclass(post_stream.type(), Post):
            raise TypeError("Post Stream is of wrong type: {}, expected {}".format(post_stream.type(), Post))
"""
        self._post_streams = post_streams
        self._call_stream = Stream(10, Call)
        self._to_fetch = Stream(10, dict)
        self._to_stop = []

    # Must not block or allocate
    def call(self, call):
        self._call_stream.push(call)

    def _handle_calls(self):
        # Iterate over all unhandled calls
        for call in self._call_stream:
            print("{}".format(call))

            if call.type == CALL_TYPES["FETCH"]:
                if call.args["api"] not in self._post_streams:
                    raise ValueError("Unknown api")
                self._to_fetch.push(call.args)
            elif call.type == CALL_TYPES["STOP_FETCHING"]:
                self._to_stop.append(call.args)

    def _fetch_current(self):
        to_fetch = Stream(10, dict)
        for fetch in self._to_fetch:
            self._fetch(fetch)

            # Push fetch back to stream
            if not fetch["once"]:
                # Check if a stop fetch exists for this api
                for stop_fetch in self._to_stop:
                    if stop_fetch["api"] == fetch["api"]:
                        return
                to_fetch.push(fetch)
        self._to_fetch = to_fetch

    @staticmethod
    def fetch(fetch):
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
        posts = [Post(post, fetch["api"]) for post in posts]
        # Return posts
        return posts

        ## Create and push Post objects
        # for post in posts:
        #    self._post_streams[fetch["api"]].push(post))

    def run(self):
        while True:
            # Handle outstanding calls
            self._handle_calls()
            # Handle outstanding fetches
            self._fetch_current()
