import builtins
from collections import deque
def ASSERT_(c,t='\U00002a33'):assert c,t;return c
DEGEN_=lambda g:deque(g,maxlen=0)
print=lambda *a,**k:builtins.print(*a,**k)or(a[0]if a else None)

import subprocess
class pait:
    def __call__(𝕊,s,*a,**k):
        proc = subprocess.Popen(s.split(' '),*a,**k)
        if "background" not in k: proc.wait()
        return proc
    def _parse(𝕊,o): return o.read().decode()
    
    def r(*a,**k): return 𝕊(*a,**k).returncode
    def S(𝕊,*a,**k): return 𝕊._parse(𝕊(*a,stdout=subprocess.capture,**k).stdout)
    def E(𝕊,*a,**k): return 𝕊._parse(𝕊(*a,stderr=subprocess.capture,**k).stderr)
    def b(𝕊,*a,**k): return 𝕊(*a,background=True,stdout=subprocess.capture,stderr=subprocess.capture,**k)
    def B(𝕊,*a,**k):
        o = 𝕊(*a,stdout=subprocess.capture,stderr=subprocess.capture,**k)
        return 𝕊._parse(o.stdout), 𝕊._parse(o.stderr)
    def A(𝕊,*a,**k):
        o = 𝕊(*a,stdout=subprocess.capture,stderr=subprocess.capture,**k)
        return o.returncode, 𝕊._parse(o.stdout), 𝕊._parse(o.stderr)
pait = pait()
def  x():
    print(1)
    print(2) if   True 
    print(0) if   False 
    L = [0]
    print((L[0] := '3'), L)
    print(4)
    print((x $> x**2)(5))
    print(( lambda x: x**2)(5))
    h = <$x$>x**2
    print(h(5))
print(x())

j=(x=2$>x**2)
print(j(2))

k=<$f=(x$>x**2),y=5$>print(f(y*2), ARGS_, KWARGS_)
print(k(y=8))

print((x$>[x+5,ARGS_[0] [1],KWARGS_])(1, "hello", 3, yay="yay"))

# prints [6, (3, 2), {'yay': 'yay'}]
# 
# print(<$x,y$>x+y,2)

m=<$x$>(<$$>list(map(x,ARGS_[0])))
f=<$$>ARGS_[0]**2
print(*𝕞(f)([1,2,3]))
print(*[f(x) for x in [1,2,3]])

h=x,y$>x**2+y
print(h(5,1))