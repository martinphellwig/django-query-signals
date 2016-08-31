"The main test module."
from django.test import TestCase
from django.contrib.auth.models import User
from django_query_signals import (receiver,
                                  pre_bulk_create, post_bulk_create,
                                  pre_delete, post_delete,
                                  pre_get_or_create, post_get_or_create,
                                  pre_update_or_create, post_update_or_create,
                                  pre_update, post_update,
                                  )

# pylint: disable=unused-variable, unused-argument
class MainTest(TestCase):
    "Main test module"
    def test_01_bulk_create(self):
        "Does bulk create trigger a signal?"
        tmp = {'pre':False,
               'post':False}

        @receiver(pre_bulk_create)
        def _set_pre(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['pre'] = True

        @receiver(post_bulk_create)
        def _set_post(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['post'] = True

        User.objects.bulk_create([User(username='test1'),
                                  User(username='test2')])

        self.assertTrue(tmp['pre'], msg='pre_bulk_create not called')
        self.assertTrue(tmp['post'], msg='post_bulk_create not called')


    def test_02_delete(self):
        "Does delete trigger a signal?"
        tmp = {'pre':False,
               'post':False}

        @receiver(pre_delete)
        def _set_pre(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['pre'] = True

        @receiver(post_delete)
        def _set_post(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['post'] = True

        self.test_01_bulk_create()
        users = User.objects.all()
        users.delete()

        self.assertTrue(tmp['pre'], msg='pre_delete not called')
        self.assertTrue(tmp['post'], msg='post_delete not called')

    def test_03_get_or_create(self):
        "Does get_or_create trigger a signal?"
        tmp = {'pre':False,
               'post':False}

        @receiver(pre_get_or_create)
        def _set_pre(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['pre'] = True

        @receiver(post_get_or_create)
        def _set_post(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['post'] = True

        users = User.objects.get_or_create(username='test')

        self.assertTrue(tmp['pre'], msg='pre_get_or_create not called')
        self.assertTrue(tmp['post'], msg='post_get_or_create not called')

    def test_04_update_or_create(self):
        "Does update_or_create trigger a signal?"
        tmp = {'pre':False,
               'post':False}

        @receiver(pre_update_or_create)
        def _set_pre(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['pre'] = True

        @receiver(post_update_or_create)
        def _set_post(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['post'] = True

        users = User.objects.update_or_create(username='test')

        self.assertTrue(tmp['pre'], msg='pre_update_or_create not called')
        self.assertTrue(tmp['post'], msg='post_update_or_create not called')


    def test_05_update(self):
        "Does update trigger a signal?"
        tmp = {'pre':False,
               'post':False}

        @receiver(pre_update)
        def _set_pre(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['pre'] = True

        @receiver(post_update)
        def _set_post(signal, sender, args):
            self.assertEqual(sender, User)
            tmp['post'] = True

        self.test_01_bulk_create()
        users = User.objects.all()
        users.update(last_name='Erone')

        self.assertTrue(tmp['pre'], msg='pre_update not called')
        self.assertTrue(tmp['post'], msg='post_udpate not called')
