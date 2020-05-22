from rest_framework import status
from rest_framework.test import APITestCase

from todolist.models import TodoItem

TODO_DATA = {
    "title": "test title",
    "done": False
}


class TodoItemTestCase(APITestCase):
    def setUp(self):
        self.todo_item = TodoItem.objects.create(
            title='test',
            author_ip='0.0.0.0',
            done=False
        )
        self.url_list = '/todolist/'
        self.url_detail = '/todolist/1/'

    def test_create_todoitem(self):
        TodoItem.objects.all().delete()
        payload = TODO_DATA
        response = self.client.post(self.url_list, payload, format='json')
        todo_item = TodoItem.objects.first()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(todo_item.title, payload['title'])
        self.assertEqual(todo_item.done, payload['done'])
        self.assertIsNone(todo_item.done_date)

    def test_list_todoitems(self):

        response = self.client.get(self.url_list)
        todo_items = TodoItem.objects.all()

        self.assertEqual(todo_items.count(), 1)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todoitem(self):

        response = self.client.get(self.url_list)

        self.assertIsNotNone(response.data)
        self.assertEqual(TodoItem.objects.all().count(), 1)

        response = self.client.delete(self.url_detail)
        todo_items = TodoItem.objects.all()

        self.assertEqual(todo_items.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_details_todoitem(self):

        response = self.client.get(self.url_detail)

        self.assertEqual(response.data['title'], 'test')
        self.assertEqual(response.data['done'], False)
        self.assertEqual(response.data['author_ip'], '0.0.0.0')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_done_and_done_date_validation(self):
        TodoItem.objects.all().delete()
        payload = TODO_DATA
        payload['done_date'] = "2020-05-22T18:39:22.866462Z"
        expected = {
            "non_field_errors": ["You cannot assign done_date if done is False"]
        }
        response = self.client.post(self.url_list, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected)
        self.assertEqual(TodoItem.objects.all().count(), 0)

        payload = TODO_DATA
        payload['done'] = True
        response = self.client.post(self.url_list, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.all().count(), 1)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(TodoItem.objects.first().done_date)
