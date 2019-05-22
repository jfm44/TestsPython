import asyncio


if __name__ == "__main__" : 
    loop = asyncio.get_event_loop()
    loop.call_later(2, print, 'Hello')
    loop.call_later(10, print, 'World')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
