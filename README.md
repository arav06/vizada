# Vizaga BDBMS

> Arav Budhiraja | 15th August 2022

A simple Blockchain Database Management System (BDMS) created using python
 
## Features

- Data is stored in the form of JSON
- Ability to create and delete tables
- Ability to create, delete and add data to tables
- Cannot modify/delete existing data in tables

## Installation

```bash
$ python3 setup.py

▀█ █▀  ▀  ▀▀█ █▀▀█ █▀▀▄ █▀▀█ 
 █▄█  ▀█▀ ▄▀  █▄▄█ █  █ █▄▄█ 
  ▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀  ▀  ▀ 

- By Arav Budhiraja


Enter the name of your database
> myDatabase

Creating 'myDatabase' database

myDatabase has been created!
You can access the database by executing python3 vizada.py myDatabase
```

## Usage

### Run the program

```bash
$ python3 vizada.py <DATABASE NAME>

▀█ █▀  ▀  ▀▀█ █▀▀█ █▀▀▄ █▀▀█
 █▄█  ▀█▀ ▄▀  █▄▄█ █  █ █▄▄█
  ▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀  ▀  ▀

Welcome!

>
```

### Create a Table

```bash
> ct newTable OR createtable newTable
```

### Delete a Table

```bash
> dt newTable OR deletetable newTable
```

### List Tables

```bash
> list OR ls OR listtables OR lt
hello
myTable
```

### View table contents

```bash
> vt myTable OR viewtable myTable
{"hello":"world","name":"test"}
{"database":"vizada","number":384}
```

### Insert data into table

```bash
> id myTable OR insertdata myTable
myTable> {"newData":"stuff","how are you":"good"}
```

### Exit

```bash
> exit OR bye
```

***
