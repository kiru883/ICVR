
def set_class_names(classes, path):
    num_classes = len(classes)
    dataset_names_path = path + 'inference_model_data/dataset.names'
    dataset_data_path = path + 'inference_model_data/dataset.data'

    # write dataset.data
    dataset_data = f"classes = {num_classes}\nnames = {dataset_names_path}"
    with open(dataset_data_path, 'w') as ddf:
        ddf.write(dataset_data)

    # write dataset.names
    with open(dataset_names_path, 'w') as ddf:
        for cls in classes:
            ddf.write(f"{cls}\n")
