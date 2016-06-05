# ImageCutter
Cut a image keeping a specific range from a point.

# Usage
```python
ImageCutter.cut(image, point, range)
```
- **image**: (PIL.Image.Image) The image to be cut.
- **point**: (dict:int) A integer dictionary with "x" and "y" keys.
- **range**: (int) The distance from de point to new image bounds.