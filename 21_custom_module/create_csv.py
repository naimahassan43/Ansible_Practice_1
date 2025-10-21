import csv

device_facts= {
        "r3": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "R3",
            "net_image": "bootflash:packages.conf",
            "net_iostype": "IOS-XE",
            "net_model": "CSR1000V",
            "net_operatingmode": "controller",
            "net_python_version": "3.12.3",
            "net_serialnum": "90FT2FXJ4N9",
            "net_system": "ios",
            "net_version": "16.08.01a",
            "network_resources": {}
        },
        "r1": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "R1",
            "net_image": "flash0:/vios-adventerprisek9-m",
            "net_iostype": "IOS",
            "net_model": "IOSv",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.12.3",
            "net_serialnum": "926U8Z887M0WS05QSU2Z3",
            "net_system": "ios",
            "net_version": "15.6(2)T",
            "network_resources": {}
        },
        "r2": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "R2",
            "net_image": "flash0:/vios-adventerprisek9-m",
            "net_iostype": "IOS",
            "net_model": "IOSv",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.12.3",
            "net_serialnum": "9ZW2QF6D8O016EAP9U46T",
            "net_system": "ios",
            "net_version": "15.6(2)T",
            "network_resources": {}
        }

    }

# print(device_facts)

sorted_device_facts = dict(sorted(device_facts.items()))

csv_filename = '/home/naima/Ansible_Practice_1/21_custom_module/new_generated_file.csv'
csv_header = ["inventory_name", "hostname", "model", "version", "serial_number"]

with open(csv_filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer.writeheader()
    for device, details in sorted_device_facts.items():
        writer.writerow({
            "inventory_name": device, 
            "hostname": details['net_hostname'], 
            "model": details['net_model'],
            "version": details['net_version'], 
            "serial_number": details['net_serialnum']
            })