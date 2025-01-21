### Summary of Variables in Python

Variables in Python are used to store data that can be manipulated or referenced throughout a program. Below is a concise summary of key concepts regarding variables:

---

#### **1. Defining Variables**
- **No Declaration Needed**: Variables are created when a value is assigned to them.
  ```python
  x = 5
  name = "Alice"
  ```
- **Dynamic Typing**: The type of a variable is determined at runtime, and it can change.
  ```python
  x = 5       # x is an integer
  x = "hello" # x is now a string
  ```

---

#### **2. Naming Rules**
- Must begin with a letter (a-z, A-Z) or an underscore `_`.
- Can include letters, numbers (0-9), and underscores but cannot begin with a number.
- Case-sensitive: `myVar` and `myvar` are different.
- Cannot use Python reserved keywords (e.g., `if`, `while`, `True`).

---

#### **3. Types of Variables**
Python has built-in data types:
- **Numeric**: `int`, `float`, `complex`
- **Sequence**: `str`, `list`, `tuple`, `range`
- **Mapping**: `dict`
- **Set Types**: `set`, `frozenset`
- **Boolean**: `bool`
- **Binary**: `bytes`, `bytearray`, `memoryview`

---

#### **4. Assigning Values**
- **Single Assignment**: Assign one value to one variable.
  ```python
  x = 10
  ```
- **Multiple Assignment**: Assign multiple variables in one line.
  ```python
  a, b, c = 1, 2, 3
  ```
- **Same Value to Multiple Variables**:
  ```python
  x = y = z = 0
  ```

---

#### **5. Variable Scope**
- **Local**: Defined within a function and accessible only there.
- **Global**: Defined outside all functions and accessible throughout the program.
  ```python
  x = 10  # Global variable

  def func():
      y = 5  # Local variable
  ```

---

#### **6. Mutable vs Immutable Variables**
- **Immutable**: `int`, `float`, `str`, `tuple` (cannot change their value in place).
- **Mutable**: `list`, `dict`, `set` (can change their value in place).

---

#### **7. Type Checking**
- Use the `type()` function to check the type of a variable.
  ```python
  x = 42
  print(type(x))  # Output: <class 'int'>
  ```

---

#### **8. Best Practices**
- Use descriptive names: `age`, `price`, `user_name`.
- Follow conventions (PEP 8):
  - Variable names should use `snake_case`.
  - Avoid single-character names except for counters (`i`, `j`).
- Comment complex variables for clarity.

---

### Summary of Dictionaries in Python

Dictionaries are a powerful, built-in data structure in Python used to store data in key-value pairs. Below is a concise summary of key concepts about dictionaries:

---

#### **1. What is a Dictionary?**
- A dictionary is an **unordered**, **mutable**, and **indexed** collection of key-value pairs.
- Keys are unique, while values can be duplicated.
  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "New York"}
  ```

---

#### **2. Creating Dictionaries**
- Using curly braces `{}`:
  ```python
  my_dict = {"key1": "value1", "key2": "value2"}
  ```
- Using the `dict()` constructor:
  ```python
  my_dict = dict(name="Alice", age=25)
  ```

---

#### **3. Accessing Values**
- Use keys to access values:
  ```python
  print(my_dict["name"])  # Output: Alice
  ```
- Using the `.get()` method (prevents KeyError):
  ```python
  print(my_dict.get("age"))  # Output: 25
  ```

---

#### **4. Adding and Updating**
- Add or update key-value pairs:
  ```python
  my_dict["country"] = "USA"  # Adds a new key-value pair
  my_dict["age"] = 26        # Updates the value of an existing key
  ```

---

#### **5. Removing Elements**
- `pop(key)`: Removes a key-value pair and returns the value.
  ```python
  my_dict.pop("city")  # Removes "city"
  ```
- `popitem()`: Removes the last inserted key-value pair (Python 3.7+).
- `del`: Deletes a specific key or the entire dictionary.
  ```python
  del my_dict["name"]  # Deletes the key "name"
  del my_dict          # Deletes the dictionary
  ```
- `clear()`: Empties the dictionary.
  ```python
  my_dict.clear()
  ```

---

#### **6. Dictionary Methods**
- **Keys and Values**:
  ```python
  my_dict.keys()   # Returns all keys
  my_dict.values() # Returns all values
  my_dict.items()  # Returns all key-value pairs as tuples
  ```
- **Checking Membership**:
  ```python
  "name" in my_dict    # True if "name" exists as a key
  "city" not in my_dict
  ```

---

#### **7. Iterating Through a Dictionary**
- Iterate over keys:
  ```python
  for key in my_dict:
      print(key)
  ```
- Iterate over values:
  ```python
  for value in my_dict.values():
      print(value)
  ```
- Iterate over key-value pairs:
  ```python
  for key, value in my_dict.items():
      print(f"{key}: {value}")
  ```

---

#### **8. Nested Dictionaries**
- Dictionaries can hold other dictionaries as values:
  ```python
  nested_dict = {
      "person1": {"name": "Alice", "age": 25},
      "person2": {"name": "Bob", "age": 30}
  }
  ```

---

#### **9. Dictionary Comprehension**
- Create dictionaries using a concise syntax:
  ```python
  squares = {x: x**2 for x in range(1, 6)}
  print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  ```

---

#### **10. Best Practices**
- Use immutable types (e.g., `str`, `int`, `tuple`) as dictionary keys.
- Use `.get()` when unsure if a key exists to avoid errors.
- Prefer meaningful keys for readability:
  ```python
  employee = {"id": 101, "name": "Alice", "role": "Developer"}
  ```

---

We can use `type()` function to discover the type of the variable.

### Summary of Lists in Python

Lists are one of the most commonly used data structures in Python, designed to store collections of items. Here's a concise summary of key concepts about lists:

---

#### **1. What is a List?**
- A list is an **ordered**, **mutable**, and **indexable** collection of items.
- Lists can hold items of different data types, including other lists.
  ```python
  my_list = [1, "apple", 3.14, [1, 2, 3]]
  ```

---

#### **2. Creating Lists**
- Using square brackets:
  ```python
  my_list = [10, 20, 30]
  ```
- Using the `list()` constructor:
  ```python
  my_list = list(("apple", "banana", "cherry"))
  ```

---

#### **3. Accessing Elements**
- By **index** (starting at 0):
  ```python
  my_list[0]  # First element
  my_list[-1] # Last element
  ```
- By slicing:
  ```python
  my_list[1:3]  # Elements from index 1 to 2
  my_list[:2]   # First two elements
  my_list[::2]  # Every second element
  ```

---

#### **4. Modifying Lists**
- Change an element by index:
  ```python
  my_list[1] = "orange"
  ```
- Add elements:
  - `append()`: Adds a single item to the end.
    ```python
    my_list.append(40)
    ```
  - `extend()`: Adds multiple items.
    ```python
    my_list.extend([50, 60])
    ```
  - `insert()`: Adds an item at a specific index.
    ```python
    my_list.insert(1, "pear")
    ```

---

#### **5. Removing Elements**
- `remove()`: Removes the first occurrence of a specified value.
  ```python
  my_list.remove("apple")
  ```
- `pop()`: Removes an item by index and returns it.
  ```python
  my_list.pop(2)
  ```
- `del`: Deletes an item or the entire list.
  ```python
  del my_list[0]  # Deletes the first element
  del my_list      # Deletes the whole list
  ```
- `clear()`: Empties the list.
  ```python
  my_list.clear()
  ```

---

#### **6. List Operations**
- **Concatenation**:
  ```python
  new_list = [1, 2] + [3, 4]
  ```
- **Repetition**:
  ```python
  repeated = [1, 2] * 3  # Output: [1, 2, 1, 2, 1, 2]
  ```
- **Length**:
  ```python
  len(my_list)
  ```

---

#### **7. Iterating Through a List**
- Using a `for` loop:
  ```python
  for item in my_list:
      print(item)
  ```
- Using `enumerate()` to get both index and value:
  ```python
  for index, value in enumerate(my_list):
      print(index, value)
  ```

---

#### **8. List Methods**
- `sort()`: Sorts the list in place.
  ```python
  my_list.sort()
  ```
- `reverse()`: Reverses the list in place.
  ```python
  my_list.reverse()
  ```
- `count()`: Counts the occurrences of a value.
  ```python
  my_list.count(10)
  ```
- `index()`: Returns the index of the first occurrence of a value.
  ```python
  my_list.index(20)
  ```

---

#### **9. List Comprehension**
- A concise way to create lists:
  ```python
  squares = [x**2 for x in range(5)]
  print(squares)  # Output: [0, 1, 4, 9, 16]
  ```

---

#### **10. Nested Lists**
- Lists can contain other lists:
  ```python
  nested = [[1, 2], [3, 4, 5], [6]]
  print(nested[1][2])  # Output: 5
  ```

---

#### **11. Best Practices**
- Use descriptive names for lists (e.g., `students`, `prices`).
- Be cautious with `sort()` and `reverse()` as they modify the original list.
- Use list comprehensions for concise and readable code.

---