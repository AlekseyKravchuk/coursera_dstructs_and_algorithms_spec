from collections import deque
from collections import namedtuple


class Buffer(deque):
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.dropped_packets = deque()

    def has_free_space(self):
        return bool(len(self) < self.buffer_size)

    def has_dropped_packets(self):
        return bool(len(self.dropped_packets))


def main():
    buf_size, n = map(int, input().split())  # S: buffer size, n: number of packets arrived
    buf = Buffer(buf_size)
    Packet = namedtuple('Packet', ['arrival_time', 'time2process'])

    if n:
        packet = Packet(*map(int, input().split()))
        print(packet.arrival_time)  # start to handle first packet
        ready2proc_time = sum(packet)
        buf.append(packet)

        for i in range(n - 1):
            packet = Packet(*map(int, input().split()))

            if packet.arrival_time < ready2proc_time:  # i.e. previous packet is still being processed
                if buf.has_free_space():
                    buf.append(packet)
                    continue
                else:  # there is no free space in buffer
                    buf.dropped_packets.append(-1)
                    continue
            else:  # if packet.arrival_time >= ready2proc_time
                while buf:
                    buf.popleft()
                    print(ready2proc_time)
                    next_packet_time = ready2proc_time + buf[0].time2process
                    if packet.arrival_time >= next_packet_time:
                        print(ready2proc_time)
                        packet_from_buf = buf.popleft()
                        ready2proc_time += packet_from_buf.time2process
                        continue
                    else:
                        break
                while buf.has_dropped_packets():
                    print(buf.dropped_packets.popleft())

                print(ready2proc_time)
                ready2proc_time += packet.time2process
        while buf:
            print(ready2proc_time)
            packet_from_buf = buf.popleft()
            ready2proc_time += packet_from_buf.time2process
        while buf.dropped_packets:
            print(buf.dropped_packets.popleft())


if __name__ == '__main__':
    main()
