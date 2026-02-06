hopefully this will be version 6

matpy.py — A lightweight Python library that mimics core MATLAB matrix syntax & operators

To publish a new version:
# 1. Bump the version (e.g., to 0.0.2)
poetry version patch

# 2. Commit the change to pyproject.toml
git commit -am "Bump version to $(poetry version --short)"

# 3. Create a git tag for the new version
git tag v$(poetry version --short)

# 4. Push the commit and the tag to GitHub
git push origin main
git push origin v$(poetry version --short)

poetry version patch
git commit -am "Bump version to $(poetry version --short)"
git tag v$(poetry version --short)
git push origin main
git push origin v$(poetry version --short)