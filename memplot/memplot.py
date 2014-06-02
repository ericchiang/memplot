#! /usr/bin/env python

from time import sleep
from datetime import datetime

import matplotlib.pyplot as plt

import psutil
import subprocess

__all__ = ["memplot"]

def memplot(cmd,wait_time=0.05):
    usage = []
    p = subprocess.Popen(cmd)
    util_process = psutil.Process(p.pid)
    try:
        while util_process.status() != psutil.STATUS_ZOMBIE:
            stats = util_process.memory_info()
            usage.append((datetime.now(),
                          stats.rss,
                          stats.vms,))
            sleep(wait_time)
    except KeyboardInterrupt:
        # on ctrl-c kill the subprocess
        p.kill()

    t,rss,vms = zip(*usage)
    
    rss = map(lambda mem: mem / float(2**20), rss) # convert to mb
    plt.plot_date(x=t,y=rss,fmt="b-")
    plt.title(' '.join(cmd))
    plt.ylabel("Memory Usage (mb)")
    plt.xlabel("Time")
    plt.grid(True)
    plt.show()

