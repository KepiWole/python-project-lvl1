#!/usr/bin/env python3
from brain_games.cli import welcome_user
greeting = "Welcome to the Brain Games!"
def greet(greeting):
  print(greeting)
  welcome_user()
def main():
  greet(greeting)
if __name__ == '__main__':
  main()
