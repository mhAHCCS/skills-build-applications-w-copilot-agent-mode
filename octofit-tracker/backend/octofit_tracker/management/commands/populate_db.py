from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=1500),
            User(email='metalgeek@mhigh.edu', name='Iron Man', age=48),
            User(email='zerocool@mhigh.edu', name='Captain America', age=102),
            User(email='crashoverride@mhigh.edu', name='Hulk', age=49),
            User(email='sleeptoken@mhigh.edu', name='Black Widow', age=35),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team.objects.create(name='Blue Team')
        team2 = Team.objects.create(name='Gold Team')
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-03'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-04'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], points=100),
            Leaderboard(user=users[1], points=90),
            Leaderboard(user=users[2], points=95),
            Leaderboard(user=users[3], points=85),
            Leaderboard(user=users[4], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))