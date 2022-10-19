from unittest import TestCase
from chapter_06_linked_structures.temp_linked_dequeue.linked_dequeue import *

number_of_add_successful = 5
number_of_delete_successful = number_of_add_successful - 3

number_of_delete_raising_exception = number_of_add_successful + 1

class TestDequeue(TestCase):

  def test_linked_dequeue_add_front(self):
    ld = LinkedDequeue()
    list_for_comparing = []

    for i in range(number_of_add_successful):
      list_for_comparing.append(i)
      ld.add_front(i)


    list_for_comparing.reverse()

    self.assertEqual(ld.display(), list_for_comparing)

  def test_linked_dequeue_delete_front_after_add_front_in_several_times(self):
    ld = LinkedDequeue()
    list_for_comparing = []

    for i in range(number_of_add_successful):
      list_for_comparing.append(i)
      ld.add_front(i)

    self.assertEqual(ld.delete_front(), list_for_comparing[-1])
    
    