from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from data.models import Day, Sleep, HappyLog, UnhappyLog, Exercise, FoodScore, HappyScore, TestModel
from data.forms import DayForm, SleepForm, TestForm, FoodForm, ExerciseForm, HSForm, HappyForm, UnhappyForm
from django.forms.models import modelformset_factory
import datetime
from random import randint
import calendar
# Create your views here.

#CSS
GOOD = 'good_text'
OK = 'ok_text'
BAD = 'bad_text'

def get_day_list():
	day_list = Day.objects.order_by('-date')
	happy_list = HappyLog.objects.all()
	sad_list = UnhappyLog.objects.all()
	food_score = FoodScore.objects.all()
	happy_score = HappyScore.objects.all()
	exercise = Exercise.objects.all()
	sleep = Sleep.objects.all()
	
	day_log = []
	day_list = day_list[get_index_of_today():]
	for d in day_list:
		da = d.date
		happy_items = happy_list.filter(date=da)
		sad_items = sad_list.filter(date=da)
		try:
			p_score = food_score.get(date=da).p_score
			g_score = food_score.get(date=da).g_score
		except FoodScore.DoesNotExist:
			p_score = None
			g_score = None
		try:
			h_score = happy_score.get(date=da)
		except HappyScore.DoesNotExist:
			h_score = None
		exercise_items = exercise.filter(date=da)
		try:
			sleep_str = sleep.get(date=da).sleep_str()
		except Sleep.DoesNotExist:
			sleep_str = 'n/a'
		day_log.append({'day':d.date_str, 
						'happy_list':[str(h) for h in happy_items], 
						'sad_list':[str(s) for s in sad_items],
						'exercise_list':[str(e) for e in exercise_items] if exercise_items else '-',
						'p_score': p_score if p_score is not None else '-',
						'g_score': g_score if g_score is not None else '-',
						'h_score': h_score,
						'sleep': sleep_str
										})
		# day_log.append([str(d),str(happy_items)])
		
	return day_log

# returns a tuple of (avg hours slept, time in bed)
def get_sleep_summary():
	last_week = [d.date for d in last_n_days(7)]
	sleep_objects = Sleep.objects.all().filter(date__in=last_week)
	hours_slept = avg_hours_slept(sleep_objects)
	time_in_bed = avg_time_in_bed(sleep_objects)
	if hours_slept >= 7:
		css_hours = GOOD
	elif hours_slept >= 6:
		css_hours = OK
	else:
		css_hours = BAD
	return {'avg_hours_slept': hours_slept,
			'avg_time_in_bed': time_in_bed, 
			'css_hours' : css_hours}

def get_food_summary():
	last_week = [d.date for d in last_n_days(7)]
	food_objects = FoodScore.objects.all().filter(date__in=last_week)
	p_sum = sum([f.p_score for f in food_objects])
	g_sum = sum([f.g_score for f in food_objects])
	p_percent = str(100-round(float(p_sum) / 21,2)*100)
	g_percent = str(100-round(float(g_sum) / 21,2)*100)
	if p_percent >= 50:
		p_grade = GOOD
	elif p_percent >= 30:
		p_grade = OK
	else:
		p_grade = BAD
	
	if g_percent >= 80:
		g_grade = GOOD
	elif g_percent >= 50:
		g_grade = OK
	else:
		g_grade = BAD
	
	return {'p_percent': p_percent+"%",
			'p_grade': p_grade,
			'g_percent': g_percent+"%",
			'g_grade': g_grade}
			
def get_exercise_summary():
	last_week = [d.date for d in last_n_days(7)]
	exercise_objects = Exercise.objects.all().filter(date__in=last_week)
	days = percent_days_exercised(exercise_objects,last_week)
	types = types_exercised(exercise_objects)
	if days >= 6:
		day_grade = GOOD
	elif days >= 4:
		day_grade = OK
	else:
		day_grade = BAD
	return {'days': days,
			'types': types,
			'day_grade': day_grade }
			
def get_happiness_summary():
	last_week = [d.date for d in last_n_days(7)]
	happy_objects = HappyLog.objects.all().filter(date__in=last_week)
	hs_objects = HappyScore.objects.all().filter(date__in=last_week)
	rand_happiness = happy_objects[randint(0,len(happy_objects)-1)]
	avg_hs = round(sum([h.score for h in hs_objects])/float(len(hs_objects)),1)
	
	if avg_hs >= 7:
		happy_grade = GOOD
	if avg_hs >= 5:
		happy_grade = OK
	else:
		happy_grade = BAD

	return {'rand_happiness' : rand_happiness,
			'avg_hs' : avg_hs,
			'happy_grade' : happy_grade }

def get_today():
	t = datetime.datetime.now() - datetime.timedelta(hours=7)
	return datetime.date(t.year,t.month,t.day)

def get_index_of_today():
	all_days = Day.objects.order_by('-date')
	try:
		today = Day.objects.get(date=get_today())
		index = 0
		while True:
			if all_days[index] == today:
				return index
			print(all_days[index],index)
			index += 1
	except:
		return 0

def last_n_days(n):
	all_days = Day.objects.order_by('-date')
	today_index = get_index_of_today()
	if len(all_days)-today_index >= n:
		print(all_days[today_index:today_index+n])
		return all_days[today_index:today_index+n]
	print('here')
	return all_days[today_index:]

def objects_given_days(dates):
	return objects.filter(date__in=dates)
	
def duration(start,end):
    startdelta=datetime.timedelta(hours=start.hour,minutes=start.minute,seconds=start.second)
    enddelta=datetime.timedelta(hours=end.hour,minutes=end.minute,seconds=end.second)
    return (enddelta-startdelta).seconds/float(60)/float(60)

# def utc_to_local(utc_dt):
#     # get integer timestamp to avoid precision lost
#     timestamp = calendar.timegm(utc_dt.timetuple())
#     local_dt = datetime.fromtimestamp(timestamp)
#     assert utc_dt.resolution >= timedelta(microseconds=1)
#     return local_dt.replace(microsecond=utc_dt.microsecond)
		
## SLEEP HELPERS ## 

# given a set of sleep objects, calculate hours slept
def avg_hours_slept(sleep_objects):
	hours_array = []
	for s in sleep_objects:
		hours_array.append(s.total_sleep_hours())
	return round(float(sum(hours_array)) / len(hours_array),1)

# calculate average time i went to bed
def avg_time_in_bed(sleep_objects):
	time_sum = 0
	times = [time_to_absolute(s.time_slept) for s in sleep_objects]
	for t in times:
		time_sum += t.minute + t.hour*60
	avg = int(time_sum/float(len(sleep_objects)))
	return absolute_to_time(datetime.time(avg/60, avg%60))

def time_to_absolute(time):
	if time < datetime.time(12,0):	#before 12pm
		return datetime.time(time.hour+12,time.minute)
	else:
		return datetime.time(time.hour-12,time.minute)

def absolute_to_time(time):
	if time > datetime.time(12,0):	
		return datetime.time(time.hour-12,time.minute)
	else:
		return datetime.time(time.hour+12,time.minute)

## FOOD HELPERS ##
	
def percent_days_exercised(exercise_objects,date_list):
	num_days = len(date_list)
	days_no_ex = 0
	for d in date_list:
		if not exercise_objects.filter(date=d):
			days_no_ex += 1
	return num_days - days_no_ex

def types_exercised(exercise_objects):
	types = set()
	for e in exercise_objects:
		if e.exercise_type not in types:
			types.add(e.exercise_type)
	return types

def get_today_str():
	return get_today().strftime('%Y%m%d')

def get_day_before_str(date):
	return (date-datetime.timedelta(days=1)).strftime('%Y%m%d')

def get_day_after_str(date):
	return (date+datetime.timedelta(days=1)).strftime('%Y%m%d')

#returns array for graphing sleep
def sleep_array():
	sleep = Sleep.objects.all()
	sleep_array = [[0,24]]
	for i in range(0,29):
		s = sleep[i]
		bed_hours = duration(s.time_slept,s.time_awake)
		time_slept = (s.time_slept.hour+s.time_slept.minute/float(60) + 6) % 24 # start at 6pm
		sleep_array.append([time_slept, bed_hours])	
	return sleep_array
		
# assume three meals a day
# input = list of gluten free or paleo scores
def percent_healthy_meals(food_scores):
	return float(sum(food_scores)) / len(food_scores)*3
	
# def percent_days_exercised(exercise_objects,num_days):
# 	exercise_objects.filter
	
#returns a string
# def calculate_sleep(s):
# 	bed_hours = duration(s.time_slept,s.time_awake) + float(s.hours_napped)
# 	if s.hours_napped > 0: 
# 		return str(round(bed_hours,1)) + " (" + str(s.hours_napped) +")"
# 	return round(bed_hours,1)
# 
# def calculate_sleep_hours(s):
# 	return duration(s.time_slept,s.time_awake) + float(s.hours_napped)

# pages
def index(request):
	template = loader.get_template('data/index.html')
	context = RequestContext(request, {
		'day_log' : get_day_list(),
		'today_str' : get_today_str()
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

def summary(request):
	template = loader.get_template('data/summary.html')
	context = RequestContext(request, {
		'sleep_summary' : get_sleep_summary(),
		'food_summary' : get_food_summary(),
		'exercise_summary' : get_exercise_summary(),
		'happy_summary' : get_happiness_summary(),
		'good_text' : 'good_text',
		'today_str' : get_today_str()
	})
	return HttpResponse(template.render(context))
	
def edit(request,date):
	try:
		formatted_date = date[0:4]+'-'+date[4:6]+'-'+date[6:]
		try:
			current_day = Day.objects.get(date=formatted_date)
		except:
			current_day = Day(date=formatted_date)
			current_day.save()
	except:
		return HttpResponse("fail")
	datetime_date = datetime.date(int(date[0:4]),int(date[4:6]),int(date[6:]))
	day_before_str = get_day_before_str(datetime_date)
	day_after_str = get_day_after_str(datetime_date)
	happy_formset = None
	HappyFormSet = modelformset_factory(HappyLog, exclude=('day','date',),extra=1)
	UnhappyFormSet = modelformset_factory(UnhappyLog, exclude=('day','date',),extra=1)
	ExerciseFormSet = modelformset_factory(Exercise, exclude=('day','date',))

	# saving content
	if request.method =='POST':
		try:
			sleep_instance = Sleep.objects.get(day=current_day)
			sleep_form = SleepForm(request.POST, prefix = 'sleep', instance=sleep_instance)
		except:
			sleep_form = SleepForm(request.POST, prefix = 'sleep')
		try:
			inst = FoodScore.objects.get(day=current_day)
			food_form = FoodForm(request.POST, prefix = 'food', instance=inst)
		except:
			food_form = FoodForm(request.POST,prefix = 'food')
		try:
			inst = HappyScore.objects.get(day=current_day)
			hs_form = HSForm(request.POST, prefix = 'hs', instance=inst)
		except:
			hs_form = HSForm(request.POST,prefix = 'hs')
		
		happy_formset = HappyFormSet(request.POST, prefix = 'happy')
		unhappy_formset = UnhappyFormSet(request.POST, prefix = 'unhappy')
		exercise_formset = ExerciseFormSet(request.POST, prefix = 'exercise')
		
		for formset in [happy_formset, unhappy_formset, exercise_formset]:
			instances = formset.save(commit=False)
			for i in instances:
				if i.day == None:
					i.day = current_day
					i.date = current_day.date
				i.save()
		
		for form in [sleep_form, food_form, hs_form]:
			if form.is_valid():
				new_data = form.save(commit=False)
				new_data.day = current_day
				new_data.date = current_day.date
				new_data.save()
	
	# creating forms
	try:
		sleep_instance = Sleep.objects.get(day=current_day)
		sleep_form = SleepForm(prefix = 'sleep', instance=sleep_instance)
	except:
		sleep_form = SleepForm(prefix = 'sleep')
	try:
		inst = FoodScore.objects.get(day=current_day)
		food_form = FoodForm(prefix = 'food', instance=inst)
	except:
		food_form = FoodForm(prefix = 'food')
	try:
		inst = HappyScore.objects.get(day=current_day)
		hs_form = HSForm(prefix = 'hs', instance=inst)
	except:
		hs_form = HSForm(prefix = 'hs')
	happy_formset = HappyFormSet(prefix = 'happy', queryset=HappyLog.objects.filter(day=current_day))
	unhappy_formset = UnhappyFormSet(prefix = 'unhappy',queryset=UnhappyLog.objects.filter(day=current_day))
	exercise_formset = ExerciseFormSet(prefix = 'exercise',queryset=Exercise.objects.filter(day=current_day))
		
	return render(request, 'data/edit.html', {
		'current_day': current_day,
		'sleep_form': sleep_form,
		'food_form': food_form,
		'hs_form': hs_form,
		'happy_formset': happy_formset,
		'unhappy_formset': unhappy_formset,
		'exercise_formset': exercise_formset,
		'day_before_str':day_before_str,
		'day_after_str':day_after_str,
		'today_str': get_today_str()
		
	})
	