# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device a5y17lte
%define vendor samsung

%define vendor_pretty SAMSUNG
%define device_pretty Samsung A5 2017
%define droid_target_aarch64 1
%define installable_zip 1

%define android_config \
#define MALI_QUIRKS 1\
%{nil}


%define straggler_files \
/bugreports\
/d\
/product_service\
/product\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

