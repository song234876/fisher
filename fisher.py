from flask import Flask, request, jsonify, make_response
from app import create_app
from rx import operators as ops, Observable
from rx.scheduler import ThreadPoolScheduler, CurrentThreadScheduler, EventLoopScheduler, ImmediateScheduler
from rx.core.typing import Observer, Disposable
import rx
import multiprocessing
import time
import asyncio
import threading

# app = create_app()

pool_schedular = ThreadPoolScheduler(multiprocessing.cpu_count())


def delaySync():
    time.sleep(3)
    print("同步等待3秒")

async def delayAsync(sleep):
    print("开始等待")
    await asyncio.sleep(sleep)
    print(f"异步等待 {sleep}秒")

def doNow(*args):
    dt = time.time()
    print('dt的值为：{}，记录：{}'.format(dt ,args))


async def async_test():
    print("开始执行")
    await delayAsync(3)
    print("下一步")


def doRx():
    def subscribe(a: Observer, scheduler=None):
        print(threading.current_thread().name)
        a.on_next(1)
        a.on_completed()

    def mapper(value):
        print("立即执行")
        return value + 1

    create = rx.timer(5)
    # create = rx.create(subscribe)
    pipe = create.pipe(
        ops.map(mapper)
    )

    def on_next(value):
        print(threading.current_thread().name)
        print(value)

    pipe.subscribe(on_next)
    # observable = rx.of('A', 'B', 'C', 'D')
    # pipe = observable.pipe(
    #     ops.subscribe_on(pool_schedular),
    #     ops.map(lambda char: char + char),
    #     ops.filter(lambda char: char != 'BB')
    # )
    # pipe.subscribe(on_next=lambda value: print(value))

    # source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
    #
    # composed = source.pipe(
    #     ops.map(lambda s: len(s)),
    #     ops.filter(lambda i: i >= 5)
    # )
    # composed.subscribe(lambda value: print("Received {0}".format(value)))

async def call_later_demo(loop):
    doNow("开始")
    loop.call_later(1, doNow, '第一次，延迟一秒')
    loop.call_later(2, doNow, '第二次，延迟二秒')
    loop.call_soon(doNow, '第三次，立即调用')
    # loop.call_soon(delaySync)
    print("最后一次调用")


async def run_together():
    await asyncio.gather(delayAsync(1),delayAsync(4))

if __name__ == "__main__":
    # asyncio.run(run_together())
    # asyncio.gather(delayAsync(), delayAsync())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(call_later_demo(loop))
    doRx()
    # app.run(host="0.0.0.0", debug=True)
