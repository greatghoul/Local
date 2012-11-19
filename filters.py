#!/usr/bin/env python
#-*-coding:utf-8-*-


def dateformat(value, format="%Y-%m-%d %H:%M"):
    return value.strftime(format)


def empty(value, text=None):
    if not value:
        if text:
            return text
    return value


def error_class(field):
    print field
    return field.errors and 'error' or ''


def error_text(field, default='', sep='；'):
    return field.errors and sep.join(field.errors) or default
