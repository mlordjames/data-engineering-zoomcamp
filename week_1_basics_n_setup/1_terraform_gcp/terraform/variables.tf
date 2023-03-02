locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  description = "Your GCP Project ID"
  default     = "de-terra-377820"
  type        = string

}

variable "gcp_region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "europe-west1"
  type        = string
}


# not needed for now
variable "bucket_name" {
  description = "The name of the Google Cloud Storage bucket. Must be globally unique."
  default     = ""
}

variable "storage_class" {
  description = "Storage class type of your Bucket. Check official docs for more info."
  default     = "STANDARD"

}

variable "BQ_DATASET" {
  description = "Big query dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "trips_data_all"
}

variable "TABLE_NAME" {
  description = "BigQuery Table"
  type        = string
  default     = "ny-trips"

}