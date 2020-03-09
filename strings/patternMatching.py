class PatternMatch:
    def kmp_prefix(self,p):
        m = len(p)
        prefix_len = 0
        a =[0]
        for i in range(1,m):
            while prefix_len > 0 and p[i] != p[prefix_len]:
                prefix_len = a[prefix_len]
            if p[i] == p[prefix_len]:
                prefix_len+=1
            a.append(prefix_len)
        return a
    def kmp_match(self,t,p):
        n = len(t)
        m = len(p)
        q = 0 #number of matches
        a = self.kmp_prefix(p)
        for i in range(n):
            if q>0 and p[q] != t[i]:
                q = a[q]
            if t[i] == p[q]:
                q+=1
            if q == m-1:
                print('pattern match', i+2-m)
                q = a[q]
            print(q,i)

test = PatternMatch()
print(test.kmp_match("ababababca","ababababca"))

