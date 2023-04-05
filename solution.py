import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 303247798 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)  # используем несмещенную оценку стандартного отклонения

    t_critical = abs(np.round(norm.t.ppf((1 - p) / 2, n - 1), 4))  # критическое значение t-статистики

    left_boundary = round(sample_mean - (t_critical * sample_std / np.sqrt(n)), 4)
    right_boundary = round(sample_mean + (t_critical * sample_std / np.sqrt(n)), 4)

    return (left_boundary, right_boundary)
