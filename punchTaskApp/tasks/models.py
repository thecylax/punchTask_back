from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    #address_one = models.CharField(max_length=100)
    #address_two = models.CharField(max_length=100, blank=True)
    #city = models.CharField(max_length=50)
    #state = models.CharField(max_length=2)
    #phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'tasks'
        
    def __unicode__(self):
        return u"%s" % self.name
        
    @models.permalink
    def get_absolute_url(self):
        return 'task_detail', [self.uid]
    
    @models.permalink
    def get_update_url(self):
        return 'task_update', [self.uid]
    
    @models.permalink
    def get_delete_url(self):
        return 'task_delete', [self.uid]
    
