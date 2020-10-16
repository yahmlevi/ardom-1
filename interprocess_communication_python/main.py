from hub import Hub
from telnet_stream import Telnet_Stream
import queue
import time

# def preprocess_json(json_file):
#     data = json.load(json_file)
#     for i in data['UID']:
#         dict 'UID', i['data']

def create_telnet_stream(u_id):
    q_in = queue.Queue()
    q_out = queue.Queue()

    info = {"uid": u_id}
    thread = Telnet_Stream(info, q_in, q_out)

    return thread, q_in, q_out


if __name__ == '__main__':

    queues = {}
    threads = []

    thread_ids = ["one", "two"]

    for u_id in thread_ids:
        print ("Creating TelnetStream thread '{}'".format(u_id))
        thread, q_in, q_out = create_telnet_stream(u_id)
        queues[u_id] = {
            "uid": u_id,
            "q_in": q_in, 
            "q_out": q_out
        }
        thread.start()
        threads.append(thread)
        

    hub = Hub(queues)  
    hub.start()
  

    for thread in threads:
        thread.join()
    
    printer.join()


        
