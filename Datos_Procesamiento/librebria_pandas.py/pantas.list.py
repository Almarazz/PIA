import numpy as np
import pandas as pd
df = pd.DataFrame([['Maria', 18], ['Luis', 22], ['Carmen', 20]], 
columns= ['Nombre', 'Edad',])
print(df)

import pandas as pd
dff = pd.DataFrame([{'Nombre': 'Maria', 'Edad' :18}, {'Nombre': 'Luis', 'Edad' :22}, {'Nombre': 'Carmen'}])
print(dff)

import pandas as pd
dff = pd.DataFrame(np.random.randn(4, 3), columns= ['a', 'b', 'c'])
print(dff)


