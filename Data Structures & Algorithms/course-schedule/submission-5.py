class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mp = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites: 
            mp[course].append(pre)

        visit = set()

        def dfs(crs):
            # base
            if crs in visit:
                return False 
            
            if mp[crs] == []:
                return True 

            # Recursive / backtrack
            visit.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False 
            
            visit.remove(crs)
            mp[crs] = []
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False 

        return True








# how do i know this is a graph questions???

# return true if it's possible to finish all courses, or return false 
# numCourses are the number of courses have to take 
# prerequist[course, prerequest cource]

# create a course map 
# assign each course prerequest into map 

# create dfs to search 
# base case: 