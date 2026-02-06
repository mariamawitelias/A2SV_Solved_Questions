class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        table  = {}
        for entry in paths: 
            parts = entry.split(" ") 
            directory = parts[0] 
            for file in parts[1:]: 
                name, content = file.split("(") 
                content = content[:-1]
                full_path = directory + "/" + name 
                if content not in table: 
                    table[content] = [] 
                table[content].append(full_path) 
        return [group for group in table.values() if len(group) > 1]








        