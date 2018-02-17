import heapq

class PQ:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)

    def delete(self,x):
    	k=[r[0] for r in self.elements if r[1]==x]
    	if len(k)>0:
    		self.elements.remove((k[0],x))
    	return heapq.heapify(self.elements)