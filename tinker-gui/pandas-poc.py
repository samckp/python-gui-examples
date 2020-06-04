dict = {"country": ["Brazil", "Russia", "India", "USA", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Washington", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "US", "SA"]
print(brics)