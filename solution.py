import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 303247798 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    critical_value = np.sqrt(np.log(1/(1-p))/2)
    mean = np.mean(x)
    std_dev = np.std(x, ddof=1)
    left_boundary = mean - critical_value*std_dev/np.sqrt(n)
    right_boundary = mean + critical_value*std_dev/np.sqrt(n)
    return (left_boundary, right_boundary)
