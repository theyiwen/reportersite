# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'UnhappyLog', fields ['day']
        db.delete_unique(u'data_unhappylog', ['day_id'])

        # Removing unique constraint on 'Exercise', fields ['day']
        db.delete_unique(u'data_exercise', ['day_id'])

        # Removing unique constraint on 'HappyLog', fields ['day']
        db.delete_unique(u'data_happylog', ['day_id'])


        # Changing field 'HappyLog.day'
        db.alter_column(u'data_happylog', 'day_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Day'], null=True))

        # Changing field 'Exercise.day'
        db.alter_column(u'data_exercise', 'day_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Day'], null=True))

        # Changing field 'UnhappyLog.day'
        db.alter_column(u'data_unhappylog', 'day_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Day'], null=True))

    def backwards(self, orm):

        # Changing field 'HappyLog.day'
        db.alter_column(u'data_happylog', 'day_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['data.Day'], unique=True, null=True))
        # Adding unique constraint on 'HappyLog', fields ['day']
        db.create_unique(u'data_happylog', ['day_id'])


        # Changing field 'Exercise.day'
        db.alter_column(u'data_exercise', 'day_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['data.Day'], unique=True, null=True))
        # Adding unique constraint on 'Exercise', fields ['day']
        db.create_unique(u'data_exercise', ['day_id'])


        # Changing field 'UnhappyLog.day'
        db.alter_column(u'data_unhappylog', 'day_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['data.Day'], unique=True, null=True))
        # Adding unique constraint on 'UnhappyLog', fields ['day']
        db.create_unique(u'data_unhappylog', ['day_id'])


    models = {
        u'data.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {'primary_key': 'True'})
        },
        u'data.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Day']", 'null': 'True', 'blank': 'True'}),
            'exercise_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exercise_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'data.foodscore': {
            'Meta': {'object_name': 'FoodScore'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['data.Day']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'g_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.happylog': {
            'Meta': {'object_name': 'HappyLog'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Day']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data.happyscore': {
            'Meta': {'object_name': 'HappyScore'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['data.Day']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'data.sleep': {
            'Meta': {'object_name': 'Sleep'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['data.Day']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Day']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data.work': {
            'Meta': {'object_name': 'Work'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['data.Day']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_left_work': ('django.db.models.fields.TimeField', [], {}),
            'time_start_work': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['data']