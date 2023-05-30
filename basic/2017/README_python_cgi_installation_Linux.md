HOW TO INSTALL PYTHON AND RUN CGI

1. INSTALL PYTHON ON THE LINUX SERVER
2. INSTALL THE APACHE2 
2. GO TO /etc/apache2/conf-enabled/serve-cgi-bin.conf
3. ADD THE BELOW CONFIGURATION:
	 ScriptAlias /cgi-bin/ /var/www/cgi-bin/
                <Directory "/var/www/cgi-bin/perl">
                        AllowOverride None
                        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                        Require all granted
                        AddHandler cgi-script .cgi .pl
                </Directory>
                <Directory "/var/www/cgin-bin/python">
                  Options +ExecCGI
                  AddHandler cgi-script .py
                  Order allow,deny
                  Allow from all
                </Directory>
4. AFTER MAKING CONFIG CHANGES RESTART THE APACHE2
5. sudo service apache2 restart