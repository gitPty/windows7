import socketserver, datetime, time, psutil, os
USER_INFO = {"is_login": False}


class check_login(object):
    def __init__(self):
        pass

    def __call__(self, func):

        def inner(*args, **kwargs):
            if USER_INFO.get("is_login", None):
                ret = func(*args, **kwargs)
                return ret
            else:
                print("please login")
                return "please login"
        return inner


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            conn = self.request
            conn.sendall('Connected to the server.'.encode())
            while True:
                data = conn.recv(1024).decode()
                if data == "exit":
                    print("Disconnect from: %s" % (self.client_address,))
                    break
                elif data == "reboot":
                    res = self.reboot()
                    conn.sendall(('Command executed: <%s>, return: %s' % (data, res)).encode())
                elif data == "uptime":
                    res = self.get_time()
                    conn.sendall(('Command executed: <%s>, rteurn: %s' % (data, res)).encode())
                elif data == "help":
                    res = self.help()
                    conn.sendall(('Command executed: <%s>, return: %s' % (data, res)).encode())
                elif data == "Datacenter@2018@99":
                    res = self.login(data)
                    conn.sendall(('Command executed: <%s>, return: %s' % (data, res)).encode())
                else:
                    print("The client from <%s> sent you a message: %s" % (self.client_address, data))
                    conn.sendall(('Received the news <%s>' % data).encode())
        except ConnectionResetError:
            USER_INFO["is_login"] = False
            print("client is exit")

    def get_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        tmp = time.time() - psutil.boot_time()
        m, s = divmod(tmp, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        res = "%02d:%02d:%02d:%02d" % (d, h, m, s)
        print("current time: %s, uptime: %s" % (current_time, res))
        return "current time: %s, uptime: %s" % (current_time, res)

    @check_login()
    def reboot(self):
        os.system("shutdown -r -t 30")

    def login(self, pwd):
        # print(pwd)
        USER_INFO["is_login"] = True
        return "login is OK"

    def help(self):
        tmp = """input <reboot> reboot server，input <uptime> get system time or uptime"""
        return tmp


if __name__ == '__main__':

    server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyServer)
    print("services is running!")
    server.serve_forever()
