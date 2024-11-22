import shutil
import kagglehub

# Download latest version
path = kagglehub.dataset_download("himanshunakrani/iris-dataset")

destination_path = "G:/Sem5/Python/Iris"

shutil.move(path, destination_path)

