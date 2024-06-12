import re
from azure.storage.blob import BlobServiceClient


CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=vaishalistorage;AccountKey=placeholder_value;EndpointSuffix=core.windows.net'
STORAGE_ACCOUNT_NAME = 'vaishalistorage'
CONTAINER_NAME = 'vaishalicontainer'

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)

def upload_file_to_azure(file):
    sanitized_filename = sanitize_filename(file.name)
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(sanitized_filename)
    blob_client.upload_blob(file, overwrite=True)

def download_file_from_azure(filename):
    sanitized_filename = sanitize_filename(filename)
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(sanitized_filename)
    download_stream = blob_client.download_blob()
    return download_stream.readall()

def list_files_in_azure_container():
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_list = container_client.list_blobs()
    return [blob.name for blob in blob_list]


#placeholder_value  enrTLtfa4PkRZcFzJTq5Wu/qyN3nThJ7Wk3RWEsxk77wF4O+WifHZllRkrEBf6UyzeOB7j70wdsV+ASt7zqk6w==

