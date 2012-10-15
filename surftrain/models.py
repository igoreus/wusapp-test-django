from django.db import models
import datetime
from django.utils import timezone

STATUSES = {'scheduled': 'Scheduled',
            'ongoing': 'Ongoing',
            'arrived': 'Arrived'
            }

class StatusTrainException(Exception):
    pass

class TrainManager(models.Manager):

    def get_scheduled(self):
        return super(TrainManager, self).get_query_set().filter(departure__gt=datetime.datetime.now())

    def get_ongoing(self):
        return super(TrainManager, self).get_query_set().filter(departure__lt=datetime.datetime.now(),\
            arrival__isnull=True)

    def get_arrived(self):
        return super(TrainManager, self).get_query_set().filter(arrival__isnull=False)

class Train(models.Model):
    """
        Consists schedule of trains
    """
    user = models.CharField(max_length=50, blank=False, verbose_name='User')
    description = models.CharField(max_length=50, blank=False, verbose_name='Description')
    departure = models.DateTimeField(verbose_name='Departure time')
    arrival = models.DateTimeField(null=True, blank=True, verbose_name='Arrival time')

    objects = StatusTrainException()

    @property
    def status(self):
        """
            Getter for status. status calculates depending on time departure and arrival.
        """
        now = timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone())
        if self.departure > now:
            status = STATUSES['scheduled']
        elif self.departure < now and self.arrival == None:
            status = STATUSES['ongoing']
        elif self.arrival < now:
            status = STATUSES['arrived']
        else:
            raise StatusTrainException('Error status')
        return status

    def __unicode__(self):
        return u'%s Created by: %s' % (self.description, self.user)

    class Meta:
        verbose_name_plural = 'Trains'
        verbose_name = 'Train'
