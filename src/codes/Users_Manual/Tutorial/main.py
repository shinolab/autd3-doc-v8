import os

import numpy as np
from pyautd3 import AUTD3, Controller, Focus, Hz, Silencer, Sine
from pyautd3.link.soem import SOEM, Status


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


if __name__ == "__main__":
    with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(
        SOEM.builder().with_err_handler(err_handler),
    ) as autd:
        firmware_version = autd.firmware_version()
        print("\n".join([f"[{i}]: {firm}" for i, firm in enumerate(firmware_version)]))

        autd.send(Silencer.default())

        g = Focus(autd.geometry.center + np.array([0.0, 0.0, 150.0]))
        m = Sine(150 * Hz)
        autd.send((m, g))

        _ = input()

        autd.close()
