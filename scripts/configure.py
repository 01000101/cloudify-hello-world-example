# #######
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

'''
    lifecycle.Configure
    ~~~~~~~~~~~~~~~~~~~
    Configures the Cloudify test web application
'''

from os import remove
from cloudify import ctx

IIS_DEF_DIR = 'C:\\inetpub\\wwwroot\\'


def main():
    '''Entry point'''
    ctx.logger.info('Removing default IIS web application')
    remove('{0}{1}'.format(IIS_DEF_DIR, 'iisstart.htm'))
    ctx.logger.info('Downloading web application to {0}'.format(IIS_DEF_DIR))
    ctx.download_resource_and_render('index.html',
                                     '{0}{1}'.format(
                                         IIS_DEF_DIR, 'index.html'))
    ctx.download_resource_and_render('images/cloudify-logo.png',
                                     '{0}{1}'.format(
                                         IIS_DEF_DIR, 'cloudify-logo.png'))


main()
