import hmac
import hashlib
import base64

def generate_token(user_key, secret_key):
    # Combine the user_key and secret_key
    message = user_key.encode('utf-8')  # Convert user_key to bytes
    secret = secret_key.encode('utf-8')  # Convert secret_key to bytes
    
    # Generate the HMAC-SHA256 hash
    hashed = hmac.new(secret, message, hashlib.sha256)
    
    # Convert the hash to a base64 encoded string (for easy transmission)
    token = base64.urlsafe_b64encode(hashed.digest()).decode('utf-8')
    
    return token
