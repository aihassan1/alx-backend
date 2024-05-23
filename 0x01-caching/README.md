Caching Algorithms in Python
This repository contains Python code for implementing various caching algorithms:

Basic Cache: A simple cache with no limit on the number of items it can store.
FIFO Cache: Implements the First-In-First-Out (FIFO) algorithm, discarding the oldest item when the cache reaches its maximum capacity.
LIFO Cache: Implements the Last-In-First-Out (LIFO) algorithm, discarding the most recently added item when the cache reaches its maximum capacity.
LRU Cache: Implements the Least Recently Used (LRU) algorithm, discarding the least recently accessed item when the cache reaches its maximum capacity.
MRU Cache: Implements the Most Recently Used (MRU) algorithm, discarding the most recently used item when the cache reaches its maximum capacity.
Learning Objectives
By working on this project, you'll gain a deeper understanding of:

The concept of caching systems and their benefits.
Different cache replacement policies (FIFO, LIFO, LRU, MRU).
Implementing these algorithms in Python using a common base class.
Requirements
This project assumes you have the following:

Python 3 (version 3.7)
A code editor or IDE
Basic understanding of Python programming
Running the Tests
The code includes unit tests that you can run to verify its functionality. However, the specific instructions for running the tests might vary depending on your development environment.

File Structure
The repository includes the following files:

0-basic_cache.py: Implements the basic cache class.
1-fifo_cache.py: Implements the FIFO cache class.
2-lifo_cache.py: Implements the LIFO cache class.
3-lru_cache.py: Implements the LRU cache class.
4-mru_cache.py: Implements the MRU cache class.
base_caching.py: Defines the base class for all caching implementations.
README.md (this file): Provides an overview of the project.
