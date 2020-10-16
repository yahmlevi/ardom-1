import time
import threading
import queue
#import json

# B SIDE
class Hub(threading.Thread):
    
    def __init__(self, queues: dict):
        threading.Thread.__init__(self)
        self.queues = queues

        self.running = True



    def run(self):
        while self.running:
            for q_item in self.queues.values():
                
                q_out: queue.Queue = q_item["q_out"]
                q_in: queue.Queue  = q_item["q_in"]

                u_id: str = q_item["uid"]

                if not q_out.empty():
                    value_from_q = q_out.get()
                    print("B SIDE: Received value '{}' from thread '{}'".format(value_from_q, u_id) )

                data = self.get_data_by_uid(u_id)
                q_in.put("B SIDE: data")   

                #else:
                #    print("queue '{}' is empty".format(u_id))
            time.sleep(1)

    def stop(self):
        self.running = False


    def get_data_by_uid(self, u_id):
        x = {"uid":"one", "data":30,
            "uid":"two", "data":40,
            "uid":"three", "data":50,
            "uid":"four", "data":80}
        print(u_id)
        
        #print(x.get[u_id])

        return "Data for {}".format(u_id)

