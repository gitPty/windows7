import time

from concurrent import futures

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(0.1)
    return "我是:" + name

if __name__ == "__main__":

    name_list = ["张三", "李四", "王五"]
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_name = executor.map(show, name_list)
        print(future_to_name)
        for future in future_to_name:
            print(future)
    print("---done!---")