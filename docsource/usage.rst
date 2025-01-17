Usage Guide
===========

Using the Makefile
------------------

The Makefile simplifies common tasks like setting up, training, and running the server and client.

Available Commands:
- **Setup Dependencies**: `make all`
- **Train the Model**: `make train`
- **Run the Server**: `make run_server`
- **Run the Client**: `make run_client`
- **Run Tests**: `make test`

Making Predictions
-------------------

Ensure the server and client are running, then use an API client like `curl` or Postman to send a POST request.

Example with `curl`:
.. code-block:: bash

   curl -X POST "http://127.0.0.1:8001/predict" \
   -H "Content-Type: application/json" \
   -d '{
         "distance_from_home": 10.5,
         "distance_from_last_transaction": 5.2,
         "ratio_to_median_purchase_price": 1.3,
         "repeat_retailer": 1,
         "used_chip": 0,
         "used_pin_number": 1,
         "online_order": 0
       }'

The server will return an encrypted prediction, which the client decrypts before displaying the result.
