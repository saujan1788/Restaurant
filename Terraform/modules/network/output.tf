output "private_subnet_id" {
	value = aws_subnet.private_k8s_subnet.id
}

output "public_subnet_id"{
	value = data.aws_subnet.existing_public_subnet.id
}
