class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_clr=image[sr][sc]
        R,C=len(image),len(image[0])
        visit=set()

        def dfs(image,r,c,visit):
            if r<0 or c<0 or r==R or c==C or image[r][c]!=org_clr or (r,c) in visit:
                return 
            if image[r][c]==org_clr:
                image[r][c]=color
            
            visit.add((r,c))
            neighbors=((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbors:
                dfs(image,r+dr,c+dc,visit)
            return
        dfs(image,sr,sc,visit)
        return image
        