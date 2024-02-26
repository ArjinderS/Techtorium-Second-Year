
#Week 3 Thursday/Friday Testing Experiment

'''
from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

# test_assert_examples.py

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
'''

'''
import pandas as pd

df = pd.read_excel('C:/Users/icego/Desktop/Techtorium/Second Year/Projects/Term 1 24/rugby_players_data-1.xlsx')
df_sorted = df.sort_values(by='Age', ascending=True)
#df_new = df[['col3']]

print(df_sorted)
'''

import pandas as pd
import time

def test_sorting(df, sort_type):
    start_time = time.time()
    if sort_type == "bubble":
        df.sort_values(by='Age', kind='bubble', inplace=True)
    elif sort_type == "insertion":
        df.sort_values(by='Age', kind='insertion', inplace=True)
    elif sort_type == "selection":
        df.sort_values(by='Age', kind='selection', inplace=True)
    elif sort_type == "merge":
        df.sort_values(by='Age', kind='merge', inplace=True)
    elif sort_type == "quick":
        df.sort_values(by='Age', kind='quick', inplace=True)
    end_time = time.time()
    return end_time - start_time

df = pd.read_excel('C:/Users/icego/Desktop/Techtorium/Second Year/Projects/Term 1 24/rugby_players_data-1.xlsx')
data_types = {
    'Sorted': df['Age'].sort_values(),
    'Unsorted': df['Age'].sample(frac=1).reset_index(drop=True),
    'Reversed': df['Age'].sort_values(ascending=False),
    'Empty': pd.Series(dtype=int),
    'Duplicate': pd.concat([df['Age'], df['Age']]).reset_index(drop=True)
}

results = {}

for data_type, series in data_types.items():
    results[data_type] = {}
    for sort_algo in ["bubble", "insertion", "selection", "merge", "quick"]:
        df_copy = pd.DataFrame({'Age': series})
        time_taken = test_sorting(df_copy, sort_algo)
        results[data_type][sort_algo] = time_taken

results_df = pd.DataFrame(results)

results_df.to_csv('sorting_results.csv', index_label='Data Type')

print("Sorting results saved to 'sorting_results.csv'")
