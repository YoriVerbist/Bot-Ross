from fastai.vision.all import *


paintings = DataBlock(blocks=(ImageBlock, CategoryBlock),
                    get_items=get_image_files,
                    splitter=RandomSplitter(valid_pct=0.2, seed=42),
                    get_y=parent_label,
                    item_tfms=RandomResizedCrop(244, min_scale=0.3),
                    batch_tfms=aug_transforms())
dls = paintings.dataloaders('../data/paintings', nuw_workers=0)

model = ccn_learner(dls, resnet34, metrics=accuracy)
model.load(../model/test.pth) # Need to change path to model


def predict(image):
    return model.predict(image)


