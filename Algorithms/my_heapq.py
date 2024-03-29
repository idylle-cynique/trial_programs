'''
    Pythonの標準モジュールheapqをラップしてlistなどと同じ要領で使えるようにする
'''
import heapq
import random
 
class PriorityQueue:
    priorityqueue = list()
 
    def __init__(self,lst=list())->None:
        self.priorityqueue = lst
        heapq.heapify(lst)
    
    def heappush(self,element)->None:
        heapq.heappush(self.priorityqueue,element)
    
    def heappop(self):
        ret_ele = self.priorityqueue[0]
        heapq.heappop(self.priorityqueue)
        return ret_ele

    def heapsort(self)->list:
        sorted_list = list()
        pq = list()

        while(self.priorityqueue):
            min_ele = heapq.heappop(self.priorityqueue)
            sorted_list.append(min_ele)
            heapq.heappush(pq,min_ele)

        self.priorityqueue = pq
        return sorted_list
    
    def __repr__(self)-> str:
        return f"PriorityQueue({self.priorityqueue})"




def main():
    length = 32
    numbers = [random.randint(1,100) for x in range(length)]
    numbers = [52, 46, 18, 59, 58, 40, 77, 39, 69, 46, 74, 39, 29, 59, 62, 64, 57, 39, 35, 92, 39, 57, 64, 35, 33, 31, 57, 71, 36, 3, 83, 57]
    hq = PriorityQueue(numbers)

    print(numbers)
    print(hq)
    print(hq.heapsort())
    return 


if __name__ == '__main__':
    main()