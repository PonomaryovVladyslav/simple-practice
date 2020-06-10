from datetime import timedelta
from unittest import TestCase as GeneralTestCase

from django.test import TestCase as DjangoTestCase
from django.utils import timezone
from authenicate.models import User
from list.models import Note


class SomeGeneralTest(GeneralTestCase):
    my_list = [1, 2, '3']

    def setUp(self):
        self.test_str = 'str'
        self.test_num = 33

    def test_str_correct(self):
        self.assertEqual(self.test_str, 'str')

    def test_num_incorrect(self):
        self.assertEqual(self.test_num, 33)

    def test_list(self):
        self.assertEqual(self.my_list, [1, 2, '3'])


class SomeDjangoTest(DjangoTestCase):

    def setUp(self):
        us = User.objects.create(username='vlad', birthday=timezone.now() - timedelta(days=4000))
        us.set_password('my_pass12!')
        self.user = us
        self.note = Note.objects.create(text='some_text', creator=self.user)

    def test_note(self):
        self.assertEqual(Note.objects.all().count(), 1)

    def test_creator(self):
        self.assertEqual(Note.objects.first().creator, self.user)

    def test_text(self):
        self.assertEqual(Note.objects.first().text, 'some_text')

    def test_different_user_note(self):
        new_user = User.objects.create(username='another_user',
                                       birthday=timezone.now() - timedelta(days=2000))
        new_user.set_password('my_pass12!')
        new_user.save()
        new_note = Note.objects.create(text='some_text', creator=new_user)
        self.assertEqual(Note.objects.filter(creator=new_user).first(), new_note)
        self.assertEqual(Note.objects.filter(creator=self.user).first(), self.note)
        self.assertEqual(Note.objects.all().count(), 2)


class ClientDjangoTest(DjangoTestCase):
    def setUp(self):
        us = User.objects.create(username='vlad', birthday=timezone.now() - timedelta(days=4000))
        us.set_password('my_pass12!')
        us.save()
        self.user = us
        form_data = {'username': 'vlad', 'password': 'my_pass12!'}
        self.client.post('/authenticate/login/', data=form_data)

    def test_create_note_incorrect(self):
        self.client.post('/note/create/')
        ## THIS IS A BUG

    def test_create_note_correct(self):
        self.client.post('/note/create/', {'text': 'bla'})
        self.assertEqual(Note.objects.all().count(), 1)

