# Solutions to Everli's technical tasks

## Installation

Clone this repository:

```shell
git clone git@github.com:domcorvasce/everli-tasks
cd everli-tasks
```

Install the required dependencies for the third task:

```
pip3 install -r requirements.txt
```

## Task 1

[Check out solution](reverse_binary/reverse_binary.js)

**Language:** JavaScript

**Tested on:** Node.js v14.18.0

Write a function for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.


## Task 2

[Check out solution](change_directory/change_directory.php)

**Language:** PHP

**Tested on:** PHP 7.4.27

Write a function that provides change directory (`cd`) function for an abstract file system.

### Notes

1. root path is '/'.
2. path separator is '/'.
3. parent directory is addressable as '..'.
4. directory names consist only of English alphabet letters (A-Z and a-z).
5. the function will not be passed any invalid paths.
6. do not use built-in path-related functions.

### Example

```php
$path = new Path('/a/b/c/d');
$path->cd('../x');

echo $path->currentPath; //=> '/a/b/c/x'.
```

## Task 3

**Requirement:** `pip3 install haversine`

[Check out solution](haversine_coverage/haversine_coverage.py)

**Language:** Python

**Tested on:** Python 3.9.9

Suppose you have:
- a `haversine(lat1, lng1, lat2, lng2)` function that returns the distance (measured in km) between the coordinates of two given geographic point (`lat` and `lng` are latitude and longitude)

- an array of geographical zones (`locations`)

```python
locations = [
  {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
  {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
  {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
  {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
  # ...
]
```

- an array of shoppers

```python
shoppers = [
  {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
  {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
  {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
  {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
  {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
  {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
  {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]
```

The goal is to calculate the percentage of the zone covered by enabled shoppers (`coverage`). One shopper covers a zone if the distance among the coordinates is less than 10 km.

Resulted array should be sorted (desc) as the following one:

```python
sorted = [
  {'shopper_id': 'S3', 'coverage': 72},
  {'shopper_id': 'S1', 'coverage': 43},
  {'shopper_id': 'S6', 'coverage': 12},
]
```
