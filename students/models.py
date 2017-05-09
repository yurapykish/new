# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Students(models.Model):

    class Meta(object):
        verbose_name = 'Студенти',
        verbose_name_plural = 'Студенти'

    first_name = models.CharField(
        max_length=256,
        blank =False,
        verbose_name = 'Name',
    )

    last_name = models.CharField(
        max_length =256,
        blank = False,
        verbose_name ='Last name',
    )

    middle_name =models.CharField(
        max_length =256,
        blank = True,
        verbose_name = 'Middle name',
        default ='',
    )

    birthday = models.DateField(
        blank =False,
        verbose_name = 'birthday',
        null = True,
    )
    photo = models.ImageField(
        blank = True,
        verbose_name = 'Photo',
        null = True,
    )

    ticket = models.CharField(
        max_length =256,
        blank =False,
        verbose_name= 'Ticket',

    )

    notes = models.TextField(
        blank = True,
        verbose_name = 'Note'
    )
    student_group = models.ForeignKey('Groups',
                                      verbose_name = 'Групи',
                                      blank = False,
                                      null = True,
                                      on_delete = models.PROTECT,
                                      )


    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


class Groups(models.Model):

    class Meta(object):
        verbose_name = 'Групи'
        verbose_name_plural = 'Групи'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Group')
    leader = models.OneToOneField('Students', verbose_name='Староста',
                                  max_length=256,
                                  blank=True,
                                  null=True,
                                  on_delete=models.SET_NULL)
    notes = models.TextField(
        blank=True,
        verbose_name='Note')

    def __str__(self):
        if self.leader:

            return '%s(%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return "%s" % (self.title)
