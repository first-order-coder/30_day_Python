import cPickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict

unpickle(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\cifar-10-batches-py\data_batch_1')