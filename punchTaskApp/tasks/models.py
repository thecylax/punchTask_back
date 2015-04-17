from django.db import models
from django.contrib.auth.models import User

STATUS = (
    ('U', 'Unconfirmed'),
    ('N', 'New'),
    ('A', 'Assigned'),
    ('R', 'Reopened'),
    ('C', 'Closed'),
)
class Task(models.Model):
    ticket = models.IntegerField(unique=True)
    product = models.CharField(max_length=80)
    component = models.CharField(max_length=80)
    assignee = models.ForeignKey(User)
    status =  models.CharField(max_length=15, default='U', choices=STATUS)
    desc = models.TextField(blank=True)
    #owner = models.ForeignKey(User)
    #modified_on = 
    created_on = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'tasks'
        
    def __unicode__(self):
        return u"%s" % self.product
        
    @models.permalink
    def get_absolute_url(self):
        return 'task_detail', [self.ticket]
    
    @models.permalink
    def get_update_url(self):
        return 'task_update', [self.ticket]
    
    @models.permalink
    def get_delete_url(self):
        return 'task_delete', [self.ticket]
    
