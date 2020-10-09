#! python3

import pandas as pd
import numpy as np

## Wikipedia example: 3 features, 2 labels ##

df = pd.DataFrame(  [ [6, 180, 12, 'male'],
                      [5.92, 190, 11, 'male'],
                      [5.58, 170, 12, 'male'],
                      [5.92, 165, 10, 'male'],
                      [5, 100, 6, 'female'],
                      [5.5, 150, 8, 'female'],
                      [5.42, 130, 7, 'female'],
                      [5.75, 150, 9, 'female'] ], 

                    columns=['height', 'weight', 'foot_size', 'sex'])

print(df, '\n')