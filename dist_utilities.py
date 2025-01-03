from sympy import fwht, ifwht
import math
import numpy as np

def filter_counts(counts, num_keep):
    '''Returns a dict with only the largest num_keep elements.'''
    list_counts=sorted(counts.items(), key=lambda x: -x[1])
    filtered_counts=list_counts[:num_keep:]
    return {k:v for (k,v) in filtered_counts}

def fill_counts_range(counts1: dict, counts2: dict, num_keep, num_qubits):
    '''We embed the counts into a power of 2 number of basis states by padding with zeros.
    Some things to note: This is necessary to match the keys for both dict. Also,
    since FWHT solvers only see a vector, when they pad they can do it in an
    unphysical fashion (e.g., 111 is in the distribution so no padding should occur after the 111.)
    args: num_keep: should be a power of 2. Both list should have the same keys for the
    inverse Fourier transforms to generate correct results.'''
    counts1_keys=set(counts1.keys())
    counts2_keys=set(counts2.keys())
    new_counts1={}
    new_counts2={}
    exist_keys=list(counts1_keys.union(counts2_keys))
    exist_keys=[int(elem, 2) for elem in exist_keys]
    exist_keys=sorted(exist_keys)
    print("max exist ", max(exist_keys))
    print("min exist ", min(exist_keys))
    print("size before ", len(exist_keys))
    max_key=exist_keys[-1]
    min_key=exist_keys[0]
    current_len=len(exist_keys)
    if num_keep>=max_key:
        max_key=num_keep
        all_keys=list(range(num_keep))
    else: #num_keep<max_key. we will pad between until the size is right
        if num_keep<current_len: #the current len exceeds what was kept.
            # go to the nearest larger power of 2.
            power=math.ceil(math.log2(current_len))
            max_key=num_keep=2**power
        all_possible_between=iter(range(min_key, max_key))
        all_possible_before=iter(range(0, min_key))
        new_keys_between=[]
        new_keys_before=[]
        # we should pad with elements between the min and max keys before outside.
        while len(new_keys_between)<num_keep-current_len:
            try:
                next_elem=next(all_possible_between)
                while next_elem in exist_keys:
                    try:
                        next_elem=next(all_possible_between)
                    except StopIteration:
                        raise StopIteration
            except StopIteration:
                break
            new_keys_between.append(next_elem)
        while len(new_keys_between)+len(new_keys_before)+len(exist_keys)<num_keep:
            # pad with before elements
            next_elem=next(all_possible_before)
            new_keys_before.append(next_elem)

        all_keys=exist_keys+new_keys_between+new_keys_before
        
    all_keys=[bin(elem)[2::].zfill(num_qubits) for elem in all_keys]

    for k in all_keys:
        new_counts1[k]=counts1.get(k,0)
        new_counts2[k]=counts2.get(k,0)
    assert len(all_keys)==len(new_counts1)
    assert len(all_keys)==len(new_counts2)

    return sorted(list(all_keys), key=lambda x: int(x)), new_counts1, new_counts2

# def real_func(num):
#     return num.real

def fill_dist(counts: dict, num_qubits):
    '''Pads with zeros until the size of counts is 2^num_qubits.'''
    all_bins=[bin(i)[2::].zfill(num_qubits) for i in range(2 ** num_qubits)]
    for basis in all_bins:
        counts[basis]=counts.get(basis, 0)

# def apply_kron(mat, n):
#     new_mat=deepcopy(mat)
#     for _ in range(n-1):
#         new_mat=np.kron(new_mat, mat)
#     return new_mat

def get_quasi_corrected(noisy_noise_est_vec, counts_vec):
    '''Solves the circulant structure system with FWHT.'''
    fft_calmat_col=np.array(fwht(noisy_noise_est_vec), dtype=float)
    fft_noisy_counts=np.array(fwht(counts_vec), dtype=float)
    print(len(fft_calmat_col))
    print(len(fft_noisy_counts))
    quasi_corrected_counts=ifwht(np.divide(fft_noisy_counts, fft_calmat_col, out=np.zeros(len(fft_noisy_counts)), where=(fft_calmat_col!=0)))
    return np.array(quasi_corrected_counts)[0:len(noisy_noise_est_vec)]

def label_quasis(counts, all_keys):
    '''Add labels to counts given by all_keys.'''
    counts_dict={all_keys[idx]:elem for idx, elem in enumerate(counts)}
    return counts_dict


def _update_label(key1, key2):
    num_qubits=len(key1)
    return bin(int(key1, 2) ^ int(key2, 2))[2:].zfill(num_qubits)

def convert_to_first_col(counts: dict, label: str):
    '''The label is the associated column of tilde A. Counts is the associated column values.
    We should convert these to the first column by the symmetry rule described in the paper.'''
    counts={_update_label(label, key):value for (key, value) in counts.items()}
    return counts