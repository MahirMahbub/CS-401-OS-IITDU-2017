# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:47:44 2017

@author: Mahir Mahbub Srizon

Only Supported in Python 3.6 or further
"""


def interval_Append()-> None:
    ys.append(float(psutil.cpu_percent(interval=None)))
    xs.append(float(datetime.now().second+(datetime.now().minute*60)+(
            datetime.now().hour*3600)))
    labels.append(str(datetime.now().strftime("%H:%M:%S")))


def interval_Pop()-> None:
    xs.pop(0)
    ys.pop(0)
    labels.pop(0)


def animate(i: int) -> None:
    interval_Append()
    if len(xs) > 15:
        interval_Pop()
    ax1.clear()
    ax1.plot(xs, ys)
    plt.grid(True)
    plt.yticks(np.arange(0, 105, 5.0))
    plt.xticks(xs, labels)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib import style
    import psutil
    import time as _time
    from datetime import datetime
    from typing import List, get_type_hints
    import numpy as np
    style.use('ggplot')  # Style Sheet
    fig: object = plt.figure()
    ax1: object = fig.add_subplot(1, 1, 1)
    ys: List[float] = []
    ys.append(float(psutil.cpu_percent(interval=None)))
    xs: List[float] = []
    xs.append(float(datetime.now().second+(datetime.now().minute*60)+(
            datetime.now().hour*3600)))
    labels: List[str] = []
    labels.append(str(datetime.now().strftime("%H:%M:%S")))
    _time.sleep(2)
    ani: object = animation.FuncAnimation(fig, animate, interval=2000, blit=False)
    plt.show()
    dic = get_type_hints(animate)
