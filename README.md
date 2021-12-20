# Man-vs-Robot
A robot arm that plays chess against a human.

Video of its prototype working: https://www.youtube.com/watch?v=F6KBEtsqXN8

## Overview

I was never able to fully complete this project, but here is the high-level description.

The robot uses [Stockish](https://github.com/official-stockfish/Stockfish) chess engine as a backend to make moves. The user enters their move, and the robot arm makes its move. My laptop runs the chess engine and dictates the servo controller what to move through USB serial connection.

The robot arm code/math was built on one of my previous projects: [chess-robotic-arm](https://github.com/gallo-json/chess-robotic-arm)

## Tech stack

- Python 3
- PyChess library
- Serial TTL

## Hardware

- Computer running chess backend (my laptop)
- SSC-32U sservo controller (connected to computer via USB)
- Lynxmotion-AL5D robot arm
- Tournament-sized chess board and pieces

## Reflection and improvements

My reflection on this project is [here](docs/Reflection.md).
