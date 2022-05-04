Some motd scripts I've written for personal use.

Scripts are based on, and meant to be used in conjunction with
<https://github.com/yboetz/motd>

==============================================================================
Contents                                                            *contents*

         1. Arch Linux Updates .............. |20-arch-updates|
         2. VPN Status ...................... |20-vpn-status|
         3. rTorrent Status ................. |70-rtorrent-status|
         4. Start Menu ...................... |100-start-menu|

==============================================================================
1. Arch Linux Updates                                        *20-arch-updates*

Shows the number of available pacman and yay updates. Adds the output of the
commands `checkupdates | wc -l` and `yay -Qua | wc -l` together and displays
the result in the same syntax as 20-sysinfo and 20-uptime from yboetz/motd.

This script also creates a cache file in $HOME/.cache/$PROG where $PROG
is the result of `basename $0`. Where the cache file is kept, and how many
seconds must pass before the number of available updates is calculated again
can be easily changed by tweaking the script.

>
    system status:
      Updates.....: 321 (pacman, aur)
<

==============================================================================
2. VPN Status                                                  *20-vpn-status*

Shows whether ProtonVPN is connected. The script file offers a few different
ways of determining the status and showing the output; a method that doesn't
make external scripts can be used by commenting and uncommenting the
appropriate lines.

TODO: change the script to be non-blocking, so the next data can print
without needing the VPN request to finish. Could then use ANSI escape codes
to change the VPN status line.

TODO: clean up output formatting for VPN_INFO when the VPN is disconnected.

>
    system status:
      VPN.........: Connected (192.0.2.0, City)
<

==============================================================================
3. rTorrent Status                                        *70-rtorrent-status*

Shows some basic rTorrent stats using pyrocore's rtcontrol. Currently
supports service uptime, total uploaded size, total downloaded size, average
ratio, and number of actively uploading (seeding) torrents.

As is, I would personally comment out these statistics except uptime and
seeding.

TODO: uptime format should match the system `uptime` command format.

TODO: need to figure out how I can display uploaded, downloaded, and ratio
stats relative to either 24 hours, or maybe since last login or something.
Not sure yet if this will be possible with rtcontrol itself, might need
a cron job and some scripting to do the math manually.

TODO: find a better way to get uptime than the python cli

TODO: consider using caching or something to speed this one up. could
just run these as a script and cache them every 24 hours so they don't
need to be run on login.

TODO: what happens if rtorrent isn't running and these commands execute?
need to handle this case.

>
    rtorrent status:
      Uptime......: 20:52:55
      Uploaded....: 360.25T (total)
      Downloaded..: 2.05T (total)
      Ratio.......: 157.00 (avg)
      Seeding.....: 13 torrents
<

==============================================================================
4. Start Menu                                                 *100-start-menu*

Python script that modifies the cutie <https://github.com/kamik423/cutie>
library to create a neat little start menu. As with the rest of the scripts
in this directory, it's meant to be tinkered with and not necessarily used
as-in. Depends on the `python-readchar` library.

By default, if the keys `q` or `ESC` (probably have to hit it twice!) are
input then the script will exit. If `CTRL-C` is input, then the screen is
cleared and the script exists. The arrow keys or the Vim navigational keys
(`j`, `k`) can be used to move the cursor up or down. Press `ENTER` to
select the current item, and its associated command will be run through
a system call.

The `commands` dictionary can be updated as desired, but requires a specific
formatting style:

>
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
<

Each dictionary key is the value that will show on the right side of the
output that can be selected.

The bash script that executes the Python script hides the cursor and shows
it again once the menu exits. If this, or any other ANSI escape sequence
used, is incompatible with your terminal the result may be unpredictable.

The bash script calls the Python script assuming it's in the same working
directory. Since this is probably not the case, make sure to update that
line after moving the start_menu.py somewhere else!

>
    start menu:
      Restore Session....: tmux
      Resource Monitor...: htop
      Network Monitor....: iptraf
<

(selection not visible in above example, but the currently selected item
should be green with an underline: `printf '\33[4;32mexample\n\33[0m'`)

==============================================================================
vim: tw=78 ft=help et
