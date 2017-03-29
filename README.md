# home-assistant-config

This repository contains my configuration for Home Assistant. It is installed on a Raspberry Pi model 2B.

## Database

I have quickly replaced the default sqlite database with MySQL.
The default database was growing rapidly and lead to bad performance.

To limit database growth, I limit recording as much as possible and purge the database for values older than 7 days.

## Contributions

If you have suggestions or improvements, please submit an issue or pull request.
