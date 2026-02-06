class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for i in cpdomains:
            count, domain = i.split(" ")
            counts[domain] = counts.get(domain, 0) + int(count)
            while "." in domain: 
                domain = domain.split(".", 1)[1] 
                counts[domain] = counts.get(domain, 0) + int(count)
        res = [f"{cnt} {dom}" for dom, cnt in counts.items()]
        return res