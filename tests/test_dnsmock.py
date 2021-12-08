#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R1710,W0621,W0613,C0301

import pytest
import dnsmock

EXPECTED_VERSION = '0.0.3'


@pytest.fixture
def mock_version():
    '''Returns Version'''
    return dnsmock.VERSION


def test_version(mock_version):
    '''Test version'''
    assert mock_version == EXPECTED_VERSION
