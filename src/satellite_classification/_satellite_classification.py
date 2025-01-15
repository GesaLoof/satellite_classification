from subprocess import call


"""
You should write your module/set of function/class(es) here
"""

class satelliteclassification:
    """docstring for satellite_classification"""
    def __init__(self, arg):
        super(satelliteclassification, self).__init__()
        self.arg = arg


def data_loader(path_to_data):
    """
    Function that loads the data that we want to classify
    Args: 
        path_to_data (str): path to data that is supposed to be classified



    """
    
    return

"""
step1: download satellite images
using https://github.com/andolg/satellite-imagery-downloader/tree/main
tbd: zoom level
where to host the images (g drive?)



step2: pre-processing of sat images
step3: downloading training data
step4: pre-processing training data
step5: training classifier
step6: classifying data

"""