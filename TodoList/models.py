from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todolist(models.Model):

    priority = [
        ('مهمه برام', 'مهمه برام'),
        ('حسش بود انجام میدم', 'حسش بود انجام میدم'),
        ('حسش فعلا نیس', 'حسش فعلا نیس'),
    ]

    title = models.CharField(max_length=100, verbose_name='نام تسک')
    description = models.TextField(verbose_name='توضیحات تسک')
    priority = models.CharField(max_length=50, choices=priority, default='حسش بود انجام میدم', verbose_name='اولویت تسک')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد تسک')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین ویرایش تسک')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolists', verbose_name='کاربر صاحب تسک')
    is_completed = models.BooleanField(default=False, verbose_name='تسکو تموم کردی؟؟؟')

    class Meta:
        verbose_name = 'تسک'
        verbose_name_plural = 'تسک‌ها'
    

    def __str__(self):
        return self.title
