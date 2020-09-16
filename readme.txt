
compiling the file shows you the results of a few inputs, you can change/edit the commands in __name__ == '__main__':
 
command:pgtorlg(tuple of symbols,list of base strings,dictonary of productions)

Note:dictonary of productions: where the keys are left hand side strings of the productions and values are list of 
strings on the right hand side.

output:prints the right-linear grammer

 
example:
lets run G2 from frassier paper:
 pgtorlg(('a','b'),['ab'],{'a':['aab'],'aababb':['ab','abb']})

Note:e denotes epsilon
   uppercase letters enclosed in <> are non terminals
   lowercase letters are terminals
<S> --> ab
<S> --> aab<A>
<S> --> ab<AABABB>
<S> --> abb<AABABB>
<A> --> b
<A> --> ab<A>
<A> --> b<AABABB>
<A> --> bb<AABABB>
<AABABB> --> e
<AABABB> --> <AABABB>
<AABABB> --> b<AABABB>



Note:I have not removed the redundant productions yet, I will remove it in the final code, once we can test and confirm this code is working.


example command:pgtorlg(('a','b','c'),['aa'],{'a':['ab'],'aa':['c']})

output:
<S> --> aa
<S> --> ab<A>
<S> --> c<AA>
<A> --> a
<A> --> b<A>
<AA> --> e
