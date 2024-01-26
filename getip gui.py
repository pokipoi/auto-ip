import wmi
from tabulate import tabulate

def get_network_adapters_info(): 
    '''在Python中，def关键字用于定义一个函数。
    在你提供的代码中，def用于定义一个名为get_network_adapters_info的函数，
    该函数用于获取网络适配器的信息并返回一个包含适配器信息的列表。
    '''

    c = wmi.WMI()
    """获取网络适配器的信息并返回一个包含适配器信息的列表。"""
    adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    """定义一个列表来存储网络适配器的信息。"""
    adapter_info = []#定义一个空列表
    for adapter in adapters:#遍历适配器列表
        ipv4_addresses = [ip for ip in adapter.IPAddress if '.' in ip]
        info = {
            "FriendlyName": adapter.Description,
            "IPAddress": ', '.join(ipv4_addresses)
        }
        adapter_info.append(info)
    return adapter_info

adapters_info = get_network_adapters_info()
table = tabulate(adapters_info, headers="keys", tablefmt="grid", numalign="center", stralign="left")

import tkinter as tk

def show_adapter_info(info):
    root = tk.Tk()
    root.configure(background="white")
    root.title("Network Adapter Information")
    label = tk.Label(root, text=table, justify="left", font=("Courier", 10))
    label.pack()
    root.mainloop()

show_adapter_info(table)

