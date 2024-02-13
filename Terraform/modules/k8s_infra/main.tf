resource "aws_instance" "k8s_Instance" {
  count         = var.instance_count
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  vpc_security_group_ids = [var.security_group_id]

  tags = {
    Name = "k8s_Instance-${count.index}"
  }
}

