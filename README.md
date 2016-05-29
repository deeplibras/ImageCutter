# libLibrasImageCutter
Crop all recorded frames from a libLibras (https://github.com/matheus-silva/libLibras) record folder keeping a specific ratio from a skeleton coord point.

# Usage
```
python libLibrasImageCutter.py <str:recordFolder> <int:ratio: <str:sklPoint> [<boolean:saveOriginalImage <str:saveFolder>]
```
- **<str:recordFolder>**: The path to the recording folder root.
- **<str:ratio>**: A integer bigger than "0". Will be the ratio from the center during the cropping.
- **<str:sklPoint>**: The skeleton point to be used as center of cropping. Valid points are:
- - ```HEAD, NECK, SHOULDER_LEFT, SHOULDER_RIGHT, ELBOW_LEFT, ELBOW_RIGHT, HAND_LEFT, HAND_RIGHT, TORSO, HIP_LEFT, HIP_RIGHT, FOOT_LEFT, FOOT_RIGHT```
- **<boolean:saveOriginalImage>**: (Optional) "true" if the original image should be saved.
- **<str:saveFolder>**: The path to save the new images. The original imagens will be saved in a subfolder called "original".