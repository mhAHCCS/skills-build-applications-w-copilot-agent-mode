from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctoFitTrackerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2025-04-08")
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)
        self.workout = Workout.objects.create(name="Test Workout", description="A test workout", duration=45)

    def test_user_creation(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_creation(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_creation(self):
        response = self.client.get("/api/activity/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_creation(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_creation(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)