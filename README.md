# Access Control Algorithm

Python algorithm to control access.

## Initial Instructions

### Scope - Access Mngt Health care company

### Rules and System Design

1. Update a file that identifies the employees who can access restricted content.
2. File contains access information to personal patient records.
3. Employees are restricted access based on their IP address.
4. Allow list for IP addresses permitted to sign into the restricted subnetwork.
5. Remove list that identifies employees to be removed from this allow list.

### Project description

1. Create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list.

1.1 Method receives 2 files as arguments

```python
def file_updates(import_file, denied_list):
```

2.Remove those IP addresses from the file containing the allow list.

Open file that contains the allow list and denied list.

```python
with open(import_file, "r") as file_ips, open(denied_list,"r") as file_denied_ips:
```

3.Read file content and assign to a variable.

```python
ip_addresses = file.read()
```

4.Convert the string into a list

Using the split method convert list into array.

```python
ip_addresses = ip_addresses.split()
```

5.Iterate through the remove list

```python
for rm in remove_list:
```

6.Remove IP addresses that are on the remove list

```python
ip_addresses.remove(rm)
```

7.Update the file with the revised list of IP addresses 

```python
with open(import_file, "w") as file:
            file.write("\n".join(ip_addresses))
```

## Reference

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
