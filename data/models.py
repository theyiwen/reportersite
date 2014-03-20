from django.db import models
# Create your models here.

# one day
class Day(models.Model):
  date = models.DateField()
  def __unicode__(self):  
      return str(self.date)
  
# once a day
class Sleep(models.Model):
  day = models.OneToOneField('Day')
  time_slept = models.TimeField()
  time_awake = models.TimeField()
  hours_napped = models.DecimalField(max_digits=4,decimal_places=2)
  # def __unicode__(self):
  #   return [self.time_slept, self.time_awake, self.hours_napped]

# many times a day
class HappyLog(models.Model):
  day = models.ForeignKey('Day')
  text = models.CharField(max_length=200)
  def __unicode__(self):
    return self.text

# many times a day
class UnhappyLog(models.Model):
  day = models.ForeignKey('Day')
  text = models.CharField(max_length=200)
  def __unicode__(self):
    return self.text

# many times a day
class Exercise(models.Model):
  day = models.ForeignKey('Day')
  exercise_type = models.CharField(max_length=50)
  exercise_time = models.IntegerField(blank=True) #minutes
  def __unicode__(self):
    return self.exercise_type + " " + str(self.exercise_time)

class HappyScore(models.Model):
  day = models.ForeignKey('Day')
  score = models.IntegerField()
  def __unicode__(self):
    return str(self.score)

# once a day
class FoodScore(models.Model):
  day = models.OneToOneField('Day')
  p_score = models.IntegerField(blank=True, null=True) #paleo
  g_score = models.IntegerField(blank=True, null=True) 
  def __unicode__(self):
      return str(self.p_score) + ", " + str(self.g_score)



  