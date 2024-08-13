from google.cloud import compute_v1

def create_instance(project_id, zone, instance_name):
    instance_client = compute_v1.InstancesClient()

    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = f"zones/{zone}/machineTypes/e2-small"

    # Add a simple configuration for the boot disk
    disk = compute_v1.AttachedDisk()
    disk.boot = True
    disk.initialize_params.source_image = "projects/debian-cloud/global/images/family/debian-11"
    instance.disks = [disk]

    # Set network interface to default
    network_interface = compute_v1.NetworkInterface()
    network_interface.name = "global/networks/default"
    instance.network_interfaces = [network_interface]

    # Create the instance
    operation = instance_client.insert_unary(
        project=project_id, zone=zone, instance_resource=instance
    )
    print(f"Instance {instance_name} created: {operation.status}")

if __name__ == "__main__":
    project_id = "still-totality-432312-r8"  # Your project ID
    zone = "us-central1-a"  # Your preferred zone
    instance_name = "radiant-instance-2"
    create_instance(project_id, zone, instance_name)
