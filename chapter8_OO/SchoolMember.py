#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Desc: 继承的例子。 在括号里面写父类
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/6/22 17:03


class SchoolMember:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def info(self):
        print("name:", self.name, " my age:",self.age, end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        self.name = name;
        self.age = age;
        self.salary=salary;

    def info(self):
        SchoolMember.info(self);
        print("salary:", self.salary)


class Student(SchoolMember):
    def __init__(self, name, age, score):
        self.name = name;
        self.age = age;
        self.score=score;

    def info(self):
        SchoolMember.info(self);
        print("score:", self.score)


s = Student('EE',30, 100);
t = Teacher('KK',40, 6000);


s.info();
t.info();