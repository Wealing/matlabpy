## Development

To publish a new version:

```bash
# 1. Bump the version (e.g., to 0.0.2)
poetry version patch

# 2. Commit the change to pyproject.toml
git commit -am "Bump version to $(poetry version --short)"

# 3. Create a git tag for the new version
git tag v$(poetry version --short)

# 4. Push the commit and the tag to GitHub
git push origin main
git push origin v$(poetry version --short)
```


## Testing

To run the tests:

```bash
poetry run pytest
```

## Testing the published package (to be replaced with CI/CD testing...)

### Go to a safe directory (away from your source code)
```bash
cd /tmp
```

```bash
# Create a throwaway virtualenv
python3 -m venv test_env
source test_env/bin/activate
```
### Install your new package
```bash
pip install matlabpy==0.0.4
```

### Verify it imports
```bash
python -c "import matlabpy; print(f'Success! Installed version: {matlabpy.__version__}')"
```

### Cleanup
```bash
deactivate
rm -rf test_env
```

### Cleanup
```bash
deactivate
rm -rf test_env
```
