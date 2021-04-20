from collections import namedtuple
from collections import deque
# ========== for debugging purposes ==========
# import os
# import re
# import sys
# import filecmp

Packet = namedtuple('Packet', ['arr_time', 'time2proc'])
Times = namedtuple('Times', ['start', 'end'])


class Buffer(deque):
    def __init__(self, S):
        self.buf_size = S
        self.real_times_cnt = 0
        self.ready2proc = 0
        super().__init__()

    def has_free_space(self):
        return bool(self.real_times_cnt < self.buf_size)

    def process_packet(self, packet):
        if self.__len__() == 0:  # buffer is empty
            self.ready2proc = sum(packet)
            self.append_time(Times(packet.arr_time, self.ready2proc))
        else:  # there are some packets in the buffer
            if packet.arr_time < self[0].end:  # leftmost packet presented by (start,end) times is still not processed
                if self.has_free_space():  # there are some free space in buf / relies on self.real_times_cnt
                    self.ready2proc = self[-1].end + packet.time2proc
                    self.append_time(Times(self[-1].end, self.ready2proc))
                else:  # buf is full / relies on self.real_times_cnt
                    self.append_time(Times(packet.arr_time, -1))  # time2proc = -1 indicates that packet was dropped
            elif packet.arr_time == self[0].end:  # leftmost packet from buf has been processed right now
                if self.real_times_cnt > 1:  # there are packets in the buffer
                    self.popleft_time()
                    start, end = self.ready2proc, self.ready2proc + packet.time2proc
                    self.append_time(Times(start, end))
                    self.ready2proc = end
                else:  # buffer will be empty after poping
                    time = self.popleft_time()
                    self.append_time(Times(time.end, time.end + packet.time2proc))
            else:  # we didn't know how many packets have been processed before the packet arrived
                while self and packet.arr_time > self[0].end:
                    self.popleft_time()
                if self:  # buffer still contain several packets (represented by times)
                    if packet.arr_time == self[0].end:
                        self.popleft_time()
                        self.append_time(Times(self[-1].end, self[-1].end + packet.time2proc))
                    if packet.arr_time < self[0].end:
                        self.append_time(Times(self[-1].end, self[-1].end + packet.time2proc))
                else:  # buffer is empty, i.e. all previous packets were successfully processed
                    self.append_time(Times(packet.arr_time, sum(packet)))

    def append_time(self, time):
        self.append(time)
        if time.end >= 0:
            self.real_times_cnt += 1

    def popleft_time(self):
        times = self.popleft()
        if times.end >= 0:
            self.real_times_cnt -= 1
            print(times.start)
            if self.real_times_cnt == 0 and self:
                while self.__len__():
                    print(-1)
                    self.popleft()
        else:  # times.end == -1
            print(-1)

        return times

    def flush(self):
        while self:
            self.popleft_time()

# ========== for debugging purposes ==========
# def main_debug(fname):
#     out_file_name = fname + '.out'
#     with open(fname, 'r') as test_file, open(out_file_name, 'w') as out_file:
#         sys.stdin = test_file
#         sys.stdout = out_file
#
#         buf_size, n = map(int, input().split())
#         if n == 0:
#             return 0
#
#         buf = Buffer(buf_size)
#         for i in range(n):
#             packet = Packet(*map(int, input().split()))
#             buf.process_packet(packet)
#
#         if buf:
#             buf.flush()


def main():
    buf_size, n = map(int, input().split())
    if n == 0:
        return 0

    buf = Buffer(buf_size)
    for i in range(n):
        packet = Packet(*map(int, input().split()))
        buf.process_packet(packet)

    if buf:
        buf.flush()


if __name__ == '__main__':
    main()

    # ========== for debugging purposes ==========
    # test_file_names = sorted(['./tests/' + f for f in os.listdir('./tests') if re.search(r'\d$', f)])
    # for test_fname in test_file_names:
    #     main(test_fname)
    #     out_fname = test_fname + '.out'
    #     correct_out_fname = test_fname + '.a'
    #     cmp_res = filecmp.cmp(out_fname, correct_out_fname, shallow=False)
    #     if not cmp_res:
    #         os.rename(out_fname, out_fname + '.FAILED')
    #
    # for test_file_name in test_file_names:
    #     main(test_file_name)

    # test_fname = './tests/20'
    # main(test_fname)
    # out_fname = test_fname + '.out'
    # correct_out_fname = test_fname + '.a'
    # cmp_res = filecmp.cmp(out_fname, correct_out_fname, shallow=False)
    # if not cmp_res:
    #     os.rename(out_fname, out_fname + '.FAILED')
