# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:23:06 2022

@author: carlo
"""

import math

class IncrementerController:
    def __init__(self, arm):
        # the controller should save a reference to the arm it's controlling
        self.arm = arm

    def control(self, target):
        # the control method receives a target

        # This specific controller ignores the target
        # It only increments each joint in 1 degree

        # the arm.move method receives a list of joint values increments
        # the list should have as many elements as the arm has joints
        # you can find out how many joints the arm has via arm.get_num_joints()
        # for this example:
        # pi/180 = 1 degree in radians
        # [element] * 3 => [element, element, element]
        self.arm.move( [0]*self.arm.get_num_joints() )