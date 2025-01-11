<p align="center">
  <img src="logo-ou.png" alt="Logo">
</p>

<h1 align="center">KeyGen</h1>

<p align="center">

<a href="https://github.com/adaves1/keygen/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/adaves1/keygen?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/adaves1/keygen/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/adaves1/keygen?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/adaves1/keygen/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/adaves1/keygen?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/adaves1/keygen/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/adaves1/keygen?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/adaves1/keygen/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/adaves1/keygen?style=flat&color=e06c75&label="> </a>

<img src="https://img.shields.io/github/languages/code-size/adaves1/keygen" alt="GitHub code size in bytes"/>

<img src="https://img.shields.io/github/commit-activity/w/adaves1/keygen" alt="GitHub commit activity"/>

</p>

<p align="center">
  <strong>Just a module, or is it?</strong>
  <br>
  A module for generating random keys
  <br>
  <br>
  <a href="https://github.com/adaves1/keygen/wiki">Documentation</a>
  ·
  <a href="https://github.com/adaves1/keygen/issues">Report a Bug</a>
  ·
  <a href="https://github.com/adaves1/keygen/pulls">Request a Feature</a>
</p>

<br>

## Overview

You are in the home of the PKGMD (Python Key Generator Module Development) project.
The PKGMD (Python Key Generator Module Development) project is a growing, lively project to develop the `keygen` Python module together.

**KeyGen** is a Python module to make creating random keys easier. Think of a number. The number you just said is not completely random. Every number can be traced with some kind of pattern. 3627? Start with 3, multiply 3 with 2, then, decrement 3 by 1, then, increment 6 by the number you just decremented the most recent 3 by, which is 1.
Converting it into code, it looks like this:

```python
# Python 3.6

num = 3627

number_a = 1
number_b = 3 * 2
number_c = 3 - number_a
number_d = number_b + number_a
print("3" + number_b + number_c + number_d)

# Result: 3627 
```

For those who did not understand:

The first digit forms the third digit. 3 is decremented by 1, resulting in 2, the third number. Then, the second digit forms the last digit. 6 is incremented by 1 (The same number that is decremented from 3, the first digit), resulting in 7, the last digit.

From that, you can see that the cycle can continue since the only numbers needed are the third and last digits. Cut off 36. We get 27. We can get 2718, a new number from 27. Cut off 27, we get 1809 from 18. Cut off 18, we get 0990 or 990 from 09.

The point is that every number follows some kind of pattern. We have aimed to make utilities to generate, not the perfect and random key, but the most random key that humanity and all of computers can think of.

## Features



## Installation

```python
pip install keygen, random
```

## Usage


