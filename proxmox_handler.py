# from proxmoxer import ProxmoxAPI
# import os


# host = os.getenv("PROXMOX_HOST")
# user = os.getenv("PROXMOX_USER")
# password = os.getenv("PROXMOX_PASS")

# def create_vm(vm_config):
#     proxmox = ProxmoxAPI(
#         host,
#         user=user,
#         password=password,
#         verify_ssl=False
#     )
#     node = "pve"
#     vmid = int(vm_config.get("vmid", 102))

#     proxmox.nodes(node).qemu.create(
#         vmid=vmid,
#         name=vm_config["name"],
#         memory=vm_config["memory_mb"],
#         cores=vm_config["cpu_cores"],
#         ide0=f"local:{vm_config['disk_gb']},format=qcow2",
#         ostype=vm_config["os_type"],
#         net0="virtio,bridge=vmbr0",
#         iso=f"local:iso/{vm_config['iso_file']}"
#     )

import time

def create_vm(vm_config):
    print("📦 MOCK Proxmox VM Creation Triggered!")
    print("📝 VM Config Received:")
    for k, v in vm_config.items():
        print(f"  {k}: {v}")
    
    # Simulate delay
    time.sleep(1)

    # Simulate success
    print("✅ VM creation simulated successfully.")
    return {
        "status": "success",
        "vmid": vm_config.get("vmid", 102),
        "name": vm_config.get("name", "mock-vm")
    }