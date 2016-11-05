from PIL import Image, ImageOps

from Config import Config


class ImageProcessor:
    def __init__(self):
        pass

    def processAllStaticPhotos(self):
        self._discoverAllStaticPhotos()
        for eachBigPhoto in self.allStaticPhotoFilePointers:
            self._makeThumbnailsOfPhoto(eachBigPhoto)

    def _discoverAllStaticPhotos(self):
        self.allStaticPhotoFilePointers = []
        import os
        for file in os.listdir(Config.staticFolderPath):
            self.allStaticPhotoFilePointers.append(file)

    def _makeThumbnailsOfPhoto(self, bigPhoto):
        allResolutions = [
        {'resolutionName': "ldpi", 'x': 785, 'y': 325},
        {'resolutionName': "mdpi", 'x': 1050,'y':  430},
        {'resolutionName': "hdpi", 'x': 1575,'y':  645},
        {'resolutionName': "xhdpi", 'x': 2100,'y':  860},
        {'resolutionName': "xxhdpi", 'x': 3150,'y':  1290},
        {'resolutionName': "xxxhdpi", 'x': 4200,'y':  1720},
        {'resolutionName': "1x", 'x': 105, 'y': 105},
        {'resolutionName': "2x", 'x': 210, 'y': 210},
        {'resolutionName': "3x", 'x': 313, 'y': 313}]
        
        for resolution in allResolutions:
            self._makeThumbnail(resolution, bigPhoto)

    def _makeThumbnail(self, resolution, bigPhoto):

        size = resolution['x'], resolution['y']
        infile = bigPhoto

        import os
        outfile = Config.dynamicFolderPath + bigPhoto + '.' + resolution['resolutionName'] + ".jpeg"
        if infile != outfile:
            imageRelativePath = Config.staticFolderPath + infile
            image = Image.open(imageRelativePath)
            processedImage = ImageOps.fit(image, size)#open("../static/"+infile)
            processedImage.save(outfile, "JPEG")
