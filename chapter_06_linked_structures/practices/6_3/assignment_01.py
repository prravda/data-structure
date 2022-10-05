from chapter_06_linked_structures.linked_queue.linked_queue import LinkedQueue


def driver_code():
    queue = LinkedQueue()

    for i in range(10):
        queue.enqueue(i)

    print('after 9 enqueue:', queue)

    print('\n\tdequeue:', queue.dequeue())
    print('\tdequeue:', queue.dequeue())
    print('\tdequeue:', queue.dequeue())

    print('\nafter 3 dequeue:', queue)

    hero_list = ('superman', 'batman', 'wonder_woman' 'aquaman')

    for hero in hero_list:
        queue.enqueue(hero)

    print(f'\nafter {len(hero_list)} enqueue', queue)

    print('\n\tdequeue:', queue.dequeue())

    print('\nafter 1 dequeue:', queue)

    print('\n\tpeek:', queue.peek())


driver_code()