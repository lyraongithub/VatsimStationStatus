# VATSIM ATC Station Status

Have you ever wanted a simple script to monitor the statis of ATC at your favourite airport on VATSIM? Then look no further.\n
VatsimStationStatus solves this issue by providing a number of scripts to accomidate a number of scenarios.

The script in the root directory is the script currently under development, with previous (completed) scripts in the /old_scripts directory. Unfortuantly, these older scripts are unikely to recieve bug fixes.

## To run:
1. Install requirements.
```
pip install requirements.txt
```
It is worth noteing that this file will reflect the requirements for the latest version of the script, so some unrequired libs may be installed.

2. Run the script of choice through your preffered method.
```
python3 SCRIPT_OF_CHOICE
```

## Still in developmment:
- [ ] Inpliment setting of station at startup.
- [X] Impliment Discord webhook intergration.
- [ ] Improve Discord webhook intergration to only post on station status change.