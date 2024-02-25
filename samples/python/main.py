import asyncio
import os

import numpy as np
from pyautd3 import AUTD3, ConfigureSilencer, Controller
from pyautd3.gain import Focus
from pyautd3.link.soem import SOEM, Status
from pyautd3.modulation import Sine


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


async def main() -> None:
    with await (
        Controller.builder()
        .add_device(AUTD3([0.0, 0.0, 0.0]))
        .open_async(
            SOEM.builder().with_err_handler(err_handler),
        )
    ) as autd:
        firm_info_list = await autd.firmware_info_list_async()
        print("\n".join([f"[{i}]: {firm}" for i, firm in enumerate(firm_info_list)]))

        await autd.send_async(ConfigureSilencer.default())

        g = Focus(autd.geometry.center + np.array([0.0, 0.0, 150.0]))
        m = Sine(150)
        await autd.send_async(m, g)

        _ = input()

        await autd.close_async()


if __name__ == "__main__":
    asyncio.run(main())
