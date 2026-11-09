class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        ind = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]] += 1
                    break
        
        q = deque([c for c in ind if ind[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for n in adj[c]:
                ind[n] -= 1
                if ind[n] == 0:
                    q.append(n)
        
        if len(res) != len(ind):
            return ""
        
        return "".join(res)