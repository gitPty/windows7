from django.shortcuts import render
from django.shortcuts import redirect
from django import views
from wintel_web import models
import threading
from queue import Queue

# Create your views here.


class Login(views.View):

    def get(self, request):
        return render(request, 'login.html', {'msg': ''})

    def post(self, request):
        u = ''
        p = ''
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = models.Userinfo.objects.filter(user=user)
        for i in user_obj:
            u = i.user
            p = i.passwd

        if u == '' or p == '':
            message = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': message})

        elif user == u and pwd == p:
            request.session['is_login'] = True
            request.session['username'] = user
            request.session.set_expiry(3600)    # session 过期时间, 单位秒
            return redirect('/index')

        else:
            message = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': message})


class Index(views.View):

    conn_list = []
    conn_set = ()
    reboot_list = []
    reboot_set = ()
    return_dic = {"conn": "", "reboot": "", "username": ""}

    ip_queue = Queue()  # 不加参数表示接收无限队列

    def get(self, request):
        self.return_dic["conn"] = ""
        self.return_dic["reboot"] = ""
        is_login = request.session.get('is_login')
        if is_login:
            self.return_dic["username"] = request.session.get('username')
            return render(request, 'index.html', {'result_one': self.return_dic})
        else:
            return redirect('/')

    def post(self, request):
        self.conn_list.clear()
        self.reboot_list.clear()
        self.return_dic.clear()
        login_user = request.session.get('username')
        self.return_dic["username"] = login_user
        value = list(request.POST.values())
        print('value----', value)
        ip_table = value[2:-1]
        group_one = request.POST.get('one')
        reboot_action = request.POST.get('reboot')
        uptime_action = request.POST.get('uptime')

        threads = []
        for i in ip_table:
            self.ip_queue.put(i)  # 放入队列

        if reboot_action:
            for num in range(10):       # 定义工作线程数
                thread = threading.Thread(target=self.reboot_server, args=(reboot_action, ))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # 主线程等待所有的子线程任务都处理完了，然后退出线程
        else:
            for num in range(10):
                thread = threading.Thread(target=self.reboot_server, args=(uptime_action, ))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
        threads.clear()
        if group_one:
            return render(request, 'index.html', {'result_one': self.return_dic})
        else:
            return render(request, 'index.html', {'result_two': self.return_dic})

    def reboot_server(self, action):
        import socket
        while not self.ip_queue.empty():
            ip = self.ip_queue.get()
            try:
                ip_port = (ip, 8888)
                sk = socket.socket()
                sk.connect(ip_port)
                sk.settimeout(5)
                data = sk.recv(1024).decode()
                print('Connection status:', data)
                if action == "reboot":
                    pwd = "Datacenter@2018@99"
                    sk.sendall(pwd.encode())
                    data2 = sk.recv(1024).decode()
                    print('Server:', data2)

                sk.sendall(action.encode())
                data3 = sk.recv(1024).decode()
                print('result:', data3)

                if action == 'uptime' and data3 >= str(1):
                    self.reboot_list.append(ip)
                    self.reboot_set = ('{} Server online time greater than or equal to one day.'.format(self.reboot_list))
                    self.return_dic["reboot"] = self.reboot_set
                    print(self.reboot_set)

                inp2 = "exit"
                sk.sendall(inp2.encode())  # 发送退出连接
                sk.close()

            except (ConnectionRefusedError, TimeoutError):
                self.conn_list.append(ip)
                self.conn_set = ('{} Connection failed service not running or server downtime.'.format(self.conn_list))
                self.return_dic["conn"] = self.conn_set
                print(self.conn_set)


def logout(request):
    request.session.clear()
    return redirect('/')
