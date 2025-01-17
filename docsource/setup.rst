Setup and Deployment
====================

Follow these steps to set up and deploy the Private-FHE-fraud-detection project:

Prerequisites
--------------

- Python 3.10.12 or later
- pip (Python package manager)
- Make
- Git

Steps
------

1. Clone the Repository:

   .. code-block:: bash

      git clone git@github.com:CirSandro/private-fhe-fraud-detection.git
      cd PFEE-ZAMA

2. Install Dependencies:

   .. code-block:: bash

      make all

3. Train the Model:

   .. code-block:: bash

      make train

4. Run the Server and Client:

   .. code-block:: bash

      make run_server
      make run_client

For additional details, refer to the sections on usage and workflow.
