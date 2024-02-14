variable "availability_zones" {
  description = "A list of availability zones in the region"
  type        = list(string)
}

variable "instance_count" {
  description = "The number of instances to create"
  type        = number
  default     = 3
}

