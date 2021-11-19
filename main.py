import asyncio
import logging
import os
import sys

import aiohttp.web as aiohttp_web
import aiojobs


class App:
    def __init__(
            self,
            aio_app: aiohttp_web.Application,
            job_scheduler: aiojobs.Scheduler,
    ) -> None:
        self._aio_app = aio_app
        self._job_scheduler = job_scheduler

    @classmethod
    async def create(cls) -> "App":
        logging.basicConfig(level=logging.DEBUG)
        job_scheduler = await aiojobs.create_scheduler(close_timeout=10.0)
        aio_app = aiohttp_web.Application()

        application = cls(
            aio_app=aio_app,
            job_scheduler=job_scheduler,
        )

        return application

    async def start_jobs(self):
        pass
        # Not a single job was launched

    async def start_server(self):
        try:
            await aiohttp_web._run_app(
                app=self._aio_app,
                host="127.0.0.1",
                port=2000,
            )
        except asyncio.CancelledError:
            logging.info("HTTP server has been interrupted")

    async def dispose(self):
        try:
            await self._job_scheduler.close()
        except asyncio.CancelledError:
            # See: https://github.com/aio-libs/aiojobs/issues/252
            logging.exception("Failed to dispose job scheduler")
        else:
            logging.info("Background job scheduler has been disposed")


async def run() -> None:
    app = await App.create()

    try:
        await app.start_jobs()
        await app.start_server()
    finally:
        await app.dispose()


def main():
    try:
        asyncio.run(run())
    except SystemExit:
        sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
