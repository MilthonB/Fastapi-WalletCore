import inspect
import asyncio
from typing import TypeVar, Callable, Awaitable, Union, cast

T = TypeVar("T")

async def run_async_or_sync(
    func: Callable[..., Union[T, Awaitable[T]]],
    *args: object,
    **kwargs: object,
) -> T:
    result = func(*args, **kwargs)

    if inspect.isawaitable(result):
        return cast(T, await result)

    loop = asyncio.get_running_loop()
    return cast(
        T,
        await loop.run_in_executor(None, lambda: result)
    )
