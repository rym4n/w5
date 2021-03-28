#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def scan(Target, Ports, Protocol):
    try:
        import nmap
    except:
        logger.info("[nmap] 导入 python-nmap 模块失败, 请输入命令 pip install python-nmap")
        return {"status": 2, "result": "缺少 python-nmap 模块，请 pip install python-nmap 安装"}

    logger.info("[nmap] APP执行参数为：{target} {ports} {protocol}", target=Target, ports=Ports, protocol=Protocol)

    nm = nmap.PortScanner()

    args = '-T4 -sV'

    if Protocol == 'udp':
        args = '-sU --privileged'

    nm.scan(Target, ports=Ports, arguments=args)

    return {"status": 0, "result": str(nm.analyse_nmap_xml_scan()['scan'])}
