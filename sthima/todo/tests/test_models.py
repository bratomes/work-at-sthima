from django.test import TestCase
from django.contrib.auth.models import User

from model_mommy import mommy

from todo.models import Task


class TaskTest(TestCase):
    """
    Test case of Task model
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.user = mommy.make(User)
        self.task = mommy.make(Task)

    def test_string_representation(self):
        """
        Test if the __str__ method returns the description of a task
        """
        self.assertEqual(str(self.task), self.task.description)
