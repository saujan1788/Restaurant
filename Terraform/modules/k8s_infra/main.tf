resource "aws_instance" "k8s_Instance" {
  count         = var.instance_count
  ami           = "ami-0766b4b472db7e3b9"
  instance_type = "t2.medium"
  subnet_id     = "subnet-94311af2"  # Use the same subnet for all instances

  vpc_security_group_ids = ["sg-0cc759ffd6251c8ff"]

  tags = {
    Name = "k8s_Instance-${count.index}"
  }
}
