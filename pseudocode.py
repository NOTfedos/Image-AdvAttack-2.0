def random_normal(x, y, z):
    pass

image = random_normal(3, 64, 64)
for epochs in range(EPOCHS):
    batch = []
    labels = []
    for class_ind in num_classes:
        batch.append(mask(image, class_ind))
        labels.append(class_ind)
    predictions = model(batch)
    loss = loss_function(predictions, labels)
    loss.backward()