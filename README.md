# Requests

Clone of requests(found at https://github.com/psf/requests), with batching logic added.
Batches are done asynchronously using asyncio+aiohttp so that wait time is less.
Batches currently support post or get requests only.
An example of usage can be seen in testBatches.py.
