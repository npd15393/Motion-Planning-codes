# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:24:09 2018

@author: Nishant
"""
import numpy as np

class Graph:

    def __init__(self):
        self.nodes=set()
	
    def addNode(self,p,l):
        assert len(p)==2
        h=GraphNode(p,l)
        self.nodes.add(h)
        return h

    def addEdge(self, l1,l2, ln):
        n1=[v for v in self.nodes if v.label==n1]
        n2=[v for v in self.nodes if v.label==n1]
        assert (len(n1)==1, n1+ ' not in the Graph') 
        assert (len(n2)==1,n2+' not in the Graph')
        n1=n1[0]
        n2=n2[0]
        n1.paths.append=(n2,ln)
        n2.paths.append=(n1,ln)


class GraphNode:
	def __init__(self,p,l):
        self.label=l
        self.p=p
		self.x=p[0]
        self.y=p[1]
        self.paths=[]
   
class TreeNode: 
    def __init__(self):
        self.left_node=None
        self.right_node=None
    
 
import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()
    
class Stack:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop(len(self.elements)-1)

class PQNode():
    def __init__(self):
        self.val
        
class PriorityQ():
    def __init__(self):
        self.root=None
        self.left_node=None
        self.right_node=None
    
    def insert(self,p):
        current =self.root
        parent=None
        while current.val>p.val:
            parent=current
            current=current.left_node if np.abs(current.left_node.val-p.val)<np.abs(current.right_node.val-p.val) else current.right_node
            
        if np.abs(current.left_node.val-current.val)>np.abs(current.right_node.val-current.val):
            p.left_node=current
            p.right_node=current.right_node
            if parent.left_node==current:
                 parent.left_node=p
            else:
                parent.right_node=p
    
    def pop(self):
        return self.realign(self.root)

    def realign(self,root):
        current=root
        if not (current.left_node==None and current.right_node==None):
            if current.left_node.val>current.right_node.val:
                nl=self.realign(current.left_node) 
                if nl.left_node==None:
                    nl.left_node=current.right_node
                else:
                    nl.right_node=current.right_node
                return current
            else:
                nl=self.realign(current.right_node)
                if nl.left_node==None:
                    nl.left_node=current.left_node
                else:
                    nl.right_node=current.left_node
                return current
        elif current.left_node==None:
            self.realign(current.right_node) 
            return current
        elif current.right_node==None:
            self.realign(current.left_node)
            return current
        else:
            return current
    
    
class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
