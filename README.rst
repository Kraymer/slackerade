slackerade
==========

Masquerade yourself as fictitious user on slack

Usage
-----

::

    slackerade https://hooks.slack.com/services/CHANNEL/URL/HASH
    USERNAME MSG EMOJI_NAME
    
Note: to have access to the channel *Webhook Url* you must first activate slack legacy *Custom Integrations* feature as explained `here <https://api.slack.com/legacy/custom-integrations/incoming-webhooks>`_.

Install
-------

::

    pip3 install slackerade

Example
-------

``./slackerade.py https://hooks.slack.com/services/<censured> "The Joker"  "That's the joke" ":thats_the_joke:"``

gives :

.. figure:: https://github.com/Kraymer/public/raw/master/slackerade/slackerade_demo.png
   :alt:



Notify the `APP` tag next to the username so it can be distinguished from a real user.
