import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "25b8b0a678b997af8cd224620db4a8b25b450a50cdd1e9d2539a07fe20195999"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254715744353"])
print(response)
# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["2547xxxxxx"], callback=on_finish)