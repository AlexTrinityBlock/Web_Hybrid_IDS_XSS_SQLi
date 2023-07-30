import pandas as pd
import numpy as np
import re
import tensorflow as tf


def data2char_index(X, max_len):
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
    X_char = tf.keras.preprocessing.sequence.pad_sequences(np.array(
        result, dtype=object), padding='post', truncating='post', maxlen=max_len)
    return X_char


def data_to_symbol_tag(X, max_len):
    symbol = " -,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    result = []
    for data in X:
        mat = []
        for ch in data:
            ch = ch.lower()
            if ch not in symbol:
                mat.append(0)
            else:
                mat.append(symbol.index(ch))
        result.append(mat)
    X_char = tf.keras.preprocessing.sequence.pad_sequences(np.array(
        result, dtype=object), padding='post', truncating='post', maxlen=max_len)
    return X_char
