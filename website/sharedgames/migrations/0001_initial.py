# Generated by Django 3.2.6 on 2021-08-28 19:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_multiplayer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Multiplayer',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sharedgames.game')),
                ('name', models.CharField(max_length=100)),
                ('header_image', models.URLField()),
                ('is_free', models.BooleanField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('steam_id', models.IntegerField(unique=True)),
                ('friends', models.ManyToManyField(related_name='_sharedgames_player_friends_+', to='sharedgames.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharedgames.player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharedgames.multiplayer')),
            ],
        ),
    ]
