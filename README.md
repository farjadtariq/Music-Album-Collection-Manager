# Music-Album-Collection-Manager

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [How to Run](#how-to-run)
5. [Results](#results)
6. [Analysis](#analysis)
7. [Significance](#significance)
8. [Author](#author)
9. [License](#license)

## Introduction
This Python project is designed to read a file containing information about a collection of music albums and build a structured dictionary to manage them. It provides functionalities to categorize albums by artists and display them.

## Features
- Reads a file containing the artist names, album titles, and release years (Sample file given)
- Builds a dictionary to categorize albums by artists
- Displays albums grouped by artists in a neat, human-readable format

## Technologies Used
- Python 3.x

## How to Run
1. Clone the repository.
2. Run `main.py`.
3. Enter the name of the file containing the music album information when prompted.

## Results
- The program outputs the album collection sorted by artist names.
- Each artist name is followed by the albums they have released, along with the release years.

## Analysis
1. **Data Structure**: The choice of dictionary as a data structure optimizes search and retrieval operations, offering \(O(1)\) complexity for adding new albums or artists.
  
2. **Readability**: The program produces an easy-to-read output that groups albums by artists, making it simple to view the entire collection.

3. **Scalability**: Due to its efficient data structure, the application can handle large collections of albums with minimal performance impact.

## Significance
1. **Organization**: Helps in organizing a large collection of music albums effectively.
2. **Accessibility**: Provides quick access to information like album names and their respective release years.
3. **Extendibility**: Can be extended to include more features like sorting albums by release year, genres, etc.

## Author
- **Farjad Tariq**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
