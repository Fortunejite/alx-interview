#!/usr/bin/python3
from sys import stdin


def clear_dict(dict):
    for key in dict:
        dict[key] = 0

def main():
    loop = 1
    total_size = 0
    total_status = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    for logs in stdin:
        logs = logs.split()
        total_size += int(logs[8])
        total_status[logs[7]] += 1
        if loop >= 10:
          print ('File size: {}'.format(total_size))
          for i in total_status:
              if total_status[i] != 0:
                print ('{}: {}'.format(i, total_status[i]))
          loop = 1
          total_size = 0
          clear_dict(total_status)
          continue
        loop += 1

if __name__ == "__main__":
    main()