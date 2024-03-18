import faker
from pathlib import Path

def fill_txt_files(folder_path, num_files):
    fake = faker.Faker()
    folder = Path(folder_path)

    for i in range(1, num_files+1):
        file_path = folder / f"file_{i}.txt"
        with file_path.open("w") as file:
            file.write(fake.text())

if __name__ == "__main__":
    folder_path = "./text"  
    num_files = 5  

    fill_txt_files(folder_path, num_files)