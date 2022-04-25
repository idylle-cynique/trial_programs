'''二分木
データを二分木構造で格納するためのライブラリ
現時点ではまだ一連の走査機能がないのでその辺りはこれから

またあくまでもデータを二分木生成アルゴリズムを用いてデータ格納を行うだけなので
格納するデータの挿入順によっては計算量が改善されない場合がある
    ex. [1,2,3,4,5,6,...]のような順で挿入する場合
したがって、実際に活用するにあたってはこれを拡張して平衡二分探索木を作る必要がある
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self): # print()で中身が分かるようにしておく
        return (f"LEFT: {self.left}, VALUE: {self.value}, RIGHT: {self.right}")
    

class BST:
    ''' Binary Search Tree (二分木)'''
    def __init__(self)-> None:
        # あるノードの親ノードの情報を管理する辞書を初期化
        self.parent_node = dict()
        
        # ルートノードは未設定
        self.root = None
    
    def set_root(self,value)-> None: 
        # ルートノードを生成
        self.root = Node(value)
        
        # 親ノードの親は自分自身、ということにする
        self.parent_node[self.root] = self.root

    def insert(self,element)-> None:
        node = self.root # ルートノードから探索開始

        # 挿入すべき位置に達するまで枝を辿っていく
        while(node): 
            pre_node = node # 新しいノードを接続するノードを記録
            if node.value > element: # 追加要素がそのノードの値より小さいなら左の枝を辿る
                node = node.left
                mode = "left"
            else:                    # 追加要素がそのノードの値より大きいなら右の枝を辿る 
                node = node.right
                mode = "right"
        
        # 挿入位置が分かったので挿入処理を施す
        new_node = Node(element)                # 新しいノードを生成
        self.parent_node[new_node] = pre_node   # 新しいノードの親ノードを接続元ノードとして設定
        if mode == "left":
            pre_node.left = new_node
        else: # == "right"
            pre_node.right = new_node
    
    def delete(self, element)-> None:
        '''未完成'''
        # 二分木内のあるノードを削除、引数で示されたノードが存在しない場合は何もしない

        '''処理内容
            1) 子ノードを持たないノード:    そのまま削除
            2) 子ノードを1つだけ持つノード: 指定されたノードを削除して、子ノードの親情報を親ノードの親ノードに買える
            3) 子ノードを2つ持つノード:     指定されたノードの右の子ノードを探索し最も値が小さいノードを指定されたノードの位置に据える
        '''
        return 

    def take_max(self):
        '''生成した二分木から最大値を取り出す'''
        now_node = self.root
        while(now_node.right): # ルートノードから探索を開始してひたすら右側の枝を辿っていく
            now_node = now_node.right
        return now_node.value
    
    def take_min(self):
        '''生成した二分木から最小値を取り出す'''
        now_node = self.root
        while(now_node.left):  # ルートノードから探索を開始してひたすら右側の枝を辿っていく
            now_node = now_node.left
        return now_node.value

    def check_exist(self, search_value)-> bool:
        '''ある値をとる要素の存在チェック'''
        now_node = self.root

        while(not(now_node.value == search_value) and (now_node.left or now_node.right)): # 対応するノードが見つかるか、葉に達するまで探索を行う
            if now_node.value < search_value:
                now_node = now_node.right
            else: # search_value > now_node.value
                now_node = now_node.left
        
        if now_node.value == search_value:
            return True
        else:
            return False




        


            
        
if __name__ == "__main__":
    
    Array = [5,1,3,2,0,10,7,8,6]
    flag = False
    bst = BST()
    
    for element in Array:
        if not(flag):
            bst.set_root(element)
        else:
            bst.insert(element)


