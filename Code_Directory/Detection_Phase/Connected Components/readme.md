# Connected Components Algorithm
The Connected Components Algorithm is used to identify and label connected regions (components) in a binary image. It is commonly used in image processing to detect and isolate distinct objects within an image.


## Major Assumption
The signatures we want to extract will always be connected.

## Idea
To remove that non-useful text, we used a connected components labeling algorithm to fit a tight box around the signature.<br>
Two passes of connected component labeling were applied to get the connected components in an image. 

Then rectangle fitting was applied to the detected connected components. Components are selected on the basis of the maximum area of the rectangle.

After passing images through OCR we will use ***Connected Components Algorithm*** to extract the signatures
from the image.

### Tools Used

1. OpenCV [see here](F:\BTech\Capstone Project\Signature_Detecttion-Verfication\Project_Code\Signature_Detection\Line Sweep\readme.md)
2. Python Image Library (PIL) [see here](F:\BTech\Capstone Project\Signature_Detecttion-Verfication\Project_Code\Signature_Detection\Line Sweep\readme.md)
3. Union Find Array (Self made module to implement Union Find)


### Failure Scenarios
This technique is very tightly based on our assumption of always having connected signatures. We might have signatures which are not connected. 

> Example 
> 
> ![NotConnectedExample.png](../../../Project_Images/NotConnectedExample.png)
> 
> So the output of this signature will be wrong
> 
> ![WrongCCResult.png](../../../Project_Images/WrongCCResult.png)
    

## Documentation 
* Connected Component Algorithm - https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
* Union Find Array - https://www.geeksforgeeks.org/number-of-connected-components-of-a-graph-using-disjoint-set-union/
