# My Advent of Code Solutions

[![check](https://github.com/theobori/aoc/actions/workflows/check.yml/badge.svg)](https://github.com/theobori/aoc/actions/workflows/check.yml)

[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

This repository contains some [Advent of Code](https://adventofcode.com) challenges I have done for fun. Most of them were written for the [PyPy](https://pypy.org/) runtime.

The following command line template can be used to launch AoC solutions via Nix via dedicated branches.

```bash
nix run .#aoc-solutions.<year>.<day>.<part>.<static|dynamic>
```

The `default` key could be used instead of `aoc-solutions`. Dynamic versions are recommended for development because, unlike static versions, they don't need to rebuild the Nix derivation every time the source code changes. Dynamic versions are the equivalent of a command line like the one below.

```bash
nix run .# -- <year> <day> <part>
```

## The x launcher

The `x` launcher is an executable script written in Python whose main purpose is to run the Advent of Code solutions, which are executable scripts in Python. It can be used on its own, but this is not recommended, it is designed to be embedded in dynamic Nix derivations, mainly to handle certain error situations.
