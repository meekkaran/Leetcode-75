# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
class Solution(object):
    
    def floodFill(self, image, sr, sc, color):
        # Avoid infinite loop if the new and old colors are the same...
        if image[sr][sc] == color: return image
        # Run the fill function starting at the position given...
        self.fill(image, sr, sc, color, image[sr][sc])
        return image
    def fill(self, image, sr, sc, color, cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return
        # If image[sr][sc] is not equal to previous color...
        if cur != image[sr][sc]: return
        image[sr][sc] = color# Update the image[sr][sc] as a color...
        # Make four recursive calls
        self.fill(image, sr-1, sc, color, cur)
        self.fill(image, sr+1, sc, color, cur)
        self.fill(image, sr, sc-1, color, cur)
        self.fill(image, sr, sc+1, color, cur)
