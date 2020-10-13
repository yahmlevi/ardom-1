from multiprocessing import Process, Pipe



def send_to_first(conn):
    conn.send("yahm")
    conn.close()


def send_to_second(conn):
    conn.send("yahm1")
    conn.close()


if __name__ == '__main__':
    first, second = Pipe()

    p = Process(target=send_to_second, args=(second,))
    p.start()

    p1 = Process(target=send_to_first, args=(first,))
    p1.start()

    print(first.recv())
    print(second.recv())

    p.join()
    p1.join()