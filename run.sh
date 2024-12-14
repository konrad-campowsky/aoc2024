#! /bin/sh

set -e

if [ -z "${1}" ] || [ -z "${2}" ]; then
	echo "usage: ${0} <target> <input>"
	exit 2
fi

export PYTHONPATH=`pwd`/aoclib

cd `dirname "${1}"`

exec python3 `basename "${1}"` < "${2}"
