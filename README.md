# aiojobs-close-bug

python: 3.9.8 aiohttp: 3.8.1 aiojobs: 1.0.0

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

python3 main.py # And then press ^C
```

Traceback:

```
======== Running on http://127.0.0.1:2000 ========
(Press CTRL+C to quit)
^CINFO:root:HTTP server has been interrupted
ERROR:root:Failed to dispose job scheduler
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 629, in run_until_complete
    self.run_forever()
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 596, in run_forever
    self._run_once()
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 1890, in _run_once
    handle._run()
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
  File "/opt/homebrew/lib/python3.9/site-packages/aiohttp/web_runner.py", line 36, in _raise_graceful_exit
    raise GracefulExit()
aiohttp.web_runner.GracefulExit

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/homebrew/lib/python3.9/site-packages/aiojobs/_scheduler.py", line 129, in _wait_failed
    task = await self._failed_tasks.get()
  File "/opt/homebrew/Cellar/python@3.9/3.9.8/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/queues.py", line 166, in get
    await getter
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/evgenymarkov/Personal/aiojobs-close-bug/main.py", line 48, in dispose
    await self._job_scheduler.close()
  File "/opt/homebrew/lib/python3.9/site-packages/aiojobs/_scheduler.py", line 95, in close
    await self._failed_task
asyncio.exceptions.CancelledError
```
