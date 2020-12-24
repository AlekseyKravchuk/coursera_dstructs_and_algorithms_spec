from collections import deque
from collections import namedtuple


class Buffer(deque):
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def is_not_full(self):
        return bool(len(self) < self.buffer_size)


def main():
    buf_size, n = map(int, input().split())  # S: buffer size, n: number of packets arrived
    buf = Buffer(buf_size)
    Packet = namedtuple('Packet', ['arrival_time', 'time2process'])

    for i in range(n):
        packet = Packet(map(int, input().split()))  # packet = (arrival_time, time2process)
        if buf.is_not_full():
            buf.append(packet)
            continue
        time_proc_is_free = sum(buf[0])
        if packet.arrival_time >= time_proc_is_free:
            buf.popleft()
            buf.append(packet)




if __name__ == '__main__':
    main()
