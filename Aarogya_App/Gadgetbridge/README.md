Original app forked from [here](https://github.com/Freeyourgadget/Gadgetbridge).

For more info visit [link](https://github.com/abhaykes1/Gadgetbridge).

Gadgetbridge
============

Gadgetbridge is an Android (4.4+) application which will allow you to use your
Pebble, Mi Band, Amazfit Bip and HPlus device (and more) without the vendor's closed source application
and without the need to create an account and transmit any of your data to the
vendor's servers.


[Homepage](https://gadgetbridge.org)

[Blog](https://blog.freeyourgadget.org)

[![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/Gadgetbridge/donate)


[![Build](https://travis-ci.org/Freeyourgadget/Gadgetbridge.svg?branch=master)](https://travis-ci.org/Freeyourgadget/Gadgetbridge)
[![Code Quality: Java](https://img.shields.io/lgtm/grade/java/g/Freeyourgadget/Gadgetbridge.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Freeyourgadget/Gadgetbridge/context:java)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/Freeyourgadget/Gadgetbridge.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Freeyourgadget/Gadgetbridge/alerts)
[![Translate](https://hosted.weblate.org/widgets/freeyourgadget/-/gadgetbridge/svg-badge.svg)](https://hosted.weblate.org/projects/freeyourgadget/gadgetbridge)


[List of changes](https://codeberg.org/Freeyourgadget/Gadgetbridge/src/master/CHANGELOG.md)

## Supported Devices (Some of them WIP and some of them without maintainer)
* Amazfit Bip [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-Bip)
* Amazfit Bip Lite (NOT RECOMMENDED, NEEDS MI FIT WITH ACCOUNT ONCE) [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-Bip-Lite)
* Amazfit Cor [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-Cor)
* Amazfit Cor 2 [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-Cor-2)
* Amazfit GTR (NOT RECOMMENDED, NEEDS MI FIT WITH ACCOUNT ONCE) [Wiki] (https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-GTR)
* Amazfit GTS (NOT RECOMMENDED, NEEDS MI FIT WITH ACCOUNT ONCE) [Wiki] (https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Amazfit-GTS)
* BFH-16
* Casio GB-6900B
* HPlus Devices (e.g. ZeBand) [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/HPlus)
* ID115
* Lenovo Watch 9
* Liveview
* Makibes HR3
* Mi Band, Mi Band 1A, Mi Band 1S [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Mi-Band)
* Mi Band 2 [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Mi-Band-2)
* Mi Band 3 [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Mi-Band-3)
* Mi Band 4 (NOT RECOMMENDED, NEEDS MI FIT WITH ACCOUNT AND ROOT ONCE) [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Mi-Band-4)
* Mi Scale 2 (currently only displays a toast after stepping on the scale)
* NO.1 F1
* Pebble, Pebble Steel, Pebble Time, Pebble Time Steel, Pebble Time Round [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Pebble)
* Pebble 2 [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/Pebble)
* Teclast H10, H30
* XWatch (Affordable Chinese Casio-like smartwatches)
* Vibratissimo (experimental)
* ZeTime [Wiki](https://codeberg.org/Freeyourgadget/Gadgetbridge/wiki/MyKronoz-ZeTime)


## Features

Please see [FEATURES.md](https://codeberg.org/Freeyourgadget/Gadgetbridge/src/master/FEATURES.md)

## Authors
### Core Team (in order of first code contribution)

* Andreas Shimokawa
* Carsten Pfeiffer
* Daniele Gobbetti

### Additional device support
* João Paulo Barraca (HPlus)
* Vitaly Svyastyn (NO.1 F1)
* Sami Alaoui (Teclast H30)
* "ladbsoft" (XWatch)
* Sebastian Kranz (ZeTime)
* Vadim Kaushan (ID115)
* "maxirnilian" (Lenovo Watch 9)
* Andreas Böhler (Casio GB-6900B)
* Jean-François Greffier (Mi Scale 2)
* Johannes Schmitt (BFH-16)
* Lukas Schwichtenberg (Makibes HR3)

## Contribute

Contributions are welcome, be it feedback, bug reports, documentation, translation, research or code. Feel free to work
on any of the open [issues](https://github.com/Freeyourgadget/Gadgetbridge/issues?q=is%3Aopen+is%3Aissue);
just leave a comment that you're working on one to avoid duplicated work.

Translations can be contributed via https://hosted.weblate.org/projects/freeyourgadget/gadgetbridge/

## Do you have further questions or feedback?

Feel free to open an issue on our issue tracker, but please:
- do not use the issue tracker as a forum, do not ask for ETAs and read the issue conversation before posting
- use the search functionality to ensure that your question wasn't already answered. Don't forget to check the **closed** issues as well!
- remember that this is a community project, people are contributing in their free time because they like doing so: don't take the fun away! Be kind and constructive.
- Do not ask for help regarding your own projects, unless they are Gadgetbridge related

## Having problems?

0. Phone crashing during device discovery? Disable Privacy Guard (or similarly named functionality) during discovery.
1. Open Gadgetbridge's settings and check the option to write log files
2. Reproduce the problem you encountered
3. Check the logfile at /sdcard/Android/data/nodomain.freeyourgadget.gadgetbridge/files/gadgetbridge.log
4. File an issue at https://github.com/Freeyourgadget/Gadgetbridge/issues/new and possibly provide the logfile

Alternatively you may use the standard logcat functionality to access the log.
## Additional Changes

0. Updated UI of dashboard.
1. Added additional features like syncronization of heart beat with firebase database and emergency contact calling feature.
2. Added two activities of last recorded heart beat and sleep chart.

<img src='github_images/S1.jpeg' height=400 >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='github_images/S2.jpeg' height=400 >

<img src='github_images/S3.jpeg' height=400 >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='github_images/S4.jpeg' height=400 >



