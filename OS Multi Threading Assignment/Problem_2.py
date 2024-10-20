# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:10:35 2017

@author: Mahir Mahbub Srizon
"""

import threading
import math

class Problem_2(threading.Thread):
    
    def __init__(self, number): 
        threading.Thread.__init__(self)
        self.number = number
        self.threads = []
        self.primes = []
        self.lock = threading.Lock()
    
    def prime(self,lrange,rrange):
        #self.lock.acquire()
        for num in range(lrange,rrange):
            if self.is_prime(num):
                with self.lock:
                    self.primes.append(num)
                    #print(num)
                #self.lock.acquire()
                #print(num) 
    
    def is_prime(self,n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
        
    def run(self):
        number_of_thread=int(math.sqrt(self.number))
        left=0
        right=2
        interval=int(self.number/number_of_thread)
        for i in range(number_of_thread):
            left=right
            if i==number_of_thread-1:
                right=number+1
            else:
                right+=interval
            t1 = threading.Thread(target=self.prime,args =(left,right,))
            t1.start()
            self.threads.append(t1)
        for i in self.threads:
            i.join()
        print("The Prime Numbers are: ",*self.primes)
        

number=int(input("The range of number is 0 to n.Give the value of n: "))
pb2=Problem_2(number)
pb2.run()
