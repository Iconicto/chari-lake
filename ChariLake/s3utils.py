from storages.backends.gcloud import GoogleCloudStorage

MediaRootGoogleCloudStorage = lambda: GoogleCloudStorage(location='chari-lake/media')
