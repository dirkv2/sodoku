
class Solution:
    def square(self,x,y):
        if y==0 or y==3 or y==6:
            offsety=1
        if y==1 or y==4 or y==7:
            offsety=0
        if y==2 or y==5 or y==8:
            offsety=-1
        if x==0 or x==3 or x==6:
            offsetx=1
        if x==1 or x==4 or x==7:
            offsetx=0
        if x==2 or x==5 or x==8:
            offsetx=-1
        x=x+offsetx
        y=y+offsety
        rlist=self.board[y-1][x-1:x+1+1]
        rlist+=self.board[y][x-1:x+1+1]
        rlist+=self.board[y+1][x-1:x+1+1]
        #print("square is", rlist, x,y)
        return(rlist)
    def solveSudoku(self, board):
        self.board=board
        running=1
        while running:
            running=0
            for y in range(0,9):
                for x in range(0,9):
                    #print("INIT LOCATION",x,y)
                    if board[y][x]==0:
                        running=1
                        #print("CHECKING LOCATION", x, y)
                        count=0
                        for i in range(1,10):
                            #print("checking i =",i,end=" ")
                            # check row
                            if i in board[y][0:9]:
                                #print(i,"was found in row xy location[0-8][",y,"]")
                                continue
                            # check column
                            rowlist=[]
                            for row in range(0,9):
                                rowlist+=[board[row][x]]
                            if i in rowlist:
                                #print(i,"was found in column location",rowlist)
                                continue
                            # check square
                            if i in self.square(x,y):
                                #print(i,"was found in self.square(",x,y,")")
                                continue
                            xsol=x
                            ysol=y
                            isol=i
                            count+=1
                        if count == 1:
                            #print("**************Found only one solution for",xsol,ysol,":",isol)
                            #print("Replacing data...")
                            board[ysol][xsol]=isol
                            #print("new solution:")
                            #print(board)

#board=["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
board=[ [5,3,0,0,7,0,0,0,0],\
        [6,0,0,1,9,5,0,0,0],\
        [0,9,8,0,0,0,0,6,0],\
        [8,0,0,0,6,0,0,0,3],\
        [4,0,0,8,0,3,0,0,1],\
        [7,0,0,0,2,0,0,0,6],\
        [0,6,0,0,0,0,2,8,0],\
        [0,0,0,4,1,9,0,0,5],\
        [0,0,0,0,8,0,0,7,9]]

newsolution=Solution()
newsolution.solveSudoku(board)
print(board)
