###om urllib import response
import datetime
from django.test import TestCase
from mywatchlist.models import MyWatchList

# Create your tests here.
class tesURL(TestCase):
    def setUp(self):
        MyWatchList.objects.create(watched=True,title="Furry Hour",rating=3,release_date=datetime.date(2020,12,12),review="cute furries OwO")
    def test_object(self):
        dummy = MyWatchList.objects.get(title="Furry Hour")
        dummy.save()
        self.assertEqual(dummy.title,"Furry Hour")
        self.assertEqual(dummy.watched,True)
        self.assertEqual(dummy.rating,3)
        self.assertEqual(dummy.release_date,datetime.date(2020,12,12))
        self.assertEqual(dummy.review,"cute furries OwO")