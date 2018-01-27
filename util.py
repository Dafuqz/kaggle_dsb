# !/usr/local/bin/python
def sparse_tuple_from(sequences, dtype=np.int32):
    """
    Author: github.com/igormq
    Create a sparse representention of input array. For handling one-hot vector in targets
    Args:
        sequences: a list of lists of type dtype where each element is a sequence
    Returns:
        A tuple with (indices, values, shape)"""
    indices = []
    values = []
    for i, seq in enumerate(sequences):
        indices.extend(zip([i]*len(seq), range(len(seq))))
        values.extend(seq)

    indices = np.asarray(indices, dtype=np.int64)
    values = np.asarray(values, dtype=dtype)
    shape = np.asarray([len(sequences), np.asarray(indices).max(0)[1]+1], dtype=np.int64)

    return indices, values, shape

def next_miniBatch():
    
def next_set():

def get_label():

def get_img():
