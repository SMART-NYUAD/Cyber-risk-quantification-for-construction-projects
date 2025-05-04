def train_and_predict(label):
    set_seed(0)
    model = NeuralNetwork()

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df_one_hot, test_size=0.2)

    # Prepare the training data
    train_x = torch.Tensor(train_df.iloc[:, :259].values)
    train_y = torch.Tensor(train_df[label].values).view(-1, 1)

    # Prepare the testing data
    test_x = torch.Tensor(test_df.iloc[:, :259].values)
    test_y = torch.Tensor(test_df[label].values).view(-1, 1)

    # Create data loaders for training and testing data
    train_dataset = TensorDataset(train_x, train_y)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

    test_dataset = TensorDataset(test_x, test_y)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Define the loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.004)

    # Train the model for phishing_label
    model, test_losses, best_epoch, min_test_loss = train_model(
        model, train_loader, test_loader, criterion, optimizer, num_epochs, label
    )

    # Test data from ALEC
    new_sample_values = [0, 4, 2, 4, 5, 3, 1, 1, 2, 4, 5, 5, 5, 5, 5, 5, 1, 3, 7, 7, 7, 7, 7, 7, 0, 4, 2, 0, 4, 4, 1, 2, 2, 1, 5, 1, 0, 2, 1, 1, 0, 0, 1, 1, 0, 1]

    df_copy = df.copy()

    new_sample = pd.Series(new_sample_values, index=df_copy.columns)
    df_copy = df_copy.append(new_sample, ignore_index=True)

    df_str_copy = df_copy.astype(str)
    df_one_hot_copy = pd.get_dummies(df_str_copy)

    test_sample_tensor = torch.tensor(list(df_one_hot_copy.loc[len(df_copy)-1].astype(int)), dtype=torch.float)  # Convert the tensor to float

    model.eval()
    with torch.no_grad():
        prediction = model(test_sample_tensor)
    
    return prediction

# Labels for each risk
labels = ['p_ransomware_label', 'p_phishing_label', 'p_insider_label', 'p_data_label', 'p_supply_label']

# Train and predict for each label
predictions = [train_and_predict(label) for label in labels]

# Print final result
for i, prediction in enumerate(predictions):
    print(f"Prediction for {labels[i]}: {prediction}")