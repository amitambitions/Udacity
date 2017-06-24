"""Plot High prices for IBM"""
// Check that we are using a new library here for plotting puposes

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    df['High'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
