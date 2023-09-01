import pandas as pd
import numpy as np
import re
import tensorflow as tf
import urllib.parse
import html
import base64
import binascii


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


def encode_payload_decode(text: str):
    old_result: str = text
    new_result: str = ''
    while True:
        # URL encoder
        new_result = urllib.parse.unquote_to_bytes(old_result).decode('utf-8')
        
        # HTML entities encoder
        new_result = html.unescape(new_result)

        # Hex encoder
        try:
            new_result = bytes.fromhex(new_result).decode('utf-8')
        except ValueError:
            pass

        # Base64 encoder
        try:
            new_result = base64.b64decode(new_result)
        except binascii.Error:
            pass
        except ValueError:
            pass

        print('\n\n\n =====Encode Result=====')
        print('Old', old_result)
        print('New', new_result)
        if new_result == old_result:
            break
        else:
            old_result = new_result
    return new_result
