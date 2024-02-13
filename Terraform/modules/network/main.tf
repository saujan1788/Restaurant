# Existing VPC 
data "aws_vpc" "my_vpc"{
	id = "vpc-9b19e7e2"

}

# Existing Public Subnet 
data "aws_subnet" "existing_public_subnet" {
	id = "subnet-94311af2"
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

resource "aws_security_group" "private_k8s_sg_saujan" {
	name = "private-k8s-sg"
	description = "Security group for k8s instances in private subnet"
	vpc_id = data.aws_vpc.my_vpc.id

# Inbound rules Allow SSH from the public subnet

ingress {
	from_port = 22
	to_port = 22
	protocol = "tcp"
	cidr_blocks = [data.aws_subnet.existing_public_subnet.cidr_block]
	
}

# Default rule to allow all outbound traffic 

egress {
	from_port = 0
	to_port = 0
	protocol = "-1"
	cidr_blocks = ["0.0.0.0/0"]

}

tags = {
	Name = "PrivateK8sSG"
}


}


