Some motd scripts I've written for personal use.

Scripts are based on, and meant to be used in conjunction with
<https://github.com/yboetz/motd>

==============================================================================
Contents                                                            *contents*

         1. Arch Linux Updates .............. |20-arch-updates|
         2. VPN Status ...................... |20-vpn-status|

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
vim: tw=78 ft=help
