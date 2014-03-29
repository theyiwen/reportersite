from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from data.models import Day, Sleep, HappyLog, UnhappyLog, Exercise, FoodScore, HappyScore
import datetime
# Create your views here.

def get_day_list():
	day_list = Day.objects.order_by('-date')
	happy_list = HappyLog.objects.all()
	sad_list = UnhappyLog.objects.all()
	food_score = FoodScore.objects.all()
	happy_score = HappyScore.objects.all()
	exercise = Exercise.objects.all()
	sleep = Sleep.objects.all()
	
	day_log = []
	for d in day_list:
		happy_items = happy_list.filter(day=d)
		sad_items = sad_list.filter(day=d)
		p_score = food_score.get(day=d).p_score
		g_score = food_score.get(day=d).g_score
		h_score = happy_score.get(day=d)
		exercise_items = exercise.filter(day=d)
		sleep_str = calculate_sleep(sleep.get(day=d))
		day_log.append({'day':str(d), 
										'happy_list':[str(h) for h in happy_items], 
										'sad_list':[str(s) for s in sad_items],
										'exercise_list':[str(e) for e in exercise_items],
										'p_score': p_score if p_score is not None else 'n/a',
										'g_score': g_score if g_score is not None else 'n/a',
										'h_score': h_score,
										'sleep': sleep_str
										})
		# day_log.append([str(d),str(happy_items)])
		
	return day_log

def calculate_sleep(s):
	bed_hours = duration(s.time_slept,s.time_awake) + float(s.hours_napped)
	if s.hours_napped > 0: 
		return str(round(bed_hours,1)) + " (" + str(s.hours_napped) +")"
	return round(bed_hours,1)
	
def sleep_array():
	sleep = Sleep.objects.all()
	sleep_array = [[0,24]]
	for i in range(0,29):
		s = sleep[i]
		bed_hours = duration(s.time_slept,s.time_awake)
		time_slept = (s.time_slept.hour+s.time_slept.minute/float(60) + 6) % 24 # start at 6pm
		sleep_array.append([time_slept, bed_hours])	
	return sleep_array
	
	
def duration(start,end):
    startdelta=datetime.timedelta(hours=start.hour,minutes=start.minute,seconds=start.second)
    enddelta=datetime.timedelta(hours=end.hour,minutes=end.minute,seconds=end.second)
    return (enddelta-startdelta).seconds/float(60)/float(60)
	
def index(request):
	template = loader.get_template('data/index.html')
	context = RequestContext(request, {
		'day_log' : get_day_list()
	})
	return HttpResponse(template.render(context))

def happiness(request):
	template = loader.get_template('data/happiness.html')
	context = RequestContext(request, {
		'day_log' : get_day_list()
	})
	return HttpResponse(template.render(context))
	
def sleep(request):
	template = loader.get_template('data/sleep.html')
	context = RequestContext(request, {
		'day_log' : get_day_list(),
		'sleep_array' : sleep_array()
	})
	return HttpResponse(template.render(context))