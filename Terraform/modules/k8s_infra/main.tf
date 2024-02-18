resource "aws_instance" "k8s_Instance" {
  count         = var.instance_count
  ami           = "ami-0905a3c97561e0b69"
  instance_type = "t2.medium"
  subnet_id     = "subnet-94311af2"  # Use the same subnet for all instances
  key_name      = "K8s_control"

  vpc_security_group_ids = ["sg-0cc759ffd6251c8ff"]

  tags = {
    Name = count.index == 0 ? "master" : "worker-${count.index}"
  }
}


