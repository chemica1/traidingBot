import numpy as np

#행렬의 덧셈과 뺄셈
class cal:

    r = np.array([[1, 2], [3, 4]])
    p = np.array([[12, 11], [2, 4]])

    def add(self,A,B):
        print(f'행렬A+행렬B: {(A+B)}')

    def sub(self,A,B):
        print(f'행렬A-행렬B: {(A-B)}')

    def main(self):
        X= cal()
        X.add(self.r, self.p)
        X.sub(self.r, self.p)

if __name__ == '__main__':
    a = cal()
    a.main()