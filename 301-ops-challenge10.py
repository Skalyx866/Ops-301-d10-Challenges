#!/usr/bin/env python3

# importing psutil
import psutil

# declaring variables for various psutil functions
cpu_times = psutil.cpu_times()

# Declaring a function

def system_info():
    # print out cpu time spent by user
    print(f"Time spent by user: {cpu_times.user}")
    # print out cpu time spent by the kernel
    print(f"Time spent in kernel mode: {cpu_times.system}")
    # print out time spent while idle
    print(f"Time spent when idle: {cpu_times.idle}")
    # time spent by priority processes
    print(f"Time spent by priority processes in user mode {cpu_times.nice}")
    # time spent waiting for input/output
    print(f"Time spent waiting of I/O: {cpu_times.iowait}")
    # time spent waiting for hardware interrupts
    print(f"Time spent waiting for hardware: {cpu_times.irq}")
    # time spent waiting for software interrupts
    print(f"Time spent waiting for software interrupts: {cpu_times.softirq}")
    # time spent by other OSes in a virtualized environment
    print(f"Time spent by virtualized OSes: {cpu_times.steal}")
    # time spent by virtualized OSes controlled by the linux kernel
    print(f"Time spent by virtualized OSes controlled by the linux kernel: {cpu_times.guest}")


system_info()