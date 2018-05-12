import numpy as np
import pandas as pd
import pickle
import itertools


USER_FILE_ORIGIN = r"./data/members.csv"
SONG_FILE_ORIGIN = r"./data/songs.csv"
TRAIN_FILE_ORIGIN = r"./data/train.csv"
TEST_FILE_ORIGIN = r"./data/test.csv"

TRAIN_FILE = r"./train.pkl"
USER2SONGS = r"./user2songs.pkl"
SONG2USERS = r"./song2users.pkl"
