#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Desc: 用到@classmethod 还有类里面的全局变量。 全局变量：Class.xxx   过程变量：self.xxx
#  Python 中，所有参数都是公开的，并且所有的方法都是虚拟的（Virtual）
# classmethod和staticmethod都是静态方法，唯一区别是classmethod多一个cls参数，可以获取当前实例的属性

# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/4/26 21:26


class Robot:
    population = 0
    robot_set = set()

    def __init__(self, robot_name):
        self.robot_name = robot_name
        Robot.population += 1;
        Robot.robot_set.add(robot_name)
        print('新增了一个机器人，名字：', robot_name, '. 现在有', self.population, '个机器人。',end='\n\n')

    def say_hi(self):
        print('您好，很高兴能为你服务。我的名字是：', self.robot_name)

    def kill_me(self):
        Robot.population -= 1
        Robot.robot_set.remove(self.robot_name)
        print('机器人', self.robot_name," 已经完成历史任务。现在人道毁灭。")

    @staticmethod
    def static_info():
        print('-----------')
        if Robot.population > 0:
            print('@static_info. 有', Robot.population, '个机器人。', '它们分别是：',Robot.robot_set)
        else:
            print('@static_info. 已经没有机器人了。')
        print('-----------', end='\n\n')

    @classmethod
    def class_info(cls):
        print('-----------')
        if cls.population > 0:
            print('@class_info. 有', cls.population, '个机器人。', '它们分别是：',cls.robot_set)
        else:
            print('@class_info. 已经没有机器人了。')
        print('-----------', end='\n\n')


# 创建2只机器人

r1 = Robot('A-001')
r2 = Robot('A-002')

Robot.static_info()

r1.say_hi()
r2.say_hi()

r1.kill_me()
Robot.class_info()

r2.kill_me()
Robot.static_info()
