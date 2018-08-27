import numpy as np

a = [i**2 for i in range(10)]
a = np.array(a)

print(type(a[0]))

filename = 'test_data.npz'
np.savez(filename, a)

filename = 'test_data.npy'
np.save(filename, a, allow_pickle=False)
