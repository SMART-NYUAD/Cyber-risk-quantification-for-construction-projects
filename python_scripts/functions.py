
"""# Labeling and modeling

### Define functions and models
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
import copy
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge, LinearRegression
import numpy as np
import collections
import seaborn as sns
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def or_gate(*probabilities):
    product = 1
    for p in probabilities:
        product *= (1 - p)
    return 1 - product

def and_gate(*probabilities):
    product = 1
    for p in probabilities:
        product *= p
    return product

def set_seed(seed = 0):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    np.random.seed(seed)

set_seed(0)

# Define the linear regression model
class LinearModel(nn.Module):
    def __init__(self, input_size):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return self.linear(x)

"""* Link [here](https://www.yourdatateacher.com/2021/05/17/how-to-explain-neural-networks-using-shap/)
* Remember that we only care about the absolute value of the shap values, and we do not care about the positives or negatives.
"""
import shap

risk_factors = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.1', '2.2.1',
       '2.2.2', '2.2.3', '2.2.4', '2.2.5', '2.2.6', '2.2.7', '2.2.8', '2.3.1',
       '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8', '2.4',
       '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.1',
       '4.2', '4.3', '4.4', '4.5', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6',
       '5.7']

num_input_units=259


def train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs, label):
    model.to(device) # Moving model to device

    val_losses = []
    min_val_loss = np.inf
    best_model = None
    best_epoch = -1

    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device) # Moving data to device
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        # Evaluate the model on the validation set after each epoch
        with torch.no_grad():
            model.eval()
            epoch_outputs = []
            epoch_labels = []
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device) # Moving data to device
                outputs = model(inputs)
                epoch_outputs.append(outputs.cpu().numpy()) # Moving outputs to CPU
                epoch_labels.append(labels.cpu().numpy()) # Moving labels to CPU
            epoch_outputs = np.concatenate(epoch_outputs)
            epoch_labels = np.concatenate(epoch_labels)
            epoch_val_loss = criterion(torch.tensor(epoch_outputs).to(device), torch.tensor(epoch_labels).to(device)).item()
            val_losses.append(epoch_val_loss)

            if epoch_val_loss < min_val_loss:
                min_val_loss = epoch_val_loss
                best_model = copy.deepcopy(model.state_dict())
                best_epoch = epoch

        model.train()

    # Load the best model
    model.load_state_dict(best_model)

    return model, val_losses, best_epoch, min_val_loss

def train_combined_model(model, train_loader, val_loader, criterion, optimizer, num_epochs):
    model.to(device) # Moving model to device

    val_losses = []
    min_val_loss = np.inf
    best_model = None
    best_epoch = -1

    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device) # Moving data to device
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        # Evaluate the model on the validation set after each epoch
        with torch.no_grad():
            model.eval()
            epoch_val_loss = 0.0
            num_batches = 0
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device) # Moving data to device
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                epoch_val_loss += loss.item()
                num_batches += 1
            epoch_val_loss /= num_batches  # Average loss
            val_losses.append(epoch_val_loss)

            if epoch_val_loss < min_val_loss:
                min_val_loss = epoch_val_loss
                best_model = copy.deepcopy(model.state_dict())
                best_epoch = epoch

        model.train()

    model.load_state_dict(best_model)

    return model, val_losses, best_epoch, min_val_loss
