from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm, ClientForm, ServerForm, InstForm
from app.models import Topic, Entry, Client, Server, Instance
from django.shortcuts import get_object_or_404
from subprocess import call
from background_task import background
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import paramiko
import requests
import psutil
import os
import atexit
import schedule
import time


@login_required(login_url="/users/login")
def index(request):

    return render(request, 'app/index.html')

@login_required(login_url="/users/login")	
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'app/topics.html', context)

@login_required(login_url="/users/login")	
def clients(request):
    clients = Client.objects.order_by('date_added')	
    context = {'clients':clients}
    return render(request, 'app/clients.html', context)

@login_required(login_url="/users/login")
def client(request, client_id):
    client = Client.objects.get(id=client_id)
    entries = client.server_set.order_by('-date_added')
    context = {'client':client, 'entries':entries}
    return render(request, 'app/client.html', context)
	
@login_required(login_url="/users/login")	
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    if request.GET.get('refresh') == 'refresh':	
        
		
        r = requests.get("http://ibm.com")

        r.status_code
   
        r.save()
   
    context = {'topic':topic, 'entries':entries }
    return render(request,'app/topic.html',context)

@login_required(login_url="/users/login")	
def new_topic(request):

    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:topics'))
		  
    context = {'form': form}
    return render(request,'app/new_topic.html', context)

@login_required(login_url="/users/login")	
def new_client(request):

    if request.method != 'POST':
        form = ClientForm()
    else:
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:clients'))
		  
    context = {'form': form}
    return render(request,'app/new_client.html', context)

@login_required(login_url="/users/login")
def new_server(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method != 'POST':
        form = ServerForm()
    else:
        form = ServerForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.client = client
            new_entry.save()
            return HttpResponseRedirect(reverse('app:client', args=[client.id]))		  
    context = {'client':client, 'form': form}
    return render(request,'app/new_server.html', context)

@login_required(login_url="/users/login")	
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('app:topic', args=[topic.id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'app/new_entry.html', context)
 
@login_required(login_url="/users/login")	
def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
	
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:topic', args=[topic.id]))
			
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'app/edit_entry.html', context)

#def instance(request, instance_id):
 #   instance = Instance.objects.get(id=instance_id)
    #server = Server.objects.get(id=server_id)
   # i = server.ip
    #p = server.port
    #usr = server.username
    #pas = server.password
    #instances = instance.instance_set.all()
  #  context = {'instance':instance}
    
   # return render(request, 'app/instance.html', context)

@login_required(login_url="/users/login")
def server(request, server_id):
    try:
        server = Server.objects.get(id=server_id)	
        instances = server.instance_set.all()
   

 #   for k in Instance.objects.values_list('pid', flat= True).order_by('id'):
        
  #      c = k
  
    
    
        i = server.ip
        p = server.port
        usr = server.username
        pas = server.password
        mem = server.check_memory
        disk = server.check_disk
        cpu = server.check_cpu
        was = server.check_was
        users = server.check_users
        it1 = server.check_instance1
        it2 = server.check_instance2
        it3 = server.check_instance3
        it4 = server.check_instance4
        it5 = server.check_instance5
        it6 = server.check_instance6
        it7 = server.check_instance7
        it8 = server.check_instance8
        it9 = server.check_instance9
        it10 = server.check_instance10
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(i, p, usr, pas)
    
        stdin, stdout, stderr =ssh.exec_command("date '+%A %W %Y %X'")
        output_time = stdout.readline() 
	
        stdin, stdout, stderr =ssh.exec_command(mem)
        output_mem = stdout.readline() 
    	
        stdin, stdout, stderr =ssh.exec_command(disk)
        output_disk = stdout.readline()
    
        stdin, stdout, stderr =ssh.exec_command(cpu)
        output_cpu = stdout.readline()

        stdin, stdout, stderr =ssh.exec_command(was)
        output_was = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(users)
        output_users = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it1)
        output_it1 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it2)
        output_it2 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it3)
        output_it3 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it4)
        output_it4 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it5)
        output_it5 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it6)
        output_it6 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it7)
        output_it7 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it8)
        output_it8 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it9)
        output_it9 = stdout.readline()
        stdin, stdout, stderr =ssh.exec_command(it10)
        output_it10 = stdout.readline()
    #stdin, stdout, stderr =ssh.exec_command(ins)
   # output_ins = stdout.readline()
        file = open(str(server)+'.txt', 'a+')
        file.writelines(''.join(output_time)+'\n'+'Server: '+''.join(server.text)+'\n'+'Users: '+''.join(output_users)+'\n'+'\n'+'Memory usage: '+''.join(output_mem)+'\n'+'CPU usage: '+''.join(output_cpu)+'\n'+'Disk usage: '+''.join(output_disk)+'\n'+'WAS instances: '+''.join(output_was)+'\n'+'---------------------------------------------------'+'\n')
        file.close()
        ssh.close()
	
        context = {'server':server, 'instances':instances, 'output_time':output_time, 'output_disk':output_disk, 'output_mem':output_mem,'output_cpu':output_cpu, 'output_was':output_was, 'output_users':output_users, 'output_it1':output_it1, 'output_it2':output_it2, 'output_it3':output_it3, 'output_it4':output_it4, 'output_it5':output_it5, 'output_it6':output_it6, 'output_it7':output_it7, 'output_it8':output_it8, 'output_it9':output_it9, 'output_it10':output_it10}
        return render(request, 'app/server.html', context)
    except:
        return render(request, 'app/error.html')
		
		
@login_required(login_url="/users/login")	
def add_instance(request, server_id): 
    server = Server.objects.get(id=server_id)
    if request.method != 'POST':
        form = InstForm()
    else:
        form = InstForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.server = server
            new_entry.save()
            return HttpResponseRedirect(reverse('app:server', args=[server.id]))
    context = {'server': server, 'form': form}
    return render(request, 'app/add_instance.html', context)

@login_required(login_url="/users/login")
def edit_server(request, server_id):

    server = Server.objects.get(id=server_id)
    client = server.client
	
    if request.method != 'POST':
        form = ServerForm(instance=server)
    else:
        form = ServerForm(data=request.POST, instance=server)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:client', args=[client.id]))
			
    context = {'server': server, 'client': client, 'form': form}
    return render(request, 'app/edit_server.html', context)   




	
	
	
	