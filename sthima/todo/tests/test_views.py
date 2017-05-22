from django.test import Client, TestCase

from todo.views import TodoView


class TodoTest(TestCase):
    """
    Test case of Todo list app view
    """
    def setUp(self):
        """
        Set up all the tests
        """
        self.client = Client()

    def test_todo_view(self):
        """
        Test of todo page view
        """
        response = self.client.get('/todo-list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo.html')
