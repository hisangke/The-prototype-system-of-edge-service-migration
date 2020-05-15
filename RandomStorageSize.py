import numpy as np
def RandomStorageSize():
    data=[233.0,30.8,110.0,54.7,77.3,103.0,44.6,83.2,97.7,170,230,4.78,4.73,506.0,507.0,527.0,548.0]
    data=[d/1024.0 for d in data]
    return np.random.choice(data,1).tolist()[0]
