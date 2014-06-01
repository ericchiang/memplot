#! /usr/bin/env python

from time import sleep
from datetime import datetime

import matplotlib.pyplot as plt

import psutil
import subprocess
import sys

__all__ = ["memplot"]

def memplot(cmd,wait_time=0.05):
    usage = []
    p = subprocess.Popen(cmd.split())
    util_process = psutil.Process(p.pid)
    while util_process.status() != psutil.STATUS_ZOMBIE:
        stats = util_process.memory_info()
        usage.append((datetime.now(),
                      stats.rss,
                      stats.vms,))
        sleep(wait_time)

    t,rss,vms = zip(*usage)

    rss = map(lambda mem: mem / float(2**20), rss)
    plt.plot_date(x=t,y=rss,fmt="b-")
    plt.title(cmd)
    plt.ylabel("Memory Usage (mb)")
    plt.xlabel("Time")
    plt.grid(True)
    plt.show()

