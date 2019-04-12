from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
port = 22
username = 'root'
password = '123.com'


# Create your views here.
@login_required(login_url='/login.html')
def indexView(request):
    return render(request, 'index.html')


# 用户登录
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


# 法币管理台测试环境
@login_required(login_url='/login.html')
def FabiTestView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.246', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/fiatCenterAdmin/fiatCenterAdmin/ && git pull"
            log = "cd /usr/local/releases/fiatCenterAdmin/fiatCenterAdmin/ && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/fiatCenterAdmin/fiatCenterAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            time.sleep(1)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'fabitest.html', locals())


# 法币管理台预发布环境
@login_required(login_url='/login.html')
def FabiPreView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.246', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/fiatCenterAdmin/fiatCenterAdminpre/fiatCenterAdmin && git pull"
            log = "cd /usr/local/releases/fiatCenterAdmin/fiatCenterAdminpre/fiatCenterAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/fiatCenterAdmin/fiatCenterAdminpre/fiatCenterAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'fabipre.html', locals())


# 共享者测试环境
@login_required(login_url='/login.html')
def SharerTestView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.202', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/sharer/sharersAdmin && git pull"
            log = "cd /usr/local/releases/sharer/sharersAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/sharer/sharersAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'sharertest.html', locals())


# 共享者开发环境
@login_required(login_url='/login.html')
def SharerDevView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.204', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/sharer/sharersAdmin && git pull"
            log = "cd /usr/local/releases/sharer/sharersAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/sharer/sharersAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'sharerdev.html', locals())


# 共享者预发布环境
@login_required(login_url='/login.html')
def SharerPreView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.206', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/sharer/sharersAdmin && git pull"
            log = "cd /usr/local/releases/sharer/sharersAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/sharer/sharersAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'sharerpre.html', locals())


# 币加宝测试环境
@login_required(login_url='/login.html')
def BjbTestView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.193', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/bjb/balanceAdmin && git pull"
            log = "cd /usr/local/releases/bjb/balanceAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/bjb/balanceAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'bjbtest.html', locals())


# 币加宝预发布环境
@login_required(login_url='/login.html')
def BjbPreView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.192', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/bjb/balanceAdmin && git pull"
            log = "cd /usr/local/releases/bjb/balanceAdmin && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/bjb/balanceAdmin"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'bjbpre.html', locals())


# 卢克索测试环境
@login_required(login_url='/login.html')
def BjbstaticTestView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.193', port=port, username=username, password=password)
            cmd = "cd /usr/local/releases/balanceStatic && git pull"
            log = "cd /usr/local/releases/balanceStatic && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/balanceStatic"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'bjbstatictest.html', locals())


# 卢克索预发布环境
@login_required(login_url='/login.html')
def BjbstaticPreView(request):
        msg = "更新成功！"
        try:
            ssh.connect(hostname='172.16.255.192', port=port, username=username, password=password)
            cmd = "cd  /usr/local/releases/balanceStatic && git pull"
            log = "cd /usr/local/releases/balanceStatic && git log -1"
            cmd_chown = "chown -R apache:apache /usr/local/releases/balanceStatic"
            ssh.exec_command(cmd)
            time.sleep(1)
            ssh.exec_command(cmd_chown)
            stdin, stdout, stderr = ssh.exec_command(log)
            result = stdout.read().decode()
            print(result)
        except Exception as e:
            msg = e
        return render(request, 'bjbstaticpre.html', locals())


# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('login.html')
