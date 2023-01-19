import pathlib

src = pathlib.Path('/etc/')
for item in src.iterdir():
    print(item)
