# 0x17. Web stack debugging #3
## Fixing Typo Error in wp-settings.php
This Puppet module includes an `exec` resource to fix a typo error in the `wp-settings.php` file.
Correcting the error involves changing the instance(s) of 'phpp' to 'php'.

## Usage
Include this module in your Puppet manifest, and it will take care of correcting the error.

### Exec Resource Details
Parameters:
- **Title:** fix_wp_settings
- **Command:** sed -i 's/phpp/php/g' /var/www/html/wp-settings/php
- **Path:** /bin

Note: Adjust the file path to according to your environment

## Author
Edmund Eli Bansah - [Github](https://github.com/yung-wolf)
