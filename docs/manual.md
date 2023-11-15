# ASCS Manual

### Admin Password
- Alias: `-a`
- Extended Alias: `--admin-pass`
- Type: `str`
- Default: `'password'`
- Summary: Specify the admin password for the server.

### Back Mirror
- Alias: `-b`
- Extended Alias: `--back-mirror`
- Type: `bool`
- Default: `False`
- Summary: Enable forced back mirror.

### Cars
- Alias: `-c`
- Extended Alias: `--cars`
- Type: `List[str]`
- Default: `None`
- Summary: Specify car(s) folder(s) for custom generation.

### Dynamic Weather
- Alias: `-d`
- Extended Alias: `--dynamic`
- Type: `bool`
- Default: `False`
- Summary: Enable dynamic weather option.

### Entry Password
- Alias: `-e`
- Extended Alias: `--entry-pass`
- Type: `str`
- Default: `''`
- Summary: Specify the admin password for server entry.

### Folder Location
- Alias: `-f`
- Extended Alias: `--folder`
- Type: `str`
- Default: `'./../'`
- Summary: Specify custom folder location for game data.

### Max Cars
- Alias: `-m`
- Extended Alias: `--max-cars`
- Type: `int`
- Default: `20`
- Summary: Specify the maximum number of cars per preset.

### Num Presets
- Alias: `-n`
- Extended Alias: `--num-presets`
- Type: `int`
- Default: `1`
- Summary: Specify the number of presets generated per track.

### Online Port
- Alias: `-o`
- Extended Alias: `--online-port`
- Type: `int`
- Default: `8081`
- Summary: Specify the port where the server is hosted (HTTP).

### Practice Time
- Alias: `-p`
- Extended Alias: `--practice`
- Type: `int`
- Default: `60`
- Summary: Specify time in minutes for the practice session.

### Qualify Time
- Alias: `-q`
- Extended Alias: `--qualify`
- Type: `int`
- Default: `0`
- Summary: Specify the time in minutes for the qualify session.

### Race Laps
- Alias: `-r`
- Extended Alias: `--race`
- Type: `int`
- Default: `0`
- Summary: Specify the number of laps in a race.

### Server Extra File
- Alias: `-s`
- Extended Alias: `--server-extra`
- Type: `str`
- Default: `'extra_cfg.yml'`
- Summary: Specify a custom 'extra_cfg.yml' file for the server.

### Tracks
- Alias: `-t`
- Extended Alias: `--tracks`
- Type: `List[str]`
- Default: `None`
- Summary: Specify track(s) folder(s) for custom generation.

### UDP/TCP Port
- Alias: `-u`
- Extended Alias: `--udp-tcp-port`
- Type: `int`
- Default: `9001`
- Summary: Specify the port where the server is hosted.

### Verbose Mode
- Alias: `-v`
- Extended Alias: `--verbose`
- Type: `bool`
- Default: `False`
- Summary: Enable verbose mode.

### Weather File
- Alias: `-w`
- Extended Alias: `--weather-file`
- Type: `str`
- Default: `'weather.ini'`
- Summary: Specify a custom 'weather.ini' file for weather options.
