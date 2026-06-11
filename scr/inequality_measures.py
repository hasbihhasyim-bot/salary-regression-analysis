import numpy as np
import scipy.stats as stats

def calculate_shannon_entropy(salaries):
    """
    Menghitung Shannon Entropy dari sebaran gaji (untuk mereproduksi indeks 8.11 & 7.88).
    Formula: H(x) = -sum(p_i * ln(p_i))
    """
    salaries = np.array(salaries)
    salaries = salaries[salaries > 0]
    if len(salaries) == 0:
        return 0.0
    return stats.entropy(salaries)

def calculate_true_theil_t(salaries):
    """
    Menghitung True Theil T Index yang murni (GE(1)).
    Formula: T = (1 / N) * sum((x_i / mean) * ln(x_i / mean))
    """
    salaries = np.array(salaries)
    salaries = salaries[salaries > 0]
    n = len(salaries)
    if n == 0:
        return 0.0
    
    mean_salary = np.mean(salaries)
    shares = salaries / mean_salary
    shares = np.where(shares <= 0, 1e-10, shares)  # Mencegah galat log(0)
    
    theil_t = np.mean(shares * np.log(shares))
    return theil_t