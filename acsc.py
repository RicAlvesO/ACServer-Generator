import os
import sys
import json
import math
import random
import argparse


def generate_track_list(root_folder, selected, verbose=False):
    folder_list = []
    tracks_list = []
    tracks = os.scandir(root_folder)
    
    if selected:
        for track in selected:
            if os.path.isdir(os.path.join(root_folder, track)):
                tracks_list.append(track)
    else:
        for track in tracks:
            if track.is_dir():
                tracks_list.append(track.name)
    for track in tracks_list:
        layouts = os.scandir(os.path.join(root_folder, track, "ui"))
        lc=0
        for layout in layouts:
            if layout.is_dir():
                folder_list.append((track,layout.name))
                if verbose:
                    print("[Explorer] Found track '"+track+"' with layout '"+layout.name+"'")
                lc+=1
        if lc==0:
            folder_list.append((track,""))
            if verbose:
                print("[Explorer] Found track '"+track+"' with no layouts")
    return folder_list

def generate_car_list(root_folder, selected, verbose=False):
    folder_list = []
    cars_list = []
    tracks = os.scandir(root_folder)

    if selected:
        for car in selected:
            if os.path.isdir(os.path.join(root_folder, car)):
                cars_list.append(car)
    else:
        for car in tracks:
            if car.is_dir():
                cars_list.append(car.name)
    for car in cars_list:
        skins = os.scandir(os.path.join(root_folder, car, "skins"))
        lc=0
        for skin in skins:
            if skin.is_dir():
                folder_list.append((car,skin.name))
                if verbose:
                    print("[Explorer] Found car '"+car+"' with skin '"+skin.name+"'")
                lc+=1
        if lc==0:
            folder_list.append((car,""))
            if verbose:
                print("[Explorer] Found car '"+car+"' with no skins")
    return folder_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Asseto Corsa server generation tool")
    weather = parser.add_mutually_exclusive_group()

    parser.add_argument("name_tag", help="Name tag for distinguishing presets")

    parser.add_argument( "-a", "--admin-pass",    metavar="admin_password",  default='password',                help="Specify admin password for server")
    parser.add_argument( "-b", "--back-mirror",   action="store_true",                                          help="Enable forced back mirror")
    parser.add_argument( "-c", "--cars",          metavar="car_folder",      nargs='+',                         help="Specify car(s) folder(s) for custom generation")
    weather.add_argument("-d", "--dynamic",       action="store_true",                                          help="Enable dynamic weather option")
    parser.add_argument( "-e", "--entry-pass",    metavar="entry_password",  default='',                        help="Specify admin password for server")
    parser.add_argument( "-f", "--folder",        metavar="folder_location", default='./../',                   help="Specify custom folder location for game data")
    #g - free
    #h - taken
    #i - free
    #j - free
    #k - free
    #l - free
    parser.add_argument( "-m", "--max-cars",      metavar="car_amount",      default=20,              type=int, help="Specify max number of cars per preset")
    parser.add_argument( "-n", "--num-presets",   metavar="preset_amount",   default=1,               type=int, help="Specify number of presets generated per track (-1: All Cars)")
    parser.add_argument( "-o", "--online-port",   metavar="port",            default=8081,            type=int, help="Specify the port where server is hosted (HTTP)")
    parser.add_argument( "-p", "--practice",      metavar="minutes",         default=60,              type=int, help="Specify time in minutes for the practice session")
    parser.add_argument( "-q", "--qualify",       metavar="minutes",         default=0,               type=int, help="Specify the time in minutes for the qualify session")
    parser.add_argument( "-r", "--race",          metavar="laps",            default=0,               type=int, help="Specify number of laps in a race")
    parser.add_argument( "-s", "--server-extra",  metavar="extra_file",      default='extra_cfg.yml',           help="Specify custom 'extra_cfg.yml' file")
    parser.add_argument( "-t", "--tracks",        metavar="track_folder",    nargs='+',                         help="Specify track(s) folder(s) for custom generation")
    parser.add_argument( "-u", "--udp-tcp-port",  metavar="port",            default=9001,            type=int, help="Specify the port where server is hosted")
    parser.add_argument( "-v", "--verbose",       action="store_true",                                          help="Enable verbose mode")
    weather.add_argument("-w", "--weather-file",  metavar="weather_file",    default='weather.ini',             help="Specify custom 'weather.ini' file")
    #x - free
    #y - free
    #z - free


    args = parser.parse_args()

    if args.verbose:
        print("[Parser] Arguments passed:")
        # Basic usage
        print(f"[Parser] Name tag: {args.name_tag}")
        print(f"[Parser] Car folder(s): {args.car}")
        print(f"[Parser] Folder location: {args.folder}")
        print(f"[Parser] Max number of cars per preset: {args.max_cars}")
        print(f"[Parser] Number of presets per track: {args.num_presets}")
        print(f"[Parser] Server extra file: {args.server_extra}")
        print(f"[Parser] Track folder(s): {args.track}")
        print(f"[Parser] Verbose mode: {args.verbose}")

        # Weather options
        print(f"[Parser] Dynamic weather option: {args.dynamic}")
        print(f"[Parser] Weather file(s): {args.weather}")

        # Race args
        print(f"[Parser] Practice time in minutes: {args.practice}")
        print(f"[Parser] Qualify time in minutes: {args.qualify}")
        print(f"[Parser] Number of race laps: {args.race}")

        # Server passwords
        print(f"[Parser] Admin password: {args.admin_pass}")
        print(f"[Parser] Entry password: {args.entry_pass}")

    # Verify folder location
    if not os.path.isdir(args.folder):
        print("[Error] No game folder found at '"+args.folder+"'!", file=sys.stderr)
        exit()
    
    # Verify base car folder
    if not os.path.isdir(os.path.join(args.folder, "content", "cars")):
        print("[Error] No cars folder found at '"+os.path.join(args.folder, "content", "cars")+"'!", file=sys.stderr)
        exit()

    # Verify base track folder
    if not os.path.isdir(os.path.join(args.folder, "content", "tracks")):
        print("[Error] No tracks folder found at '"+os.path.join(args.folder, "content", "tracks")+"'!", file=sys.stderr)
        exit()

    # Verify all cars folders if passed
    if args.car:
        for car in args.car:
            car_folder=os.path.join(args.folder, "content", "cars", car)
            if not os.path.isdir(car_folder):
                print("[Error] No car folder found at '"+car_folder+"'!", file=sys.stderr)
                exit()
    
    # Verify all tracks folders if passed
    if args.track:
        for track in args.track:
            track_folder=os.path.join(args.folder, "content", "tracks", track)
            if not os.path.isdir(track_folder):
                print("[Error] No track folder found at '"+track_folder+"'!", file=sys.stderr)
                exit()

    # Get tracks layout list
    track_folder = os.path.join(args.folder, "content", "tracks")
    tracks = generate_track_list(track_folder, args.track , args.verbose)

    # Get cars skin list
    car_folder = os.path.join(args.folder, "content", "cars")
    cars = generate_car_list(car_folder, args.car, args.verbose)

    # Verbose info about tracks and cars found
    if args.verbose:
        print("[Explorer] Found "+str(len(tracks))+" tracks")
        print("[Explorer] Found "+str(len(cars))+" cars")
    
    # Generate presets
    for track in tracks:
        
        loaded = False
        
        # Get track info 
        try:
            if track[1] == "":
                track_info = json.load(open(os.path.join(track_folder,track[0],"ui","ui_track.json"),encoding="iso-8859-1"))
            else:
                track_info = json.load(open(os.path.join(track_folder,track[0],"ui",track[1],"ui_track.json") ,encoding="iso-8859-1"))
            loaded = True
        except:
            print(f'''[Error] Couldn't generate presets for track \'{track[0]}\' with layout \'{track[1]}\'!''', file=sys.stderr)
            continue

        if loaded:
            # Get max number of cars
            if args.max_cars>int(track_info["pitboxes"]):
                max = int(track_info["pitboxes"])
            else:
                max = int(args.max_cars)

            # If num presets is -1, generate presets for all cars
            if args.num_presets == -1:
                tot_for_track = math.ceil(len(cars)/max)
            else:
                tot_for_track = args.num_presets
            
            availabe_cars = cars.copy()
            
            # Generate preset name
            if track[1] == "":
                name = '{'+args.name_tag+'}'+track[0].replace(" ","_")
            else:
                name = '{'+args.name_tag+'}'+(track[0]+' '+track[1]).replace(" ","_").replace("_-_","_")

            if args.verbose:
                print(f'''[Generator] Generating {tot_for_track} preset(s) for \'{name}\' with {max} cars each''')

            # Get image of track
            try:
                if track[1] == "":
                    os.system(f'''copy "{os.path.join(track_folder,track[0],'ui','preview.png')}" "{os.path.join('images',name+'.png')}" > nul 2>&1''', )
                else:
                    os.system(f'''copy "{os.path.join(track_folder,track[0],'ui',track[1],'preview.png')}" "{os.path.join('images',name+'.png')}" > nul 2>&1''')
            except:
                print(f'''[Error] Couldn't save image for \'{name}\'''')
                continue

            # Generate n preset(s)
            for i in range(tot_for_track):
                aux_name=name+'_'+str(i+1)
                # Generate preset files
                tod = random.randint(0,160) - 80

                # Generate car lists
                car_list=''
                car_file = f''''''
                for i in range(max):
                    car = random.choice(availabe_cars)
                    availabe_cars.remove(car)
                    car_list += f'''{car[0]};'''
                    car_file += f'''[CAR_{i}]
MODEL={car[0]}
SKIN={car[1]}
SPECTATOR_MODE=0
DRIVERNAME=
TEAM=
GUID=
BALLAST=0
RESTRICTOR=0

'''   
                    if len(availabe_cars)==0:
                        availabe_cars = cars.copy()


                if args.practice<5:
                    args.practice=5
                track_file = f'''[SERVER]
NAME=Asseto LCA
CARS={car_list}
CONFIG_TRACK={track[1]}
TRACK={track[0]}
SUN_ANGLE={tod}
PASSWORD={args.entry_pass}
ADMIN_PASSWORD={args.admin_pass}
UDP_PORT={args.udp_tcp_port}
TCP_PORT={args.udp_tcp_port}
HTTP_PORT={args.online_port}
MAX_BALLAST_KG=150
QUALIFY_MAX_WAIT_PERC=120
RACE_PIT_WINDOW_START=0
RACE_PIT_WINDOW_END=0
REVERSED_GRID_RACE_POSITIONS=0
LOCKED_ENTRY_LIST=0
PICKUP_MODE_ENABLED=1
LOOP_MODE=1
SLEEP_TIME=1
CLIENT_SEND_INTERVAL_HZ=18
SEND_BUFFER_SIZE=0
RECV_BUFFER_SIZE=0
RACE_OVER_TIME=60
KICK_QUORUM=70
VOTING_QUORUM=70
VOTE_DURATION=20
BLACKLIST_MODE=0
FUEL_RATE=100
DAMAGE_MULTIPLIER=100
TYRE_WEAR_RATE=100
ALLOWED_TYRES_OUT=2
ABS_ALLOWED=1
TC_ALLOWED=1
START_RULE=0
RACE_GAS_PENALTY_DISABLED=0
TIME_OF_DAY_MULT=1
RESULT_SCREEN_TIME=20
MAX_CONTACTS_PER_KM=2
STABILITY_ALLOWED=0
AUTOCLUTCH_ALLOWED=1
TYRE_BLANKETS_ALLOWED=1
FORCE_VIRTUAL_MIRROR={args.back_mirror}
REGISTER_TO_LOBBY=1
MAX_CLIENTS={max}
NUM_THREADS=2
UDP_PLUGIN_LOCAL_PORT=0
UDP_PLUGIN_ADDRESS=
AUTH_PLUGIN_ADDRESS=
LEGAL_TYRES=
WELCOME_MESSAGE=

[FTP]
HOST=
LOGIN=
PASSWORD=pRYjB594D7V0tpdkO56wDQ==
FOLDER=
LINUX=1

[PRACTICE]
NAME=Practice
TIME={args.practice}
IS_OPEN=1
'''
                if args.qualify>0:
                    track_file +=f'''
[QUALIFY]
NAME=Qualify
TIME={args.qualify}
IS_OPEN=1
'''
                if args.race>0:
                    track_file +=f'''
[RACE]
NAME=Race
LAPS={args.race}
TIME=0
WAIT_TIME=120
IS_OPEN=1
__CM_TIME_OFF=10
'''

                track_file +=f'''
[DYNAMIC_TRACK]
SESSION_START=90
RANDOMNESS=10
SESSION_TRANSFER=50
LAP_GAIN=2

'''
                #add weather
                try:
                    f = open(args.weather,'r')
                    weather_file = f.read()
                    f.close()
                    track_file += weather_file
                except:
                    print(f'''[Error] Couldn't read weather file \'{args.weather}\'''')
                    exit()

                track_file +=f'''

[DATA]
DESCRIPTION= 
EXSERVEREXE=
EXSERVERBAT=
EXSERVERHIDEWIN=0
WEBLINK=
WELCOME_PATH=
'''

                
                try:
                    # Make dir inside preset folder with name
                    os.mkdir(os.path.join("presets",aux_name))
                    # Write track file
                    f = open(os.path.join('presets',aux_name,'server_cfg.ini'),'w')
                    f.write(track_file)
                    f.close()
                    # Write car file
                    f = open(os.path.join('presets',aux_name,'entry_list.ini'),'w')
                    f.write(car_file)
                    f.close()
                    # copy file extra_cfg.yml to folder
                    os.system(f'''copy extra_cfg.yml {os.path.join('presets',aux_name)} > nul 2>&1''')
                    if args.dynamic:
                        # open file and add dynamic weather option
                        f = open(os.path.join('presets',aux_name,'extra_cfg.yml'),'a')
                        f.write(f'''
---
!RandomWeatherConfiguration
# Minimum duration until next weather change
MinWeatherDurationMinutes: 10
# Maximum duration until next weather change
MaxWeatherDurationMinutes: 20
# Minimum weather transition duration
MinTransitionDurationSeconds: 180
# Maximum weather transition duration
MaxTransitionDurationSeconds: 600
''')
                except:
                    print(f'''Error Could not save preset \'{aux_name}\'''')
                

        