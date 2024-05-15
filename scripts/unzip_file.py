#!/usr/bin/env python3

from zipfile import ZipFile

with ZipFile("../data/MachineLearningRating_v3.zip", "r") as f:
    f.extractall("../data")