#!/usr/bin/python3

# Do not change this class
class DefaultConfig:
    a = 0.8
    b = 0.5
    frequency_weight = 2
    excluded_tag = 'exclude-from-launchbar'
    max_result_num = 80 # Set to None to cancel the limit. Note that this may cause performance issue!
    shortcut_path = '~/Documents/Devonthink' # Set to None to disable shortcut creation


# change this one
class UserConfig(DefaultConfig):
    a = 0.8
    b = 0.5
    frequency_weight = 2
    excluded_tag = 'exclude-from-launchbar'
    max_result_num = 80
    #shortcut_path = '~/Documents/Project Notes/'
    shortcut_path = "~/Documents/Ongoing/"
    #shortcut_path = "~/Library/Containers/com.softwareambience.Unclutter/Data/Library/Application Support/Unclutter/FileStorage/"
