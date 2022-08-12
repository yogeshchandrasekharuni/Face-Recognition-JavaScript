import os

folder = "labeled_images"

for sub_folder in [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]:
    for idx, file in enumerate([f for f in os.listdir(os.path.join(folder, sub_folder)) if os.path.isfile(os.path.join(folder, sub_folder, f))]):
        path = os.path.join(folder, sub_folder, file)
        new_path = os.path.join(folder, sub_folder, str(idx) + os.path.splitext(file)[1])
        os.rename(path, new_path)

    print(f"Renamed {idx} files in {sub_folder}")