group1 = ["10.150.4.150", "10.150.4.167", "10.161.212.38",  "10.150.4.191", "10.134.184.61", "10.76.17.1",
          "10.195.227.1", "10.172.112.114", "10.134.173.5", "10.134.99.129", "10.150.4.242", "10.150.4.176",
          "10.148.54.31", "10.148.55.208", "10.142.214.11", "10.142.214.13", "10.122.40.80", "10.122.40.82",
          "10.122.40.84", "10.134.166.80", "10.207.239.239", "10.150.4.127", "10.148.55.99"]

group2 = ["10.173.172.114", "10.172.113.210", "10.195.227.2", "10.195.227.3", "10.76.17.2", "10.150.4.151",
          "10.150.4.154", "10.150.4.168", "10.150.4.192", "10.150.4.194", "10.150.4.161", "10.150.7.33",
          "10.150.7.41", "10.195.227.38", "10.148.55.178", "10.148.55.32", "10.148.55.238", "10.134.184.60",
          "10.161.212.39", "10.142.214.12", "10.142.214.14", "10.122.40.81", "10.122.40.83", "10.122.40.85",
          "10.148.10.5", "10.134.99.163", "10.148.55.89"]

except_group = ["10.150.4.194"]


def reboot_server(ip, inp):

    try:
        import socket
        ip_port = (ip, 9999)
        sk = socket.socket()
        sk.connect(ip_port)
        sk.settimeout(5)
        data = sk.recv(1024).decode()         # 接收服务端连接状态
        print('Connection status: ', data)
        if inp == "reboot":
            pwd = "Datacenter@2018@99"
            sk.sendall(pwd.encode())
            data2 = sk.recv(1024).decode()   # 接收服务端认证状态
            print('Server:', data2)

        inp = inp
        sk.sendall(inp.encode())
        data3 = sk.recv(1024).decode()       # 接收服务端结果
        print('Server:', data3)

        inp2 = "exit"
        sk.sendall(inp2.encode())            # 发送退出连接
        sk.close()
    except ConnectionRefusedError:
        print("Services is not running")
    except TimeoutError:
        print("Server is down")


if __name__ == "__main__":
    user_inp = input('[ <reboot> or <uptime> ] Please input command: ')
    for i in group1:
        print('='*100)
        print('Server ip: ', i)
        reboot_server(i, user_inp)
