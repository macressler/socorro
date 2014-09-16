.. index:: setup-socorro

Setting up Socorro reporting
============================

Socorro produces graphs and reports, most are updated once per day.

You must enter information about your releases into Socorro in order
for this to work, and this information must match the incoming crashes.

Becoming a superuser
--------------------

If you're starting a fresh new Socorro instance without any users at
all, you need to bootstrap at least one superuser so the paragraph
above starts to make sense. To do that, you first need to **sign in at
least once** using the email address you want to identify as a
superuser. Once you've done that, run the following command::

    cd /data/socorro
    ./socorro-virtualenv/bin/python webapp-django/manage.py makesuperuser theemail@address.com

Now the user with this email address should see a link to "Admin" in
the footer.

From this point on, you no longer need the command line to add other
superusers - you can do this from http://crash-stats/admin/users/

Adding new products and releases
--------------------------------

Each product you wish to have reports on must be added via the Socorro
admin UI:

http://crash-stats/admin/products/

All products must have one or more releases:

http://crash-stats/admin/releases/

Make sure to restart memcached so you see your changes right away:
::
  sudo /etc/init.d/memcached restart

Now go to the front page for your application. For example, if your application
was named "KillerApp" then it will appear at:

http://crash-stats/home/products/KillerApp

You should also change the DEFAULT_PRODUCT in local.py (/etc/socorro/local.py
in a packaged install, ./webapp-django/crashstats/settings/local.py otherwise).