# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading

class Problem_1(threading.Thread):
    
    def __init__(self, number): 
        threading.Thread.__init__(self)
        self.number = number
        self.avg=0
        self.minimum=float("inf")
        self.maximum=-float("inf")
        self.length=len(number)
        self.threads = []
        self.lock = threading.Lock()
    def average(self):
        i=0
        for i in self.number:
            self.lock.acquire()
            self.avg+=i
            #print(self.avg)
            self.lock.release() 
        self.avg=self.avg/self.length
    def mini(self):
        for i in self.number:
            self.lock.acquire()
            if i<self.minimum:
                self.minimum=i
            self.lock.release() 
    def maxi(self):
        for i in self.number:
            self.lock.acquire()
            if i>self.maximum:
                self.maximum=i
            self.lock.release() 
    def run(self):
        t1 = threading.Thread(target=self.average)
        self.threads.append(t1)
        t2 = threading.Thread(target=self.mini)
        self.threads.append(t2)
        t3 = threading.Thread(target=self.maxi)
        self.threads.append(t3)
        t1.start()
        t2.start()
        t3.start()
        '''for i in self.threads:
            print(i)
            i.start()'''
        print("Average: ",self.avg," Maximum: ",self.maximum," Minimum: ",self.minimum)
        

number = list(map(int,input("Enter the list of numbers seperated by space: ").split()))
pb1=Problem_1(number)
pb1.run()
