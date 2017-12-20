#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self, list):
        js = Counter(list).most_common()
        if self.name == 'teacher':
            for x in js:
                if x == js[-1]:
                    print('{}: {}'.format(x[0], x[1]))
                else:
                    print('{}: {}'.format(x[0], x[1]), end=', ')
        else:
            count_pass = 0
            for x in js:
                if x[0] == 'D':
                    count_fail = x[1]
                else:
                    count_pass = count_pass + (x[1]) 
            print('Pass: {}, Fail: {}'.format(count_pass, count_fail))

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        list = sys.argv[2]
        TorS = sys.argv[1]
        person1 = Person(TorS)
        person1.get_grade(list)
