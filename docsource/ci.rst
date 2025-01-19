Continuous Integration
======================

Private-FHE-fraud-detection utilizes GitHub Actions for continuous integration. The CI pipeline ensures code quality by running tests, checking commit messages, and validating builds.

Pipeline Steps
---------------

1. **Install Dependencies**:
   - Installs Python packages from `requirements.txt`.

2. **Run Tests**:
   - Executes the test suite in `tests/`.

3. **Validate Commit Messages**:
   - Ensures commit messages adhere to the defined format.
