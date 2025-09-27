#!/usr/bin/env python3
"""
对一组 IP 循环 tcpping，每个 100 次，输出平均延迟。
保存为 tcpping_batch.py 后直接运行即可：
    python tcpping_batch.py
"""
from tcppinglib import tcpping

IPS = [
    "13.158.164.251",
    "13.113.53.43",
    "54.238.36.18",
    "3.115.240.84",
    "52.69.254.176",
    "18.177.177.134",
    "52.194.72.203",
    "54.178.245.74",
]

COUNT = 100

def main() -> None:
    for ip in IPS:
        try:
            res = tcpping(ip, port=443, count=COUNT, interval=0.1)
            print(f"{ip:<15}  avg = {res.avg_rtt:7.3f} ms")
        except Exception as e:
            print(f"{ip:<15}  测试失败: {e}")

if __name__ == "__main__":
    main()