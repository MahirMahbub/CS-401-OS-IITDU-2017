# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:21:58 2017

@author: Mahir Mahbub Srizon
"""

import threading
import math
import random

class Problem_3(threading.Thread):
    
    def __init__(self, number): 
        threading.Thread.__init__(self)
        self.number = number
        self.threads = []
        self.circle_dot=0
        self.rec_dot=0
        self.lock = threading.Lock()
        self.radius = 1.0
        self.result=0
    def dot_Counter(self):
        for x in range(number):
            x=random.uniform(-1,1)
            y=random.uniform(-1,1)
            distance=math.sqrt((math.fabs(x)**2)+(math.fabs(y)**2))
            if distance<=self.radius:
                self.circle_dot+=1
            self.rec_dot+=1
                
        self.result=(4*self.circle_dot)/self.rec_dot
            

    def run(self):
        t1 = threading.Thread(target=self.dot_Counter)
        t1.start()
        self.threads.append(t1)
        t1.join()
        print("Value of PI: ",self.result)
        

number=int(input("Input the Total Random Number You Want to Generate: "))
pb3=Problem_3(number)
pb3.run()
