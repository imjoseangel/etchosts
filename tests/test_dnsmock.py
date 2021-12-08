#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R1710,W0621,W0613,C0301

from inspect import signature
import socket
import pytest
import dnsmock

EXPECTED_VERSION = '0.0.3'


@pytest.fixture
def mock_version():
    '''Returns Version'''
    return dnsmock.VERSION


@pytest.fixture
def mock_bind():
    '''Returns Socket Bind'''
    dnsmock.bind_ip('www.example.com', 443, '127.0.0.1')
    return str(dnsmock.lib.etc_hosts)


@pytest.fixture
def mock_custom_resolver():
    '''Test Custom Resolver'''
    return str(signature(dnsmock.lib.custom_resolver(socket.getaddrinfo)))


def test_version(mock_version):
    '''Test version'''
    assert mock_version == EXPECTED_VERSION


def test_bind(mock_bind):
    '''Test version'''
    assert mock_bind == "{('www.example.com', 443): [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('127.0.0.1', 443))]}"


def test_custom_resolver(mock_custom_resolver):
    '''Test custom resolver'''
    assert mock_custom_resolver == "(host, port, family=0, type=0, proto=0, flags=0)"
