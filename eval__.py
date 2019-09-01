import numpy as np

#행렬의 덧셈과 뺄셈
class cal:

    def add(self,A,B):
        self.re=f'행렬A+행렬B: {A+B}'
        print(self.re)

    def sub(self,A,B):
        self.re=f'행렬A-행렬B: {A-B}'
        print(self.re)


r=np.array([[1,2],[3,4]])
p=np.array([[12,11],[2,4]])

def main():
    X= cal()
    X.add(r,p)
    X.sub(r,p)

main()
