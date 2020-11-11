# Bot-Ross
This is a paintings classifier that says by which painter the painting is drawn. There is also a neural style transfer added so you can apply the painting style to other images.

## Neural Style Transfer
### How does it work?
The principle is simple: we define two distances, one for the content (DC) and one for the style (DS). DC measures how different the content is between two images while DS measures how different the style is between two images. Then, we take a third image, the input, and transform it to minimize both its content-distance with the content-image and its style-distance with the style-image.

### Example
##### Input and style image:
![](/data/paintings/Red-Eyed_Crocodile_Skink.jpg)
![](/data/paintings/van-gogh-starry-night.png)

##### Output image:
![](/data/output/index.png)