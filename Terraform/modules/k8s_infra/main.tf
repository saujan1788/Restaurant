# modules/k8s_infra/main.tf
resource "aws_instance" "k8s_Instance" {
  count         = var.instance_count
  ami           = "ami-0905a3c97561e0b69"
  instance_type = "t2.medium"
  subnet_id     = "subnet-94311af2"
  key_name      = "K8s_control"
  vpc_security_group_ids = ["sg-0cc759ffd6251c8ff"]

  root_block_device {
    delete_on_termination = true
  }

  tags = {
    Name = count.index == 0 ? "master" : "worker-${count.index}"
  }
}

resource "aws_ebs_volume" "k8s_ebs_volume" {
  count             = var.instance_count
  availability_zone = element(var.availability_zones, count.index)
  size              = 15
  type              = "gp2"
}

resource "aws_volume_attachment" "ebs_attachment" {
  count       = var.instance_count
  device_name = "/dev/sda1"
  volume_id   = aws_ebs_volume.k8s_ebs_volume[count.index].id
  instance_id = element(aws_instance.k8s_Instance.*.id, count.index)
}

output "instance_ids" {
  value = aws_instance.k8s_Instance.*.id
}

variable "instance_count" {
  type    = number
  default = 3
}

variable "availability_zones" {
  type = list(string)
}

