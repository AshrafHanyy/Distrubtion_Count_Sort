# Distribution Counting Sort with Manim

This repository contains a visualization of the **Distribution Counting Sort** algorithm using [Manim](https://manim.community/), a mathematical animation engine. The implementation is provided by **Ashraf Hany** as part of the course **CS312**.

## Overview

Distribution Counting Sort is a sorting algorithm that works efficiently for integers with a limited range. It operates by counting the occurrences of each element and then determining the correct position for each element in the sorted array based on these counts.

## Animation Description

The Manim animation begins with a visual representation of an array to be sorted. It then proceeds to illustrate the frequency and distribution arrays, showcasing the proper positions for the last occurrences of each element in the final sorted array.

The animation includes informative text, visualizing the step-by-step process of the algorithm, and highlighting key elements for better understanding.

## Usage

To run the animation, make sure you have Manim installed and execute the provided Python script.

```bash
manim -pql sort.py DistributionCountingSort
```

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#examples)
- [Contributing](#contributing)
