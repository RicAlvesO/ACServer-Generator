# Asseto Corsa Server Creator CLI
![Asseto Corsa Logo](./images/AC-LOGO.png)

Tool for automatically generate pressets for Asseto Corsa servers.

## Requirements

- Python 3.6+

## How to use

For help on how to use this tool, in the command line, run:

```bash
python3 acsc.py -h
#or 
python3 acsc.py --help
```

The command above will show you all the options available for this tool. For a better understanding of each option, please refer to the [manual](./docs/manual.md) page or see the table bellow:

| Option            | Short | Long                | Type      | Default         | Description                                        |
|-------------------|-------|---------------------|-----------|--------------   |----------------------------------------------------|
| Admin Password    | -a    | --admin-pass        | str       | 'password'      | Specify admin password for server                  |
| Back Mirror       | -b    | --back-mirror       | bool      | False           | Enable forced back mirror                          |
| Cars              | -c    | --cars              | List[str] | None            | Specify car(s) folder(s) for custom generation     |
| Dynamic Weather   | -d    | --dynamic           | bool      | False           | Enable dynamic weather option                      |
| Entry Password    | -e    | --entry-pass        | str       | ''              | Specify admin password for server                  |
| Folder Location   | -f    | --folder            | str       | './../'         | Specify custom folder location for game data       |
| Max Cars          | -m    | --max-cars          | int       | 20              | Specify max number of cars per preset              |
| Num Presets       | -n    | --num-presets       | int       | 1               | Specify number of presets generated per track      |
| Online Port       | -o    | --online-port       | int       | 8081            | Specify the port where server is hosted (HTTP)     |
| Practice Time     | -p    | --practice          | int       | 60              | Specify time in minutes for the practice session   |
| Qualify Time      | -q    | --qualify           | int       | 0               | Specify the time in minutes for the qualify session|
| Race Laps         | -r    | --race              | int       | 0               | Specify number of laps in a race                   |
| Server Extra File | -s    | --server-extra      | str       | 'extra_cfg.yml' | Specify custom 'extra_cfg.yml' file                |
| Tracks            | -t    | --tracks            | List[str] | None            | Specify track(s) folder(s) for custom generation   |
| UDP/TCP Port      | -u    | --udp-tcp-port      | int       | 9001            | Specify the port where server is hosted            |
| Verbose Mode      | -v    | --verbose           | bool      | False           | Enable verbose mode                                |
| Weather File      | -w    | --weather-file      | str       | 'weather.ini'   | Specify custom 'weather.ini' file                  |


*Note*: This tool is fan-made and not affiliated with Kunos Simulazioni in any way.

