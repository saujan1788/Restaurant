output "instance_ids" {
	value = aws_instance.k8s_Instance.*.id
}

output "instnace_private_ips" {
	value = aws_instance.k8s_Instance.*.private_ip
}
