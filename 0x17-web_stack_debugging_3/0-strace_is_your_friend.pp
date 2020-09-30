# Fixes a php file typo
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
