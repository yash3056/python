import os

def uninstall_packages(requirements_file):
    with open(requirements_file, 'r') as f:
        for line in f:
            package = line.strip()
            if package:
                os.system(f'pip uninstall -y {package}')

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    uninstall_packages(requirements_file)
