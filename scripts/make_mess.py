#!/usr/bin/python

# This code intentionally left uncommented as to obfuscate it's workings
# I'm sure you've never heard that excuse before!

__author__ = "Kyle Barlow"

import os
import random
import shutil

data_dir = 'fake_bootcamp_data_output'

if os.path.isdir(data_dir):
    shutil.rmtree(data_dir)

os.mkdir(data_dir)

good_numbers = random.sample(xrange(100), random.randint(20, 40))
bad_numbers = random.sample(xrange(100), random.randint(20, 40))

numbers_lists = [good_numbers, bad_numbers]

def make_data_files(output_dir, total_score=False):
    files_to_make = random.randint(10, 50)
    for x in xrange(1, files_to_make+1):
        output_file = os.path.join(output_dir, 'data_%04d.txt' % x)
        with open(output_file, 'w') as f:
            for line_num in xrange(0, random.randint(100, 500)):
                f.write('Data point %06d=%.6f\n' % (line_num, random.random()) )
            if total_score:
                if random.random() >= 0.5:
                    f.write('Total score: %.2f\n' % random.random())
                else:
                    f.write('SEGFAULT\n')

for n in good_numbers:
    new_dir = os.path.join(data_dir, 'good_data_%d' % n)
    os.mkdir(new_dir)
    make_data_files(new_dir, total_score=True)

for n in bad_numbers:
    new_dir = os.path.join(data_dir, 'bad_data_%d' % n)
    os.mkdir(new_dir)
    make_data_files(new_dir)
