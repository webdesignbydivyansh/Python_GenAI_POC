from google.cloud import storage

def upload_to_gcs(player_name, credentials_file="avid-phoenix-353111-b97e4c402031.json"):
    # Uploads a file to the bucket

    bucket_name = "pythongenai"           
    source_file_name = f"{player_name.replace(' ', '_')}.mp4" 
    destination_blob_name = f"videos/{player_name}.mp4"  

    storage_client = storage.Client.from_service_account_json(credentials_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"✅ File {source_file_name} uploaded to gs://{bucket_name}/{destination_blob_name}")
    return blob.public_url
    
