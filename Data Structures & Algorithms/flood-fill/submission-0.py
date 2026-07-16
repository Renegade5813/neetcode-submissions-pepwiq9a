class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color=image[sr][sc]
        if color==org_color:
            return image

        def dfs(image,r,c,visit):
            R,C=len(image), len(image[0])
            if r<0 or c<0 or r==R or c==C or (r,c) in visit or image[r][c]!=org_color:
                return 
            if image[r][c]==org_color:
                image[r][c]= color
                
            visit.add((r,c))
            dfs(image,r-1,c,visit)
            dfs(image,r+1,c,visit)
            dfs(image,r,c-1,visit)
            dfs(image,r,c+1,visit)
            return
        dfs(image,sr,sc,set())
        return image

        