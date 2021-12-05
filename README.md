This is the walkthrough code that goes along with https://www.youtube.com/watch?v=QRQBTkCLpFY

The main code is in `notebook.ipynb`. All the `.py` files are just helpers.

~~If you want to run this, you may need to install the nightly versions of `torch` and `torchvision` (as of 15 September 2021).~~

You'll also probably need the master branch of timm: `pip install git+https://github.com/rwightman/pytorch-image-models.git` 

Other requirements are in `requirements.txt`.

**EDIT - 5 Dec 2021**

FX feature extraction was included in the latest TorchVision release some weeks ago so no need for the nightly. Also note that I made an improvement to the node naming convention (to do with postfixes of repeated node names) prior to the release, so the node names used in this version of the notebook are no longer valid. Confused? Read the notebook and you'll see what I mean :)
