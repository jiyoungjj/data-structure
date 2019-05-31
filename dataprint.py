#coding: utf-8
import random
import string

HEAD = None
SIZE = 0


class SinglyLinkedListNode(object):
    def __init__(self, name, phone,number):
        self.name = name
        self.phone = phone
        self.number = number
        self.next = None


def get_random_name():
    """랜덤한 알파벳 3자리 문자열을 리턴한다"""
    return ''.join([random.choice(string.ascii_letters).upper() for _ in range(3)])


def get_random_four_numbers():
    """랜덤한 4자리 숫자를 리턴한다"""
    return ''.join([str(random.randint(0, 9)) for _ in range(4)])


def get_random_phone():
    """랜덤한 전화번호를 리턴한다"""
    return '-'.join(['010', get_random_four_numbers(), get_random_four_numbers()])

def get_random_five_numbers():
    """랜덤한 5자리 숫자를 리턴한다"""
    return ''.join([str(random.randint(0,9)) for _ in range(5)])

def get_random_year_numbers():
    """랜덤한 1자리 숫자(학번의 년도용)을 리턴한다"""
    return ''.join([str(random.randint(3,9)) for _ in range(1)])

def get_random_number():
    """랜덤한 학번을 리턴한다"""
    return ''.join(['201',get_random_year_numbers(),get_random_five_numbers()])

def add_node(node):
    """노드를 리스트에 추가한다"""
    global HEAD
    global SIZE

    if HEAD is None:
        HEAD = node
    else:
        cursor = HEAD
        while cursor.next is not None:
            cursor = cursor.next
        node.next = cursor.next
        cursor.next = node
    SIZE += 1


def print_list():
    """리스트를 출력한다"""
    if SIZE == 0:
        print('(리스트가 비어있습니다)')
        return

    count = 1
    cursor = HEAD
    while cursor is not None:
        print(f'{count}. {cursor.name}\t{cursor.phone}\t{cursor.number}')
        cursor = cursor.next
        count += 1


def sort_add_node_for_name(head, node):
    """이름 오름차순 정렬 순으로 리스트에 노드를 삽입"""
    if head is None:
        head = node
    else:
        cursor = head
        last = None
        inserted = False
        while cursor is not None:
            if node.name < cursor.name:
                if last is None:
                    # 헤드에 삽입
                    node.next = cursor
                    head = node
                else:
                    node.next = cursor
                    last.next = node
                inserted = True
                break
            last = cursor
            cursor = cursor.next
        if not inserted:
            # 마지막에 추가
            node.next = None
            last.next = node
    return head

def sort_add_node_for_number(head, node):
    """학번 오름차순 정렬 순으로 리스트에 노드를 삽입"""
    if head is None:
        head = node
    else:
        cursor = head
        last = None
        inserted = False
        while cursor is not None:
            if node.number < cursor.number:
                if last is None:
                    # 헤드에 삽입
                    node.next = cursor
                    head = node
                else:
                    node.next = cursor
                    last.next = node
                inserted = True
                break
            last = cursor
            cursor = cursor.next
        if not inserted:
            # 마지막에 추가
            node.next = None
            last.next = node
    return head


def sort_list_for_name():
    """이름 순으로 오름차순 정렬"""
    global HEAD
    global SIZE

    if SIZE == 0:
        print('(리스트가 비어있습니다)')
        return

    cursor = HEAD
    new_head = None
    while cursor is not None:
        new_head = sort_add_node_for_name(new_head, SinglyLinkedListNode(cursor.name, cursor.phone,cursor.number))
        cursor = cursor.next

    HEAD = new_head
    return

def sort_list_for_number():
    """학번 순으로 오름차순 정렬"""
    global HEAD
    global SIZE

    if SIZE == 0:
        print('(리스트가 비어있습니다)')
        return

    cursor = HEAD
    new_head = None
    while cursor is not None:
        new_head = sort_add_node_for_number(new_head, SinglyLinkedListNode(cursor.name, cursor.phone,cursor.number))
        cursor = cursor.next

    HEAD = new_head
    return


def main():
    global HEAD
    global SIZE

    # 10000개의 랜덤한 데이터를 생성
    for _ in range(10000):
        add_node(SinglyLinkedListNode(get_random_name(), get_random_phone(), get_random_number()))

    # 메뉴 출력
    answer = True
    while answer != '0':
        print(f'({SIZE}명의 데이터가 있습니다)')
        answer = input('(1) 학번순\n(2) 이름순\n메뉴선택(0: 종료) : ')
        if answer == '1':
            sort_list_for_number()
            print_list()
        elif answer == '2':
            sort_list_for_name()
            print_list()

        else:
            if answer != '0' :
                print('(잘못된 번호를 입력하였습니다)')

    print('(종료되었습니다)')


main()
