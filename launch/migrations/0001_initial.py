# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('launch_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clocks', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('fuses', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('drawpile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Hand'], related_name='drawpile', null=True)),
            ('discardpile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Hand'], related_name='discardpile', null=True)),
            ('launchpad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Hand'], related_name='launchpad', null=True)),
            ('ispublic', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('launch', ['Game'])

        # Adding M2M table for field players on 'Game'
        m2m_table_name = db.shorten_name('launch_game_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['launch.game'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding model 'Hand'
        db.create_table('launch_hand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Game'])),
        ))
        db.send_create_signal('launch', ['Hand'])

        # Adding model 'Card'
        db.create_table('launch_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suit', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('hand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Hand'])),
        ))
        db.send_create_signal('launch', ['Card'])

        # Adding model 'Note'
        db.create_table('launch_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.Card'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('launch', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('launch_game')

        # Removing M2M table for field players on 'Game'
        db.delete_table(db.shorten_name('launch_game_players'))

        # Deleting model 'Hand'
        db.delete_table('launch_hand')

        # Deleting model 'Card'
        db.delete_table('launch_card')

        # Deleting model 'Note'
        db.delete_table('launch_note')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'launch.card': {
            'Meta': {'object_name': 'Card'},
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Hand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'suit': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'launch.game': {
            'Meta': {'object_name': 'Game'},
            'clocks': ('django.db.models.fields.IntegerField', [], {'default': '8'}),
            'discardpile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Hand']", 'related_name': "'discardpile'", 'null': 'True'}),
            'drawpile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Hand']", 'related_name': "'drawpile'", 'null': 'True'}),
            'fuses': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ispublic': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'launchpad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Hand']", 'related_name': "'launchpad'", 'null': 'True'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'launch.hand': {
            'Meta': {'object_name': 'Hand'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'launch.note': {
            'Meta': {'object_name': 'Note'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.Card']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['launch']