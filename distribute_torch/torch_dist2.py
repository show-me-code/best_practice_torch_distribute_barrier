import torch.distributed as dist
import torch.multiprocessing as mp
import time
import random

def func(name, group):
    
    for i in range(10):
        print(name, i)
        time.sleep(random.random()*10)
        dist.barrier(group)


if __name__ == "__main__":
    dist.init_process_group(backend='nccl',init_method='tcp://127.0.0.1:5001', rank=1, world_size=3)
    group = dist.new_group(backend='nccl')
    p1 = mp.Process(target=func, args=('p2', group))
    p1.start()
    p1.join()