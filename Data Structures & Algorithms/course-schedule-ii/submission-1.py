class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        out = []
        visit, cycle =set(), set()
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            #visit.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            out.append(crs)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return out