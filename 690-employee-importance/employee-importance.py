"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = {emp.id: emp for emp in employees}
        def dfs(id):
            imp = mapp[id].importance
            for i in mapp[id].subordinates:
                imp += dfs(i)
            return imp
        return dfs(id)
        
        