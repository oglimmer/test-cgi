FROM httpd

ADD httpd.conf /usr/local/apache2/conf/httpd.conf
ADD cgi-bin /usr/local/apache2/cgi-bin/
