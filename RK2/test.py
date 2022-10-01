import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_task_1(unittest.TestCase):
    def test_task_1(self):
        one_to_many = [(d.fio, d.sal, a.mode)
                       for a in auto
                       for d in driv
                       if d.exp_id == a.id]
        self.assertEqual(Task1(one_to_many), [('Ахтамбаев', 'городской'),
                                              ('Андреев', 'школьный'), ('Алешин', 'экскурсионный')])

class Test_task_2(unittest.TestCase):
    def test_task_2(self):
        one_to_many = [(d.fio, d.sal, a.mode)
                       for a in auto
                       for d in driv
                       if d.exp_id == a.id]
        self.assertEqual(Task2(one_to_many),[('экскурсионный', 23000), ('школьный', 30000),
                                             ('городской', 40000), ('пригородный', 44000), ('перонный', 50000)])


class Test_task_3(unittest.TestCase):
    def test_task_3(self):
        many_to_many_temp = [(a.mode, ad.auto_id, ad.driv_id)
                             for a in auto
                             for ad in auto_drivers
                             if a.id == ad.auto_id]
        many_to_many = [(d.fio, d.sal, auto_name)
                        for auto_name, auto_id, driv_id in many_to_many_temp
                        for d in driv if d.id == driv_id]
        self.assertEqual(Task3(many_to_many),
                         [('Алешин', 'городской'), ('Алешин', 'школьный'), ('Бегларов', 'туристический'),
                          ('Ефременко', 'туристический'), ('Носкин', 'городской'), ('Носкин', 'перонный'),
                          ('Семенов', 'туристический'), ('Стебунов', 'городской'), ('Стебунов', 'школьный'),
                          ('Стебунов', 'экскурсионный')])
if __name__ == "__main__":
    unittest.main()