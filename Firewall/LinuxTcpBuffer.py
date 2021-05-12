from netfilterqueue import NetfilterQueue
import socket

def print_and_accept(pkt):

    # if bloom_filter.check_is_not_in_filter(pkt.get_src_ip()):
    #     pkt.accept()
    # else:
    #     pkt.drop()

    print(pkt)
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
s = socket.fromfd(nfqueue.get_fd(), socket.AF_UNIX, socket.SOCK_STREAM)
try:
    nfqueue.run_socket(s)
except KeyboardInterrupt:
    print('')

s.close()
nfqueue.unbind()