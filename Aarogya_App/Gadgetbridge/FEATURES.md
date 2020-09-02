## Feature Matrix

|                                   | Pebble OG | Pebble Time/2 | Mi Band | Mi Band 2 | Mi Band 3 | Amazfit Bip | Amazfit Cor |
|-----------------------------------| ----------|---------------|---------|-----------|-----------|-------------|-------------|
|Calls Notification                 | YES       | YES           | YES     | YES       | YES       | YES         | YES         |
|Reject Calls                       | YES       | YES           | NO      | NO        | YES       | YES         | YES         |
|Accept Calls                       | NO(2)     | NO(2)         | NO      | NO        | NO        | NO          | NO          |
|Generic Notification               | YES       | YES           | YES     | YES       | YES       | YES         | YES         |
|Dismiss Notifications on Phone     | YES       | YES           | NO      | NO        | NO        | NO          | NO          |
|Predefined Replies                 | YES       | YES           | NO      | NO        | NO        | NO          | NO          |
|Voice Replies                      | N/A       | NO(3)         | N/A     | N/A       | N/A       | N/A         | N/A         |
|Calendar Sync                      | YES       | YES           | NO      | NO        | NO        | NO(3)       | NO          |
|Configure alarms from Gadgetbridge | NO        | NO            | YES     | YES       | YES       | YES         | YES         |
|Smart alarms                       | NO(1)     | YES           | YES     | NO        | NO        | NO          | NO          |
|Weather                            | NO(1)     | YES           | NO      | NO        | YES       | YES         | YES         |
|Activity Tracking                  | NO(1)     | YES           | YES     | YES       | YES       | YES         | YES         |
|GPS tracks import                  | NO        | NO            | NO      | NO        | NO        | YES         | NO          |
|Sleep Tracking                     | NO(1)     | YES           | YES     | YES       | YES       | YES         | YES         |
|HR Tracking                        | N/A       | YES           | YES     | YES       | YES       | YES         | YES         |
|Realtime Activity Tracking         | NO        | NO            | YES     | YES       | YES       | YES         | YES         |
|Music Control                      | YES       | YES           | NO      | NO        | NO        | NO          | YES         |
|Watchapp/face Installation         | YES       | YES           | NO      | NO        | NO        | YES         | YES         |
|Firmware Installation              | YES       | YES           | YES     | YES       | YES       | YES         | YES         |
|Taking Screenshots                 | YES       | YES           | NO      | NO        | NO        | NO          | NO          |
|Support Android Companion Apps     | YES       | YES           | NO      | NO        | NO        | NO          | NO          |

(1) Possible via 3rd Party Watchapp
(2) Theoretically possible (works on iOS, would need lot of work)
(3) Possible but not implemented yet


### Notes about Pebble Firmware >=3.0

* Gadgetbridge will keep track of installed watchfaces, but if the Pebble is used with another phone or another app, the information displayed in the app manager can get out of sync since it is impossible to query Firmware >= 3.x for installed apps/watchfaces.

