~import os
~from datetime import timedelta
from pyautd3.link.soem import SOEM, Status, TimerStrategy


def err_handler(slave: int, status: Status, msg: str) -> None:
    match status:
        case Status.Error:
            print(f"Error [{slave}]: {msg}")
        case Status.Lost:
            print(f"Lost [{slave}]: {msg}")
            # You can also wait for the link to recover, without exiting the process
            os._exit(-1)
        case Status.StateChanged:
            print(f"StateChanged  [{slave}]: {msg}")


SOEM.builder()\
    .with_ifname("")\
    .with_buf_size(32)\
    .with_err_handler(
        err_handler
    )\
    .with_state_check_interval(timedelta(milliseconds=100))\
    .with_sync0_cycle(2)\
    .with_send_cycle(2)\
    .with_timer_strategy(TimerStrategy.BusyWait)\
    .with_sync_tolerance(timedelta(microseconds=1))\
    .with_sync_timeout(timedelta(seconds=10))