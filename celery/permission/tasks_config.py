#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-23 11:17:07


broker_url='amqp://guest@localhost//'
broker_url='amqp://delay-notify-client@localhost//'
result_backend='redis://localhost'
result_backend='rpc://delay-notify-server@localhost//'
timezone = 'Asia/Shanghai'
worker_concurrency=1
worker_redirect_stdouts_level="DEBUG"
worker_prefetch_multiplier=1
enable_utc = False
task_default_queue="tasks"
