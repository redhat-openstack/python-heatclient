# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from heatclient.common import http
from heatclient.v1 import actions
from heatclient.v1 import events
from heatclient.v1 import resource_types
from heatclient.v1 import resources
from heatclient.v1 import stacks


class Client(http.HTTPClient):
    """Client for the Heat v1 API.

    :param string endpoint: A user-supplied endpoint URL for the heat
                            service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the Heat v1 API."""
        self.http_client = http.HTTPClient(*args, **kwargs)
        self.stacks = stacks.StackManager(self.http_client)
        self.resources = resources.ResourceManager(self.http_client)
        self.resource_types = resource_types.ResourceTypeManager(
            self.http_client)
        self.events = events.EventManager(self.http_client)
        self.actions = actions.ActionManager(self.http_client)
