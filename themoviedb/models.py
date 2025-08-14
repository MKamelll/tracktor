from __future__ import annotations
from django.db import models


class Tvshow(models.Model):
    name = models.CharField(max_length=255)
    number_of_seasons = models.IntegerField()
    number_of_episodes = models.IntegerField()
    origin_country = models.CharField(max_length=255)
    original_language = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=255, null=True)
    overview = models.TextField(null=True)
    themoviedb_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Season(models.Model):
    name = models.CharField(max_length=255)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=255, null=True)
    season_number = models.IntegerField()
    vote_average = models.FloatField()
    themoviedb_id = models.CharField(max_length=255)
    tvshow = models.ForeignKey(
        to=Tvshow, on_delete=models.CASCADE, related_name="seasons"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Episode(models.Model):
    name = models.CharField(max_length=255)
    episode_number = models.IntegerField()
    overview = models.TextField(null=True)
    still_path = models.CharField(max_length=255, null=True)
    vote_average = models.FloatField()
    themoviedb_id = models.CharField(max_length=255)
    season = models.ForeignKey(
        to=Season, on_delete=models.CASCADE, related_name="episodes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CrewMember(models.Model):
    name = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    profile_path = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    themoviedb_id = models.CharField(max_length=255)
    episodes = models.ManyToManyField(to=Episode, related_name="crew")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Guest(models.Model):
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    themoviedb_id = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    profile_path = models.CharField(max_length=255)
    known_for_department = models.CharField(max_length=255)
    episodes = models.ManyToManyField(to=Episode, related_name="guests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
