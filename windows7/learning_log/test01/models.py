from django.db import models

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text =models.CharField(max_length=200)
    date_added =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text
class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        '''嵌套的meta类是为了让entries成为条目名称,管理多个条目.meta存储用于管理模型的额外信息'''
        verbose_name_plural='entries'

    def __str__(self):
        '''返回模型的字符串表示,为了显示效果,取前50个字符友好化显示'''
        return self.text[:50]+'...'
