output "instance_ids" {
  value = aws_instance.k8s_Instance.*.id
}


