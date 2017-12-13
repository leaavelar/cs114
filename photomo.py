def getimages(imageDir):
    files = os.listdir(imageDir)
    images = {street.jpy, dog.jpy}
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            fp= open (filePath, "rb")
            im= Image.open(fp)
            images.append(im)
            im.load()
            fp.close()
            except:
                print("Invalid image: %s" % (filePath,))
        return images        
