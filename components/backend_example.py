from threading import Thread

from backend import Backend, Call, CALL_TYPES
from streams import Stream

FETCH_STREAM_LENGTH = 10
CALL_STREAM_LENGTH = 10
POST_STREAM_LENGTH = 10

post_stream = Stream(POST_STREAM_LENGTH, Post)
call_stream = Stream(CALL_STREAM_LENGTH, Call)

# Pass references to streams to new backend instance
backend = Backend(post_stream, call_stream)

# Start the backend in a new thread
backend_thread = Thread(target=backend.run)
backend_thread.start()

# Push a Call to the call stream
call_stream.push(Call(
    CALL_TYPES["FETCH"], {
        # TODO
        "once": True
    }
))
