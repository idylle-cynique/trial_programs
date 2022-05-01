class UnionFindTree:
    def __init__(self):
        '''グループ情報を記録するための辞書型変数を初期化'''
        self.parent_nodes = dict()
    
    def set(self, value)-> None:
        '''UnionFind木にノードを追加'''
        self.parent_nodes[value] = value
    
    def unite(self,node_a,node_b)-> None:
        '''2つのグループを併合する'''
        if self.check_same(node_a, node_b): # 属するグループが同じなら何もしない
            return 
        else:                               # 属するグループが異なる場合は、片方の親ノードをもう片方に設定する
            self.parent_nodes[node_a] = node_b
    
    def find_root(self,node)-> None:
        '''対象のノードが属するグループ(根ノード)を見つけ、ついでに経由したノードのグループ情報を更新する'''
        if self.is_root(node): # 対象のノードが根ノードならそのノードをそのまま返す 
            return node
        else:                  # 対象のノードが子ノードなら、親ノードの根ノードを探して取得
            root_node = self.find_root(self.parent_nodes[node])
            # 取得した根ノードを対象のノードの親ノードに設定
            self.parent_nodes[node] = root_node
            return root_node

    def check_same(self,node_a, node_b)-> bool:
        '''属するグループが同じかどうか判定する'''
        if self.find_root(node_a) == self.find_root(node_b):
            return True
        else:
            return False
    
    def is_root(self,value)-> bool:
        '''対象のノードが親ノードかチェック'''
        return self.parent_nodes[value] == value
    
    def __repr__(self) -> str:
        '''print出力用'''
        return "Node:{}".format(self.parent_nodes,)



def answer_of_atc001():
    # https://atcoder.jp/contests/atc001/tasks/unionfind_a
    N,Q = map(int,input().split())
    numbers = [int(x) for x in range(N)]
    ufs = UnionFindTree()
    for n in numbers:
        ufs.set(n)
        
    for i in range(Q):
        query = list(map(int,input().split()))
        command, val1, val2 = query
        #print(ufs,query)
        if command == 0: # 連結クエリ
            ufs.unite(val1,val2)
        else:            # 判定クエリ
            flag = ufs.check_same(val1,val2)
            if flag:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    answer_of_atc001()