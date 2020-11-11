# Bot-Ross
This is a paintings classifier that says by which painter the painting is drawn. There is also a neural style transfer added so you can apply the painting style to other images.

## Neural Style Transfer
### How does it work?
The principle is simple: we define two distances, one for the content (DC) and one for the style (DS). DC measures how different the content is between two images while DS measures how different the style is between two images. Then, we take a third image, the input, and transform it to minimize both its content-distance with the content-image and its style-distance with the style-image.

### Examples
##### Input and style image:
<img src="/data/paintings/lion.jpg" width="400">
<img src="/data/paintings/van-gogh-starry-night.png" width="400">

##### Output image:
<img src="/data/output/index.png" width="400">

##### Style image:
<img src="/data/paintings/waves1.jpeg" width="400">

##### Output image:
<img src="/data/output/lion.png" width="400">

##### Style image:
<img src="/data/paintings/ocean.jpg" width="400">

##### Output image:
<img src="/data/output/lion2.png" width="400">