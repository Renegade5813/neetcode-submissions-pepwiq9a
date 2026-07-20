class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_clr=image[sr][sc]
        if org_clr == color: return image
        R,C=len(image),len(image[0])

        def dfs(image,r,c):
            if r<0 or c<0 or r==R or c==C or image[r][c]!=org_clr:
                return 
            image[r][c]=color
            
            neighbors=((1,0),(-1,0),(0,1),(0,-1))
            for dr,dc in neighbors:
                dfs(image,r+dr,c+dc)
        dfs(image,sr,sc)
        return image