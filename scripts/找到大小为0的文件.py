import os

root = r'D:\v2x\branch\1609_facility_r4.0_feature'
skip = [".git", ".vscode"]

def main(dir):
    for file in os.listdir(dir):
        if file in skip:
            continue
        filepath = os.path.join(dir, file)
        if os.path.isdir(filepath):
            main(filepath)
        elif os.path.isfile(filepath):
            if os.path.getsize(filepath) == 0:
                print(filepath)
            

if __name__ == "__main__":
    main(root)    