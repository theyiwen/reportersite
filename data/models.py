from django.db import models
import datetime

# Create your models here.

# one day
class Day(models.Model):
    date = models.DateField(primary_key=True)
    
    def date_str(self):
        return self.date.strftime("%m/%d/%y")
    
    def __unicode__(self):  
            return str(self.date)
    
# once a day
class Sleep(models.Model):
    day = models.OneToOneField(Day, blank=True, null=True) 
    date = models.DateField()
    time_slept = models.TimeField(blank=True)
    time_awake = models.TimeField(blank=True)
    hours_napped = models.DecimalField(blank=True,max_digits=4,decimal_places=2)

    def total_sleep_hours(self):
        return self.duration(self.time_slept,self.time_awake) + float(self.hours_napped) 
        
    def total_sleep_str(self):
        sleep_hours = self.total_sleep_hours()
        if self.hours_napped > 0: 
            return str(round(sleep_hours,1)) + " (" + str(self.hours_napped) +")"
        return round(sleep_hours,1)
        
    def sleep_str(self):
        output_str = self.time_slept.strftime("%I:%M %p") + " - " + self.time_awake.strftime("%I:%M %p")
        sleep_hours_str = format(self.total_sleep_hours(), '.2f').rstrip('0').rstrip('.')
        output_str = output_str + " (" + sleep_hours_str  + ")"
        return output_str
        
    def duration(self,start,end):
        startdelta=datetime.timedelta(hours=start.hour,minutes=start.minute,seconds=start.second)
        enddelta=datetime.timedelta(hours=end.hour,minutes=end.minute,seconds=end.second)
        return (enddelta-startdelta).seconds/float(60)/float(60)
        
    # def total_sleep_str(self):
    #   sleep_hours = self.total_sleep_hours()
    #   if self.hours_napped > 0: 
    #       return str(round(sleep_hours,1)) + " (" + str(self.hours_napped) +")"
    #   return round(sleep_hours,1)
    #   
    # def __unicode__(self):
    #       return [self.time_slept, self.time_awake, self.hours_napped]

# many times a day
class HappyLog(models.Model):
    day = models.ForeignKey(Day, blank=True, null=True) 
    date = models.DateField()
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text

# many times a day
class UnhappyLog(models.Model):
    day = models.ForeignKey(Day, blank=True, null=True) 
    date = models.DateField()
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text

# many times a day
class Exercise(models.Model):
    day = models.ForeignKey(Day, blank=True, null=True) 
    date = models.DateField()
    exercise_type = models.CharField(max_length=50)
    exercise_time = models.IntegerField(blank=True, null=True) #minutes
    
    def __unicode__(self):
        if self.exercise_time:
            return self.exercise_type + " " + str(self.exercise_time)
        return self.exercise_type


class HappyScore(models.Model):
    day = models.OneToOneField(Day, blank=True, null=True) 
    date = models.DateField()
    score = models.IntegerField(blank=True)
    def __unicode__(self):
        return str(self.score)

# once a day
class FoodScore(models.Model):
    day = models.OneToOneField(Day, blank=True, null=True) 
    date = models.DateField()
    p_score = models.IntegerField(blank=True, null=True) #paleo
    g_score = models.IntegerField(blank=True, null=True) 
    def __unicode__(self):
            return str(self.p_score) + ", " + str(self.g_score)

class Work(models.Model):
    day = models.OneToOneField(Day, blank=True, null=True) 
    date = models.DateField()
    time_start_work = models.TimeField()
    time_left_work = models.TimeField()
    
class TestModel(models.Model):
    day = models.OneToOneField(Day)
    content = models.CharField(max_length=200)
