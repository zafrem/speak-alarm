#!/bin/sh

PROJECT_DIR=$(pwd)
HOME_DIR=$HOME

echo "Make symbolic link $HOME_DIR/alarm_speaking."

ln -s $PROJECT_DIR $HOME_DIR/alarm_speaking

echo "Launcher add crontab."
