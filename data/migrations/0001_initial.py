# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'data_day', (
            ('date', self.gf('django.db.models.fields.DateField')(primary_key=True)),
        ))
        db.send_create_signal(u'data', ['Day'])

        # Adding model 'Sleep'
        db.create_table(u'data_sleep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time_slept', self.gf('django.db.models.fields.TimeField')()),
            ('time_awake', self.gf('django.db.models.fields.TimeField')()),
            ('hours_napped', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'data', ['Sleep'])

        # Adding model 'HappyLog'
        db.create_table(u'data_happylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data', ['HappyLog'])

        # Adding model 'UnhappyLog'
        db.create_table(u'data_unhappylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data', ['UnhappyLog'])

        # Adding model 'Exercise'
        db.create_table(u'data_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('exercise_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('exercise_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Exercise'])

        # Adding model 'HappyScore'
        db.create_table(u'data_happyscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'data', ['HappyScore'])

        # Adding model 'FoodScore'
        db.create_table(u'data_foodscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('p_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('g_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['FoodScore'])

        # Adding model 'Work'
        db.create_table(u'data_work', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time_start_work', self.gf('django.db.models.fields.TimeField')()),
            ('time_left_work', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'data', ['Work'])

        # Adding model 'TestModel'
        db.create_table(u'data_testmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['data.Day'], unique=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data', ['TestModel'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'data_day')

        # Deleting model 'Sleep'
        db.delete_table(u'data_sleep')

        # Deleting model 'HappyLog'
        db.delete_table(u'data_happylog')

        # Deleting model 'UnhappyLog'
        db.delete_table(u'data_unhappylog')

        # Deleting model 'Exercise'
        db.delete_table(u'data_exercise')

        # Deleting model 'HappyScore'
        db.delete_table(u'data_happyscore')

        # Deleting model 'FoodScore'
        db.delete_table(u'data_foodscore')

        # Deleting model 'Work'
        db.delete_table(u'data_work')

        # Deleting model 'TestModel'
        db.delete_table(u'data_testmodel')


    models = {
        u'data.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {'primary_key': 'True'})
        },
        u'data.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'exercise_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exercise_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'data.foodscore': {
            'Meta': {'object_name': 'FoodScore'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'g_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.happylog': {
            'Meta': {'object_name': 'HappyLog'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data.happyscore': {
            'Meta': {'object_name': 'HappyScore'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'data.sleep': {
            'Meta': {'object_name': 'Sleep'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'hours_napped': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_awake': ('django.db.models.fields.TimeField', [], {}),
            'time_slept': ('django.db.models.fields.TimeField', [], {})
        },
        u'data.testmodel': {
            'Meta': {'object_name': 'TestModel'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'day': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['data.Day']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'data.unhappylog': {
            'Meta': {'object_name': 'UnhappyLog'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data.work': {
            'Meta': {'object_name': 'Work'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_left_work': ('django.db.models.fields.TimeField', [], {}),
            'time_start_work': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['data']