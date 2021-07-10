#!/bin/python3

from threading import Thread

from backend import Backend, Call, CALL_TYPES
from posts import Post
from streams import Stream

FETCH_STREAM_LENGTH = 10
CALL_STREAM_LENGTH = 10
POST_STREAM_LENGTH = 100

post_stream = Stream(POST_STREAM_LENGTH, Post)
call_stream = Stream(CALL_STREAM_LENGTH, Call)

# Pass references to streams to new backend instance
backend = Backend(post_stream, call_stream)

# Start the backend in a new thread
backend_thread = Thread(target=backend.run)
backend_thread.start()

# Push a Call to the call stream
backend.call(Call(
    CALL_TYPES["FETCH"], {
        "api": "reddit.json",
        "once": False
    }
))

post = None

while post is None:
    post = post_stream.pop()

while post is not None:
    post = post_stream.pop()

print("Received more posts")

backend.call(Call(
    CALL_TYPES["STOP_FETCHING"], {
        "api": "reddit.json",
        "once": False
    }
))

print("Made call")

while True:
    while post is None:
        post = post_stream.pop()

    while post is not None:
        post = post_stream.pop()

    print("Received more posts")
