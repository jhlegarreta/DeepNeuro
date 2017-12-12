
import os
import glob
import urllib

current_dir = os.path.realpath(os.path.dirname(__file__))

# Perhaps one day replace this with config files distributed at the level of modules.
dataset_dict = {'Segment_GBM_downsampled_wholetumor': [os.path.join(current_dir, 'Segment_GBM', 'downsampled_wholetumor.h5'), "https://www.dropbox.com/s/h2pj9hzruz3hq9a/wholetumor_downsampled_BRATS_submission.h5?dl=1"],
                'Segment_GBM_upsample_wholetumor': [os.path.join(current_dir, 'Segment_GBM', 'upsample_wholetumor.h5'), "https://www.dropbox.com/s/r4pelwcsscnuvc9/upsample_wholetumor_BRATS_submission.h5?dl=1"],
                'Segment_GBM_wholetumor': [os.path.join(current_dir, 'Segment_GBM', 'wholetumor.h5'), "https://www.dropbox.com/s/74tjx14ue11rc0q/wholetumor.h5?dl=1"],
                'Segment_GBM_enhancing': [os.path.join(current_dir, 'Segment_GBM', 'enhancing.h5'), "https://www.dropbox.com/s/usdal6cbkw3bceu/enhancingtumor_BRATS_submission.h5?dl=1"],
                }


def load(dataset):

    """Summary
    
    Parameters
    ----------
    dataset : TYPE
        Description
    
    Returns
    -------
    TYPE
        Description
    """

    # TODO: Loading progress indicator.

    dataset_path = dataset_dict[dataset][0]

    if not os.path.exists(os.path.dirname(dataset_path)):
        os.makedirs(os.path.dirname(dataset_path))

    if not os.path.exists(dataset_path):
        try:
            urllib.urlretrieve(dataset_dict[dataset][1], dataset_path)
        except Exception, e:
            if os.path.exists(dataset_path):
                os.remove(dataset_path)
            raise Exception

    return dataset_path


if __name__ == '__main__':
    pass