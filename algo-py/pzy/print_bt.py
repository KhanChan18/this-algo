class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def level_print(tree):
    if tree==None:
        return
    q=[]
    q.append(tree)
    results={}
    level=0
    current_level_num=1
    nextlevelnum=0
    d=[]
    while q:
        current=q.pop(0)
        current_level_num-=1
        d.append(current.data)
        if current.left!=None:
            q.append(current.left)
            nextlevelnum+=1
        if current.right!=None:
            q.append(current.right)
            nextlevelnum+=1
        if current_level_num==0:
            current_level_num=nextlevelnum
            nextlevelnum=0
            results[level]=d
            d=[]
            level+=1
    print(results)

if __name__=='__main__':
    tree=node('D',node('B',node('A'),node('C')),node('E',right=node('G',node('F'))))
    level_print(tree)
