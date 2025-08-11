from __future__ import annotations
from django.db import models


class Tvshow(models.Model):
    name = models.TextField()
    number_of_seasons = models.IntegerField()
    number_of_episodes = models.IntegerField()
    origin_country = models.CharField(max_length=255)
    original_language = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.TextField(null=True)
    overview = models.TextField(null=True)
    themoviedb_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Season(models.Model):
    name = models.TextField()
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    season_number = models.IntegerField()
    vote_average = models.FloatField()
    themoviedb_id = models.TextField()
    tvshow = models.ForeignKey(
        to=Tvshow, on_delete=models.CASCADE, related_name="seasons"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Episode(models.Model):
    name = models.TextField()
    episode_number = models.IntegerField()
    overview = models.TextField(null=True)
    still_path = models.TextField(null=True)
    vote_average = models.FloatField()
    themoviedb_id = models.TextField()
    season = models.ForeignKey(
        to=Season, on_delete=models.CASCADE, related_name="episodes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CrewMember(models.Model):
    name = models.TextField()
    original_name = models.TextField()
    profile_path = models.TextField()
    department = models.TextField()
    job = models.TextField()
    themoviedb_id = models.TextField()
    episodes = models.ManyToManyField(to=Episode, related_name="crew")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Guest(models.Model):
    name = models.TextField()
    character = models.CharField(max_length=255)
    themoviedb_id = models.TextField()
    original_name = models.TextField()
    profile_path = models.TextField()
    known_for_department = models.TextField()
    episodes = models.ManyToManyField(to=Episode, related_name="guests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
