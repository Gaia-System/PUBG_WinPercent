# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow as tf

# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential, load_model, Model
# from tensorflow.keras.layers import Dense, Input, Activation, BatchNormalization
# from tensorflow.keras.optimizers import SGD, Adam
# from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, ReduceLROnPlateau


# data_path = './'
# train_csv = pd.read_csv(data_path + 'structed_PUBG_data.csv')

# # data split train, valid, test
# feature, target = train_csv.iloc[:, :-1], train_csv.iloc[:, -1]
# X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size = 0.2, random_state = 0)
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.25, random_state = 0)


# # modeling
# inputs = Input(shape = (5,))
# hidden1 = Dense(units = 64)(inputs)
# bn1 = BatchNormalization()(hidden1)
# act_fn1 = Activation(activation = 'relu')(bn1)

# hidden2 = Dense(units = 32)(act_fn1)
# bn2 = BatchNormalization()(hidden2)
# act_fn2 = Activation(activation = 'relu')(bn2)

# output = Dense(units = 1)(act_fn2)
# model = Model(inputs = inputs, outputs = output)

# model.compile(optimizer = 'adam', loss = 'mse')

# model.summary()


# # callback
# check_point = ModelCheckpoint(filepath = './{epoch:03f}-{loss:.4f}-{val_loss:.4f}.hdf5',
#                               monitor = 'val_loss', verbose = 1, save_best_only = True, mode = 'min')

# reduce_lr = ReduceLROnPlateau(monitor = 'val_loss', factor = 0.8, patience = 3, vetbose = 1, min_lr = 1e-8)

# callback = [check_point, reduce_lr]

# model.fit(X_train, y_train, epochs = 8, validation_data = (X_val, y_val), batch_size = 16, verbose = 1, callbacks = callback)

# new_model = load_model('./2.000000-0.0249-0.0273.hdf5')