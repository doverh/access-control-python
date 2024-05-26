# Access Control Algorithm

Python algorithm to control access.

## Initial Instructions

### Scope - Access Mngt Health care company

### System Design

1. Update a file that identifies the employees who can access restricted content.
2. File contains access information to personal patient records.
3. Employees are restricted access based on their IP address.
4. Allow list for IP addresses permitted to sign into the restricted subnetwork.
5. Remove list that identifies employees to be removed from this allow list.

### Project description


1. Create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list.
2. Remove those IP addresses from the file containing the allow list.

### Open the file that contains the allow list

Import the file "allow_list.txt" an assign it to a variable called "import_file". Open and read the file that contains the allow list and stores it into a variable called "file"

```python
import_file = "Data/allow_list.txt"
with open(import_file, "r") as import_file:
```

### Read the file contents

Read file content and assign to a variable.

``````python
ip_addresses = file.read()
```

### Convert the string into a list

ip_addresses = ip_addresses.split()

### Iterate through the remove list

[Add content here.]

### Remove IP addresses that are on the remove list

[Add content here.]

### Update the file with the revised list of IP addresses 

[Add content here.]

### Summary

## Reference

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
