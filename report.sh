#!/bin/bash

pasta="/arachni/report"

if [ -d "$pasta" ]; then
    cd /arachni/bin
    ./arachni_reporter /arachni/report/report.afr --reporter=json
    mv /arachni/bin/*.json /arachni/report
    mv /arachni/report/*.json /arachni/report/report.json
else
    mkdir /arachni/report
    cd /arachni/bin
    ./arachni_reporter /arachni/report/report.afr --reporter=json
    mv /arachni/bin/*.json /arachni/report
    mv /arachni/report/*.json /arachni/report/report.json
fi

