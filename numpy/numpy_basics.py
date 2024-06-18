import numpy as np

python_list = [3, 2, 5, 8, 4, 9, 7, 6, 1]

array = np.array(python_list)
print(array)
print(python_list)
zeros = np.zeros((3, 5))
print(zeros)
random_np = np.random.random((4, 3))
print(random_np)
print(random_np.shape)

print(np.arange(-3, 4))
print(np.arange(4))
print(np.arange(-3, 10, 2))

print('Flatten and reshape')
some_array = np.random.random(4)
some_other = np.random.random(4)
together = np.array((some_array, some_other))
print(together)
print(together.flatten())
print(together.reshape(2, 4))
print(together.dtype)

integers = np.arange(1, 11)
print(integers.dtype)
also_integers = integers.astype(np.int32)
print(also_integers.dtype)

print(np.array([45, 67, True], dtype=np.int8).dtype)
print(np.array([45, 67, True], dtype=np.int8).astype(np.int64).dtype)
