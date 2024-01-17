# Define the exec resource to fix the spelling error in wp-settings.php
# change phpp to php
exec { 'fix_wp_settings':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
