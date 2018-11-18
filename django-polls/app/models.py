from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)
    code = models.CharField(max_length=100, default='000')
	
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, default=1, on_delete=models.PROTECT)
    text = models.TextField()
    code = models.CharField(max_length=100, default='000')
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
	
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
		
class Client(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.text

class Server(models.Model):
    client = models.ForeignKey(Client, default=1, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    ip = models.CharField(max_length=200, default='ip')
    port = models.CharField(max_length=200, default='22')
    username = models.CharField(max_length=200, default='username')
    password = models.CharField(max_length=200, default='password')
    check_uptime = models.CharField(max_length=500, default='check_uptime')
    check_memory = models.CharField(max_length=500, default='check_memory')
    check_disk = models.CharField(max_length=500, default='check_disk')
    check_logs = models.CharField(max_length=500, default='check_logs')
    check_cpu = models.CharField(max_length=500, default='check_cpu')
    check_was = models.CharField(max_length=500, default='check_was')
    check_users = models.CharField(max_length=200, default='check_users')
    check_instance1 = models.CharField(max_length=500, default='check_instance1')
    check_instance2 = models.CharField(max_length=500, default='check_instance2')
    check_instance3 = models.CharField(max_length=500, default='check_instance3')
    check_instance4 = models.CharField(max_length=500, default='check_instance4')
    check_instance5 = models.CharField(max_length=500, default='check_instance5')
    check_instance6 = models.CharField(max_length=500, default='check_instance6')
    check_instance7 = models.CharField(max_length=500, default='check_instance7')
    check_instance8 = models.CharField(max_length=500, default='check_instance8')
    check_instance9 = models.CharField(max_length=500, default='check_instance9')
    check_instance10 = models.CharField(max_length=500, default='check_instance10')
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    
    class Meta:
        verbose_name_plural = 'servers'
    
    def __str__(self):
        return self.text[:50] + "..."
		
class Instance(models.Model):
    server = models.ForeignKey(Server, default=1, on_delete=models.PROTECT)
    text=models.CharField(max_length=200, default='instance_name')
    pid=models.CharField(max_length=300, default='pid')
    status=models.CharField(max_length=300, default='status')
	
    class Meta:
        verbose_name_plural = 'instances'
    
    def __str__(self):
        return self.text[:50] + "..."

    
   


    