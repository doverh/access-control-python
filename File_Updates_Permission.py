# Read file and assign to a variable
def file_updates(import_file, denied_list):

    with open(import_file, "r") as file_a, open(denied_list,"r") as file_b:
        ip_addresses = file_a.read()
        ip_addresses = ip_addresses.split("\n")
        remove_list = file_b.read()
        remove_list = remove_list.split()
        for rm in remove_list:
            ip_addresses.remove(rm)
        #Conver the list back to a string and save the file using .join() to the string "\n"
        import_file.write(ip_addresses.join("\n"))



file_updates("Data/denied_ips.txt","Data/ips_file.txt")
