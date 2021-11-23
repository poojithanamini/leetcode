class disjoint:
    def __init__(self,n,i):
        self.parents=defaultdict(lambda:-1)
        self.rank=defaultdict(lambda:1)
        self.ans=[0]*(n+1)
        for x in i:self.ans[x]=1
    def find (self,i):
        if self.parents[i]==-1:
            return i
        else:
            self.parents[i]=self.find (self.parents[i])
            return self.parents[i]
    def union (self,i,j):
        x=self.find (i)
        y=self.find (j)
        if x!=y:
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
                self.parents[y]=x
                b=y;c=x
            elif self.rank[x]<self.rank[y]:
                self.parents[x]=y
                b=x;c=y
            else:
                self.parents[y]=x
                b=y;c=x
            if self.ans[b]>0:
                self.ans[c]+=self.ans[b]
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        e=len(nums)
        ds=disjoint(max(nums),nums)
        l=defaultdict(list)
        m=max(nums)+1
        for i in range(2,m):
            if len(l[i])==0:
                for x in range(i,m,i):
                    l[x].append(i)
        for i in nums:
            for j in l[i]:
                ds.union(i,j)
        return max(ds.ans)