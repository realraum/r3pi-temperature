#!/bin/bash

tail -n 1 temp_log.csv | ssh home "cat >> /var/www/camp/temp_log.csv"
