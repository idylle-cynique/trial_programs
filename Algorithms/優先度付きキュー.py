
class PriorityQueue:
    def __init__(self)-> None:
        self.priority_queue = list()
        self.length = len(self.priority_queue)
    
    def set_values(self,input_list)-> None:
        '''リストをキューにセットしてヒープ化'''
        self.priority_queue = input_list[:]
        self.length = len(self.priority_queue)
        self.build_heap()
    
    def append(self,value):
        '''ヒープ構造を保ちながら要素を追加'''
        self.priority_queue.append(value)
        self.heapify(len(self.priority_queue)-1)
    
    def heapify(self,idx):
        '''ある要素とその子要素とのヒープ条件を満たすようにスワップ処理を行う 計算量:O(log(要素数))'''
        #print(len(self.priority_queue),":", idx,"->",idx*2+1,idx*2+2)
        length = len(self.priority_queue)
        if idx*2+2 < length:   # 子要素を2つ持つ要素に対して処理を行う
            if self.priority_queue[idx] < self.priority_queue[idx*2+2]:
                self.priority_queue[idx],self.priority_queue[idx*2+2] = self.priority_queue[idx*2+2],self.priority_queue[idx]           
            if self.priority_queue[idx] < self.priority_queue[idx*2+1]:
                self.priority_queue[idx],self.priority_queue[idx*2+1] = self.priority_queue[idx*2+1],self.priority_queue[idx]     
        elif idx*2+1 < length: # 子要素を1つだけ持つ要素に対して処理を行う
            if self.priority_queue[idx] < self.priority_queue[idx*2+1]:
                self.priority_queue[idx],self.priority_queue[idx*2+1] = self.priority_queue[idx*2+1],self.priority_queue[idx]
        else:                  # 子要素を持たない要素に対しては処理を行わない
            pass

        if idx: # 先頭要素に達するまで再帰的にヒープ化処理を行う
            self.heapify((idx-1)//2)
        return 

    def down_heapify(self): return
    
    def up_heapidy(self): return

    
    def build_heap(self,flag=False):
        '''ヒープを構築する 計算量: O(要素数)'''
        for index in range(len(self.priority_queue)//2,-1,-1):
            self.heapify(index)
        return 

    def heappop(self):
        self.priority_queue[0],self.priority_queue[-1] = self.priority_queue[-1],self.priority_queue[0]
        self.priority_queue.pop()

    def __repr__(self):
        '''print()でキューの中身を閲覧'''
        return f"HEAP:{self.priority_queue}"




def main():
    sample_array = [1,9,8,2,3,10,14,7,16,4]
    heapq = PriorityQueue()
    heapq.set_values(sample_array)
    print(sample_array)
    print(heapq)
    return


if __name__ == '__main__':
    main()