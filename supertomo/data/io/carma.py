from scipy.io import loadmat
import numpy as np
from supertomo.data.containers.image import Image
from supertomo.data.containers.array_detector_data import ArrayDetectorData




def read_carma_mat(filename):
    """
    A simple implementation for the carma file import in Python
    :param filename: Path to the Carma .mat file
    :return: Returns a 2D nested list of SuperTomo Image objects. The first dimension
             of the list corresponds to the Photosensors count and second, to the
             Detectors count
    """
    assert filename.endswith(".mat")
    measurement = "meas_" + filename.split('/')[-1].split('.')[0]
    data = loadmat(filename)[measurement]

    # Get necessary metadata
    spacing = list(data['PixelSize'][0][0][0][::-1])
    shape = list(data['Size'][0][0][0][::-1])

    detectors = int(data['DetectorsCount'][0][0][0])
    photosensors = len(data["PhotosensorsTime"][0][0])

    # Initialize data container
    container = ArrayDetectorData(detectors, photosensors)

    # Read images
    for i in range(photosensors):
        for j in range(detectors):
            name = 'pixel_d{}_p{}'.format(j, i)
            if shape[0] == 1:
                container[i, j] = Image(np.transpose(data[name][0][0])[0], spacing[1:])
            else:
                container[i, j] = Image(np.transpose(data[name][0][0]), spacing)


    return container
