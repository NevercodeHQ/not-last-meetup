import re
import os

lines = []
with open(os.path.join(os.getenv('FCI_BUILD_DIR'), 'pubspec.yaml'), 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    match = re.match(r'version:\s?(\d+).(\d+).(\d+)(\+\d+)?', line)
    if match:
        g1, g2, g3, opt = match.group(1), match.group(2), match.group(3), match.group(4)
        print(g1, g2, g3, opt)
        lines[i] = f'version: {g1}.{g2}.{os.getenv("NEW_VERSION_CODE")}'

with open(os.path.join(os.getenv('FCI_BUILD_DIR'), 'pubspec.yaml'), 'w') as f:
    f.writelines(lines)