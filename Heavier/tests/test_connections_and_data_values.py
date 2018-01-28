'''
The MIT License (MIT)

Copyright (c) 2018 Wolfgang Almeida

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports Gerais
# ==============
import unittest
import requests

# Imports do programa
# ===================
from HeavierDownloader.ConfigReader import ConfigReader
from HeavierDownloader.PageScrapper import PageScrapper

# Classe de testes responsável por verificar os dados recebidos
# =============================================================
class TestCheckConnections(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader()

    # Verificando a disponibilidade da lista de ID's
    # ----------------------------------------------
    def test_check_list_id_availability(self):
        url = self.config.get_url_id_file()
        if url != "":
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
        else:
            self.assertTrue(False)  # Fail - url vazia

    # Verificando a conexão com o Heavy-R e os dados do vídeo (título e URL)
    # ----------------------------------------------------------------------
    def test_check_heavy_r_connection_and_video_data(self):
        video_id = "302692"
        url = self.config.get_template_url_page()
        if url != "":
            url = url % (video_id)
            response = requests.get(url)

            self.assertEqual(response.status_code, 200)

            scrapper = PageScrapper(response.text)
            self.assertIsNotNone(scrapper.get_video_title())
            self.assertIsNotNone(scrapper.get_video_url())
        else:
            self.assertTrue(False)  # Fail - url vazia