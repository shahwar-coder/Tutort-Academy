'''
661. Image Smoother
https://leetcode.com/problems/image-smoother/
'''


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows=len(img)
        cols=len(img[0])
        new_matrix=[[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                count=0
                total=0

                # top-left
                if i-1>=0 and j-1>=0:
                    total+=img[i-1][j-1]
                    count+=1

                # top
                if i-1>=0:
                    total+=img[i-1][j]
                    count+=1

                # top-right
                if i-1>=0 and j+1<cols:
                    total+=img[i-1][j+1]
                    count+=1

                # left
                if j-1>=0:
                    total+=img[i][j-1]
                    count+=1

                # right
                if j+1<cols:
                    total+=img[i][j+1]
                    count+=1

                # bottom-left
                if i+1<rows and j-1>=0:
                    total+=img[i+1][j-1]
                    count+=1

                # bottom-right
                if i+1<rows and j+1<cols:
                    total+=img[i+1][j+1]
                    count+=1

                # bottom
                if i+1<rows:
                    total+=img[i+1][j]
                    count+=1

                total+=img[i][j]
                count+=1
                avg=total//count
                new_matrix[i][j]=avg

        return new_matrix


'''
### Core Idea (Matrix Averaging)
For every pixel in the image, replace it with the **average value** of:
- itself
- all valid neighbors around it (up to 8)
Neighbors count changes near edges/corners.

Use **integer division (//)** to round down the average.

### How We Process Each Cell
For each img[i][j]:
- Look at up to 8 surrounding cells:
      top-left, top, top-right,
      left, right,
      bottom-left, bottom, bottom-right
- Only include a neighbor if it is inside the image bounds.
- Keep two counters:
      total → sum of all included values
      count → number of included values
- new_matrix[i][j] = total // count

### Why Bound Checks Are Needed
- Pixels at borders do not have 8 neighbors.
- Checking index limits ensures we don't go out-of-bounds.

### Example Behavior
Corner cells may have only 3 neighbors → smaller count  
Center cells have all 8 neighbors → full smoothing

### Output Matrix
- Same size as input
- Each cell becomes the smoothed (averaged) value

### Complexity
Let n = rows, m = columns
- Time: O(n * m * 9) = O(n * m)  
  (constant 9 checks per cell)
- Space: O(n * m) for the resulting matrix

### Why This Works
We compute a local average for each cell independently.
This reduces noise and creates a “smoothing” effect on the image.

'''
