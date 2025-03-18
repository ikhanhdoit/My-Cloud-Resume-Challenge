variable "aws_profile" {
    description = "The AWS profile to use"
    default     = "default"  # Default profile if not overridden. Needs to be changed
}

variable "aws_region" {
    description = "AWS Region"
    default     = "us-east-1" # Change if different region
}

