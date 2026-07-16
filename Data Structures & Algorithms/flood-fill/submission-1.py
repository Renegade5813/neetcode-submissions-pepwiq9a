class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color=image[sr][sc]
        if color==org_color:
            return image
        R,C=len(image), len(image[0])

        def dfs(image,r,c):
            
            if r<0 or c<0 or r==R or c==C  or image[r][c]!=org_color:
                return 
            if image[r][c]==org_color:
                image[r][c]= color
                
            dfs(image,r-1,c)
            dfs(image,r+1,c)
            dfs(image,r,c-1)
            dfs(image,r,c+1)
            return
        dfs(image,sr,sc)
        return image

        