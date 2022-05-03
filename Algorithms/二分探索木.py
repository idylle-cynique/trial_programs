'''二分探索木
データを二分木構造で格納するためのライブラリ
現時点ではまだ一連の走査機能がないのでその辺りはこれから

ただ、あくまでもデータを二分木生成アルゴリズムを用いてデータ格納を行うだけなので
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
        return (f"VALUE-{self.value}")
    

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
    
    def delete(self, element)-> bool:
        '''指定された値を持つノードを削除'''
        '''処理内容
            1) 子ノードを持たないノード:    そのまま削除
            2) 子ノードを1つだけ持つノード: 指定されたノードを削除して、子ノードの親情報を親ノードの親ノードに買える
            3) 子ノードを2つ持つノード:     指定されたノードの右部分木を探索し最も値が小さいノード(左端ノード)を対象のノードの位置に据える
        '''

        '''メモ
            Pythonの場合、削除したノードが占有していたメモリ領域の解法はどうやってする？
            対象のノードを代入した変数にdel処理をしたとして、それはメソッド内変数を削除しただけで代入元のノード自体は削除されていないのでは？
        '''

        def get_node(search_value):
            # 対応するノードを探す
            now_node = self.root
            while(not(now_node.value == search_value) and (now_node.left or now_node.right)): 
                if now_node.value < search_value:
                    now_node = now_node.right
                else: # search_value > now_node.value
                    now_node = now_node.left
            
            # ノードが存在すればそのノードを、存在しなければNoneを返す
            if now_node.value == search_value:
                return now_node
            else:
                return None

        def get_mostleft(start_node):
            # ある部分木(根からでも可)における最左ノードを取り出す
            now_node = start_node
            while(now_node.left):
                now_node = now_node.left
            return now_node

        wannadelete_node = get_node(element) # Python3.10ならセイウチ記法(:=)を使えば短く出来る模様
        if not(wannadelete_node): # 対象のノードが存在しない場合はFalseを返して終了
            return False

        if wannadelete_node.left and wannadelete_node.right:  # 左右いずれにも子ノードを持つ場合
            # 右の部分木から左端のノードを取り出しそれを削除対象のノードのある位置に据える
            mostleft_node = get_mostleft(wannadelete_node.right)

            leftchild = wannadelete_node.left                # 削除対象のノードの左子ノードを得る
            rightchild = wannadelete_node.right              # 削除対象のノードの右子ノードを得る
            parent_node = self.parent_node[wannadelete_node] # 削除対象のノードの親ノードを得る

            # 削除対象のノードを右部分木最左ノードに挿げ替える
            self.parent_node[mostleft_node] = mostleft_node if self.parent_node[wannadelete_node] == wannadelete_node else parent_node
            
            # 挿げ替えたノードを削除対象のノードの子ノードと接続
            self.parent_node[leftchild] = mostleft_node
            self.parent_node[rightchild] = mostleft_node

            # 削除対象のノードの情報を削除
            del self.parent_node[wannadelete_node]
            del wannadelete_node

        elif wannadelete_node.left or wannadelete_node.right: # 子ノードを左右いずれか一方にのみ持つ場合
            child_node = wannadelete_node.left if wannadelete_node.left else wannadelete_node.right # 子ノードの情報を得る
            parent_node = self.parent_node[wannadelete_node] # 対象のノードの親ノード情報を得る

            del self.parent_node[wannadelete_node] # 対象のノードの親ノード情報を辞書から削除
            del wannadelete_node                   # 対象のノードを削除

            self.parent_node[child_node] = parent_node # 残った子ノードと親ノードを接続
        else: # 子ノードを持たない(葉ノード)場合
            del self.parent_node[wannadelete_node] # 親ノード情報を削除
            del wannadelete_node                   # 対象のインスタンス変数を削除
        
        return True # 削除処理完了の意味でTrueを返す

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

    def get_preorder(self)-> list:
        '''行きがけ順走査によって各ノードを得る'''
        now_node = self.root
        ret_list = list()
        checklist = set([None])

        while(len(checklist) <= len(self.parent_node) or now_node == self.parent_node[now_node]):
            if now_node not in checklist:
                ret_list.append(now_node.value)
                checklist.add(now_node)

            if now_node.left in checklist:
                if now_node.right in checklist:
                    now_node = self.parent_node[now_node]
                else:
                    now_node = now_node.right
            else:
                now_node = now_node.left
        return ret_list

    def get_inorder(self)-> list:
        '''通りがけ順走査によって各ノードを得る'''
        now_node = self.root
        ret_list = list()
        checklist = set([None]) # 子ノードがないノードにも対応できるようNoneを入れておく
        while(len(checklist) <= len(self.parent_node) or now_node != self.parent_node[now_node]):
            if now_node.left not in checklist:
                now_node = now_node.left
            else:
                if now_node.right not in checklist:
                    ret_list.append(now_node.value)
                    checklist.add(now_node)
                    now_node = now_node.right
                else:
                    if now_node not in checklist:
                        ret_list.append(now_node.value)
                        checklist.add(now_node)
                    now_node = self.parent_node[now_node]
        return ret_list # ソートされた形で得ることができる

    def get_postorder(self)-> list:
        '''帰りがけ順走査によって各ノードを得る'''
        now_node = self.root
        ret_list = list()
        checklist = set([None]) # 子ノードがないノードにも対応できるようNoneを入れておく
        while(len(checklist) <= len(self.parent_node) or now_node != self.parent_node[now_node]):
            if now_node.left not in checklist:
                now_node = now_node.left
            else:
                if now_node.right not in checklist:
                    now_node = now_node.right
                else:
                    ret_list.append(now_node.value)
                    checklist.add(now_node)
                    now_node = self.parent_node[now_node]
        return ret_list 



def main():
    Array = [2,1,8,3,9,5,4,7,6]
    flag = False
    bst = BST()
    
    # ここの処理もBSTクラスの中に収めてしまいたい
    for element in Array:
        if not(flag):
            bst.set_root(element)
            flag = True
        else:
            bst.insert(element)
    print(bst.parent_node)
    print("MAX-VALUE:",bst.take_max(),"MIN-VALUE:",bst.take_min())

    print("PreOrder  -> ",bst.get_preorder())
    print("InOder    -> ",bst.get_inorder())
    print("PostOrder -> ",bst.get_postorder())
    

        
if __name__ == "__main__":
    main()
