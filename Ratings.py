import csv

import pandas as pd
import numpy as np
import _sqlite3
import math
import statistics

pd.set_option('display.max_rows', 25)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 25)


def pearson(s1, s2):
    s1_copy = s1 - s1.mean()
    s2_copy = s2 - s2.mean()
    return np.sum(s1_copy * s2_copy) / np.sqrt(np.sum(s1_copy ** 2) * np.sum(s2_copy ** 2))


def load_training_dataset():
    with open('comp3208-train-small.csv', 'r') as f:
        reader = csv.reader(f)
        data = next(reader)
        query = 'insert into Training_ts values ({0})'
        query = query.format(','.join('?' * len(data)))
        cursor.execute(query, data)
        for data in reader:
            cursor.execute(query, data)
        connection.commit()


def load_testing_dataset():
    with open('comp3208-test-small.csv', 'r') as f:
        reader = csv.reader(f)
        data = next(reader)
        query = 'insert into Testing_ts values ({0})'
        query = query.format(','.join('?' * len(data)))
        cursor.execute(query, data)
        for data in reader:
            cursor.execute(query, data)
        connection.commit()


def pearson(user1, user2):
    user1_copy = user1 - statistics.mean(user1)
    user2_copy = user2 - statistics.mean(user2)
    return np.sum(user1_copy * user2_copy) / np.sqrt(np.sum(user1_copy ** 2) * np.sum(user2_copy ** 2))


connection = _sqlite3.connect("/Users/filipandonie/Desktop/projects/SocialComputingTechniques/comp3208-small.db")
cursor = connection.cursor()

# cursor.execute("create table Training_ts (user, item, rating, timestamp)")
# load_training_dataset()
# connection.commit()
#
# cursor.execute("create table Testing_ts (user, item, timestamp )")
# load_testing_dataset()
# connection.commit()
#
# cursor.execute("create table Training (user, item, rating)")
# cursor.execute("insert into Training select user, item, rating from Training_ts")
#
# cursor.execute("create table Testing (user, item )")
# cursor.execute("insert into Testing select user, item from Testing_ts")
#
# cursor.execute("drop table Training_ts")
# cursor.execute("drop table Testing_ts")

# connection.commit()

cursor.execute("select rating from Training where user='1' ")
user1 = cursor.fetchall()
user1 = [float(item[0]) for item in user1]
print(user1)

cursor.execute("select rating from Training where user='113'")
user2 = cursor.fetchall()
user2 = [float(item[0]) for item in user2]

print(pearson(user1, user2))

connection.close()
