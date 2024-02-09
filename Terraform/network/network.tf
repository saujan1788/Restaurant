# Existing VPC 
data "aws_vpc" "my_vpc"{
	id = "vpc-9b19e7e2"
}

# Existing Subnet 
data "aws_subnet" "exisiting_public_subnet" {
	id = "subnet-94311af2"
}

variable "availability_zones"{
	type = list(string)
}

resource "aws_subnet" "private_k8s_subnet"{
	vpc_id = data.aws_vpc.my_vpc.id
	cidr_block = "172.31.48.0/24" # Choose suitable block within the VPC
	availability_zone = var.availability_zones[0]

	tags = {
		Name = "saujan-private-k8s-subnet"
		saujan = "true"
	}
} 

