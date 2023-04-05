import pandas as pd
import numpy as np

chat_id = 225497605 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return x.sum()/(x.size*90)
