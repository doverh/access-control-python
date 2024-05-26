# Read file and assign to a variable
def file_updates(import_file, denied_list):

    # Open files and assign to variables
    with open(import_file, "r") as file_ips, open(denied_list,"r") as file_denied_ips:
        #Read files and assign to arrays
        ip_addresses = file_ips.read()
        ip_addresses = ip_addresses.split('\n')
        remove_list = file_denied_ips.read()
        remove_list = remove_list.split('\n')
        for rm in remove_list:
            ip_addresses.remove(rm)
        #Convert the list back to a string and save the file using .join()
        with open(import_file, "w") as file:
            file.write("\n".join(ip_addresses))

file_updates("Data/ips_file.txt","Data/denied_ips.txt")

