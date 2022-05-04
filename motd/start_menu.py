#!/usr/bin/env python3

# Adapted from the cutie project.
# Author:   kamik423
# Homepage: https://github.com/kamik423/cutie
# License:  MIT License

from os import _exit, system
from typing import List, Optional
import readchar

commands = {
	"tmux": {
		"caption": "  Restore Session....:",
		"command": "tmux attach -t default || tmux new -s default",
	},
	"htop": {
		"caption": "  Resource Monitor...:",
		"command": "htop",
	},
	"iptraf": {
		"caption": "  Network Monitor....:",
		"command": "iptraf-ng"
	},
}

class ExitInitiated(Exception):
	pass

class Keymaps:
	interrupt: List[str] = [readchar.key.CTRL_C]
	quit: List[str] = [readchar.key.ESC, "q", "\x1b\x1b"]
	confirm: List[str] = [readchar.key.ENTER]
	down: List[str] = [readchar.key.DOWN, "j", "h"]
	up: List[str] = [readchar.key.UP, "k", "t"]

def select(
		options: List[str],
		captions: Optional[List[int]] = None,
		prefix: str = '\33[4;32m',
		suffix: str = '\33[0m',
		index: int = 1) -> int:
	while True:
		print(f"\033[{len(commands)+1}A")
		for obj1, obj2 in zip(*[iter(options)]*2):
			pre = prefix if options.index(obj2) == index else ""
			print(f"\033[K{obj1} {pre}{obj2}{suffix}")
		keypress = readchar.readkey()
		if keypress in Keymaps.up:
			new_index = index
			while new_index > 0:
				new_index -= 1
				if new_index not in captions:
					index = new_index
					break
		elif keypress in Keymaps.down:
			new_index = index
			while new_index < len(options) - 1:
				new_index += 1
				if new_index not in captions:
					index = new_index
					break
		elif keypress in Keymaps.confirm:
			break
		elif keypress in Keymaps.interrupt:
			raise KeyboardInterrupt
		elif keypress in Keymaps.quit:
			raise ExitInitiated
	return index

def main():
	options = [i for p in commands.items() for i in [p[1]["caption"], p[0]]]
	print("\n" * (len(options) // 2), end="")
	captions = [i for i in range(0, len(options), 2)]
	selection = options[select(options, captions=captions)]
	system(commands[selection]["command"])
	print("\033[H\033[J\33[0m", end="", flush=True)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\033[H\033[J\33[0m", end="", flush=True)
		_exit(0)
	except ExitInitiated:
		_exit(0)

# vim: set noet:
