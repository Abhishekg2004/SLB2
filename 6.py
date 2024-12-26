import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, bernoulli
    
data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 2, 3, 4): ")
    
data = list(map(int, data_input.split(',')))
freq = list(map(int, frequencies_input.split(',')))
    
expand = np.repeat(data , freq)
n = max(expand)

def normal_distribution(expand):
    
    mean = np.mean(expand)
    std_dev = np.std(expand)
    x = np.linspace(min(expand), n, 100)
    pdf = norm.pdf(x, mean, std_dev)

    print("Analyzing Normal Distribution:")
    
    plt.plot(x, pdf)
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.show()

def binomial_distribution(expand):
    
    p = np.mean(expand) / n
    x = np.arange(0, n+1)
    pmf = binom.pmf(x, n, p)
    
    print("Analyzing Binomial Distribution:")

    plt.bar(x, pmf)
    plt.title('Binomial Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def poisson_distribution(expand):
    
    lam = np.mean(expand)
    x = np.arange(0, n+1)
    pmf = poisson.pmf(x, lam)
    
    print("Analyzing Poisson Distribution:")

    plt.bar(x, pmf)
    plt.title('Poisson Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def bernoulli_distribution(expand):
    
    p = np.mean(data) / n
    x = [0, 1]
    pmf = bernoulli.pmf(x, p)
    
    print("Analyzing Bernoulli Distribution:")

    plt.bar(x, pmf)
    plt.title('Bernoulli Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

normal_distribution(expand)    
binomial_distribution(expand)   
poisson_distribution(expand)
bernoulli_distribution(expand)