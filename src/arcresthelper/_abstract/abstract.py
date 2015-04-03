

dateTimeFormat = '%Y-%m-%d %H:%M'
import arcrest
from arcrest.agol import FeatureLayer
from arcrest.agol import FeatureService
from arcrest.hostedservice import AdminFeatureService
import datetime, time
import json
import os
from .. import common 
import gc


########################################################################
class baseToolsClass(object):
     #----------------------------------------------------------------------
    def __init__(self,
                 username,
                 password,
                 org_url=None,
                 token_url = None,
                 proxy_url=None,
                 proxy_port=None):

        """Constructor"""
        self._org_url = org_url
        self._username = username
        self._password = password
        self._proxy_url = proxy_url
        self._proxy_port = proxy_port
        self._token_url = token_url
        if self._org_url is None or self._org_url =='':
            self._org_url = 'http://www.arcgis.com'
        if self._org_url is None or '.arcgis.com' in self._org_url:
            self._securityHandler = arcrest.AGOLTokenSecurityHandler(username=self._username,
                                                              password=self._password,
                                                              org_url=self._org_url,
                                                              token_url=self._token_url,
                                                              proxy_url=self._proxy_url,
                                                              proxy_port=self._proxy_port)
            token = self._securityHandler.token
            #if 'error' in self._securityHandler.message and token is None:
                #if self._securityHandler.message['error']['code'] == 400:

                    #self._securityHandler = arcrest.OAuthSecurityHandler(client_id='',
                                                                         #secret_id='',
                                                                         #org_url=self._org_url,
                                                                         #proxy_url=self._proxy_url,
                                                                         #proxy_port=self._proxy_port)
                    #token = self._securityHandler.token
        else:

            self._securityHandler = arcrest.PortalTokenSecurityHandler(username=self._username,
                                                              password=self._password,
                                                              org_url=self._org_url,
                                                              proxy_url=self._proxy_url,
                                                              proxy_port=self._proxy_port)
            token = self._securityHandler.token
            #if 'error' in self._securityHandler.message and token is None:
                #if self._securityHandler.message['error']== 401:

                    #self._securityHandler = arcrest.OAuthSecurityHandler(client_id='s5CKlHcJoNSm07TP',
                                                                           #secret_id='6015feb0f44c4a5fa00e1e9486de8c48',
                                                                           #org_url=self._org_url,
                                                                           #proxy_url=self._proxy_url,
                                                                           #proxy_port=self._proxy_port)
                    #token = self._securityHandler.token

    #----------------------------------------------------------------------
    def dispose(self):
        self._username = None
        self._password = None
        self._org_url = None
        self._proxy_url = None
        self._proxy_port = None
        self._token_url = None
        self._securityHandler = None
        self._valid = None
        self._message = None

        del self._username
        del self._password
        del self._org_url
        del self._proxy_url
        del self._proxy_port
        del self._token_url
        del self._securityHandler
        del self._valid
        del self._message
    #----------------------------------------------------------------------
    @property
    def message(self):
        """ returns any messages """
        return self._message
    #----------------------------------------------------------------------
    @property
    def valid(self):
        """ returns boolean wether handler is valid """
        return self._valid