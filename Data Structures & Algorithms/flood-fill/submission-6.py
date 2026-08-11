class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        org_color= image[sr][sc]
        if image[sr][sc]==color:
            return image
        
        R,C= len(image), len(image[0])
        def dfs(image,r,c):
            if r<0 or c<0 or r==R or c==C or image[r][c]!=org_color:
                return
            image[r][c]=color
            neighbor=((0,1),(0,-1),(1,0),(-1,0))
            for dr,dc in neighbor:
                dfs(image,r+dr,c+dc)
        dfs(image,sr,sc)
        return image
        