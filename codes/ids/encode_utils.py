import pandas as pd
import numpy as np
import re

def data2char_index(X, max_len, is_remove_comment = False):
    alphabet = " abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    result = [] 
    for data in X:
        mat = []
        for ch in data:
            ch = ch.lower()
            if ch not in alphabet:
                continue
            mat.append(alphabet.index(ch))
        result.append(mat)
    result_np = np.array(result, dtype=object).astype(np.float32)
    X_char = np.pad(result_np,(0,max_len-len(result_np[0])), 'constant')
    return X_char[0]

def data_to_symbol_tag(X, max_len ,is_remove_comment = False):
    symbol = " -,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    result = [] 
    for data in X:
        mat = []
        for ch in data:
            ch = ch.lower()
            if ch not in symbol:
                mat.append(0)
            else :
                mat.append(symbol.index(ch))
        result.append(mat)
    result_np = np.array(result, dtype=object).astype(np.float32)
    X_char = np.pad(result_np,(0,max_len-len(result_np[0])), 'constant')
    return X_char[0]