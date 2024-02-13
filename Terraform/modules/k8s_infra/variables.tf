variable "instance_type" {
	description = "The instance type for the EC2 instances"
	type = string 
	default = "t2.micro"

}

variable "ami_id" {
	description = "The AMI ID to use for the instances"
	type = string
}

variable "subnet_id" {
	description = "The ID of the subnet to launch the instances in"
	type = string
}

variable "security_group_id"{
	description = "The ID of the security group to associate with the instances"
	type = string
}

variable "instance_count" {
	description = "The number of insntances to create"
	type = number
	default = 3
}
